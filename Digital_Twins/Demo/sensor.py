"""
Simulated sensor for a classroom digital twin (seminar demo).

Publishes CO2, temperature and humidity readings every 2 s to a public
MQTT broker and listens for commands coming back from the dashboard:
  - "ventilate": opens the ventilation, CO2 starts dropping
  - "stop":      closes the ventilation, CO2 starts rising again

Usage:
    pip install paho-mqtt
    python sensor.py

Options (all optional):
    python sensor.py --topic another-unique-topic/classroom1 --interval 1
"""

import argparse
import json
import random
import sys
import time

try:
    import paho.mqtt.client as mqtt
except ImportError:
    sys.exit("The paho-mqtt library is missing. Install it with:  pip install paho-mqtt")

# HiveMQ public broker over secure WebSockets (port 8884).
# It is the same one the dashboard uses, so if one connects, so does the other.
# Backup if it goes down: --broker test.mosquitto.org --port 8081
BROKER = "broker.hivemq.com"
PORT = 8884
TOPIC = "uji-ccdt-podmanicacos/classroom1"

parser = argparse.ArgumentParser(description="Simulated classroom sensor")
parser.add_argument("--broker", default=BROKER)
parser.add_argument("--port", type=int, default=PORT)
parser.add_argument("--topic", default=TOPIC, help="topic prefix, must be unique")
parser.add_argument("--interval", type=float, default=2.0, help="seconds between readings")
parser.add_argument("--no-tls", action="store_true", help="unencrypted WebSockets (e.g. a local broker)")
args = parser.parse_args()

TOPIC_SENSORS = f"{args.topic}/sensors"
TOPIC_COMMANDS = f"{args.topic}/commands"

# Simulated physical state of the classroom
state = {"co2": 650.0, "temp": 21.5, "hum": 45.0, "ventilating": False}


def on_connect(client, userdata, flags, reason_code, properties=None):
    if str(reason_code) in ("0", "Success"):
        print(f"Connected to {args.broker}:{args.port}")
        client.subscribe(TOPIC_COMMANDS)
        print(f"Publishing on  {TOPIC_SENSORS}")
        print(f"Listening on   {TOPIC_COMMANDS}\n")
    else:
        print(f"Connection error: {reason_code}")


def on_message(client, userdata, msg):
    command = msg.payload.decode().strip().lower()
    if command == "ventilate":
        state["ventilating"] = True
        print(">>> Command received: VENTILATE (opening ventilation)")
    elif command == "stop":
        state["ventilating"] = False
        print(">>> Command received: STOP (closing ventilation)")
    else:
        print(f">>> Unknown command: {command!r}")


def simulate_step():
    """Advances the simulation one step and returns the reading."""
    if state["ventilating"]:
        # Outside air comes in: CO2 drops, it cools down a bit and humidity drops
        state["co2"] -= random.uniform(25, 45)
        state["temp"] -= random.uniform(0.02, 0.08)
        state["hum"] -= random.uniform(0.1, 0.3)
    else:
        # Full classroom with the ventilation closed
        state["co2"] += random.uniform(10, 30)
        state["temp"] += random.uniform(0.0, 0.05)
        state["hum"] += random.uniform(0.0, 0.15)

    state["co2"] = max(420.0, min(state["co2"], 2500.0))
    state["temp"] = max(18.0, min(state["temp"], 28.0))
    state["hum"] = max(30.0, min(state["hum"], 70.0))

    return {
        "co2": round(state["co2"]),
        "temp": round(state["temp"] + random.uniform(-0.1, 0.1), 1),
        "hum": round(state["hum"] + random.uniform(-0.3, 0.3), 1),
        "ventilating": state["ventilating"],
        "ts": time.time(),
    }


def create_client():
    client_id = f"classroom-sensor-{random.randint(1000, 9999)}"
    try:  # paho-mqtt 2.x
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id, transport="websockets")
    except AttributeError:  # paho-mqtt 1.x
        client = mqtt.Client(client_id=client_id, transport="websockets")
    client.ws_set_options(path="/mqtt")
    if not args.no_tls:
        client.tls_set()
    client.on_connect = on_connect
    client.on_message = on_message
    return client


def main():
    client = create_client()
    print(f"Connecting to {args.broker}:{args.port} ...")
    client.connect(args.broker, args.port, keepalive=30)
    client.loop_start()
    try:
        while True:
            reading = simulate_step()
            client.publish(TOPIC_SENSORS, json.dumps(reading))
            vent = "ON " if reading["ventilating"] else "OFF"
            print(f"CO2 {reading['co2']:>5} ppm | {reading['temp']:>4} °C | "
                  f"{reading['hum']:>4} % | ventilation {vent}")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nSensor stopped.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
