import json
import logging
from typing import Optional

import paho.mqtt.client as mqtt

from .models import TelemetryIn
from .influx import write_telemetry
from ..settings import settings

logger = logging.getLogger(__name__)

MQTT_TOPIC = "iot/agri/telemetry"
_client: Optional[mqtt.Client] = None


def _on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("MQTT connected, subscribing to %s", MQTT_TOPIC)
        client.subscribe(MQTT_TOPIC)
    else:
        logger.error("MQTT connection failed: rc=%s", rc)


def _on_message(client, userdata, msg):
    try:
        payload_raw = msg.payload.decode("utf-8")
        payload_dict = json.loads(payload_raw)
        payload = TelemetryIn(**payload_dict)
        write_telemetry(payload)
        logger.info("Telemetry ingested from MQTT: %s", payload.device_id)
    except Exception as exc:
        logger.exception("Failed to ingest MQTT payload: %s", exc)


def start_mqtt_consumer() -> None:
    global _client
    if _client is not None:
        return

    client = mqtt.Client()
    client.on_connect = _on_connect
    client.on_message = _on_message
    client.connect(settings.mqtt_broker_host, settings.mqtt_broker_port, 60)
    client.loop_start()
    _client = client


def stop_mqtt_consumer() -> None:
    global _client
    if _client is None:
        return
    _client.loop_stop()
    _client.disconnect()
    _client = None
