import json
import random
import time

import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "iot/agri/telemetry"


def main():
    client = mqtt.Client()
    client.connect(BROKER_HOST, BROKER_PORT, 60)

    try:
        while True:
            payload = {
                "device_id": "sensor-001",
                "temperature_c": round(random.uniform(18, 28), 2),
                "humidity_pct": round(random.uniform(45, 80), 2),
                "soil_moisture_pct": round(random.uniform(20, 60), 2),
            }
            client.publish(TOPIC, json.dumps(payload), qos=0)
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
