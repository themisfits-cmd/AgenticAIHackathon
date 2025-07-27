import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from google.cloud import pubsub_v1
import json
from config import PROJECT_ID, TOPIC_ID

print(f"Loaded from .env: PROJECT_ID={PROJECT_ID}, TOPIC_ID={TOPIC_ID}")

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publish_message(payload: dict) -> str:
    message_data = json.dumps(payload).encode("utf-8")
    print(f"Publishing message to topic {TOPIC_ID} with data: {message_data}")
    try:
        future = publisher.publish(topic_path, message_data)
        print(f"Message published, waiting for result...")
        message_id = future.result(timeout=15)
        print(f"Message ID: {message_id}")
        return message_id
    except Exception as e:
        print(f"Failed to publish message: {e}")
        raise