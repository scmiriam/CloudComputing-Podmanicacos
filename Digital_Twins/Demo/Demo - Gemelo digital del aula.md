---
tags: [demo, digital-twin, mqtt]
---
# Demo: classroom digital twin

A simulated classroom sensor sends CO₂, temperature and humidity to a cloud MQTT broker. A web dashboard shows the data live and can send the **Ventilate** command back to the sensor. That return channel is what makes it a **digital twin** rather than just a digital shadow (see [[Bidirectional Data Loop (Closed-Loop Feedback)]]).

Cost: zero. Everything is open source or free, and no accounts are needed.

## Architecture

```
[sensor.py] --data every 2 s--> [Public MQTT broker] --data--> [index.html]
     ^                          broker.hivemq.com                    |
     +------------------- "ventilate" / "stop" command --------------+
```

| Component | File / service | Technology |
|---|---|---|
| Simulated sensor | `sensor.py` | Python + paho-mqtt |
| Cloud broker | `broker.hivemq.com` (secure WebSockets, port 8884) | Public MQTT, no sign-up |
| Dashboard | `index.html` | mqtt.js + Chart.js, in the browser |

Topics:
- `uji-ccdt-podmanicacos/classroom1/sensors`: JSON readings (`co2`, `temp`, `hum`, `ventilating`, `ts`)
- `uji-ccdt-podmanicacos/classroom1/commands`: `ventilate` or `stop`

## How to run it

1. Install Python 3 and the library (first time only):
   ```
   pip install paho-mqtt
   ```
2. Open a terminal in this folder and start the sensor:
   ```
   python sensor.py
   ```
   You should see `Connected to broker.hivemq.com:8884` and one line per reading.
3. Open `index.html` by double-clicking it in the file explorer (or from GitHub Pages). The indicator in the top right should turn green and data starts arriving.

To open it from a phone or other computers, publish `index.html` on GitHub Pages. Nothing needs to change: the dashboard connects to the broker from anywhere.

## Demo script (about 3 minutes)

1. Start the sensor and show the terminal: "this is the physical classroom".
2. Show the dashboard: "this is its twin in the cloud". Data arrives every 2 seconds.
3. CO₂ rises (full classroom, windows closed). Once it passes 1000 ppm, the red alert fires (about 30–40 s after startup).
4. Press **Ventilate**: the terminal shows `Command received: VENTILATE` and CO₂ drops live.
5. Closing idea: if that button were pressed by an automatic rule or an AI model, the twin would go from descriptive to **prescriptive**.

## Troubleshooting

- **The dashboard doesn't connect**: the classroom Wi-Fi may block port 8884. Try a phone hotspot.
- **The HiveMQ broker is down**: use the backup broker on both sides.
  - Sensor: `python sensor.py --broker test.mosquitto.org --port 8081`
  - Dashboard: open `index.html?broker=wss://test.mosquitto.org:8081/mqtt`
- **Another group's data mixed in**: change the topic on both sides.
  - Sensor: `python sensor.py --topic another-unique-name/classroom1`
  - Dashboard: `index.html?topic=another-unique-name/classroom1`
- Plan C: have a recorded video of the demo working.

## Security (for the challenges section)

The broker is public: anyone who knows the topic can read the data or send commands. That is fine for a demo, but a real system would need authentication, TLS with per-device certificates and per-topic access control, as AWS IoT Core or Azure IoT Hub provide.
