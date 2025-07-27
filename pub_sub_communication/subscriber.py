import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from google.cloud import pubsub_v1
from config import PROJECT_ID, SUBSCRIPTION_ID

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"📥 Received: {message.data.decode('utf-8')}")
    message.ack()

def listen():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"🔄 Listening for messages on {subscription_path}...")

    try:
        streaming_pull_future.result()  # ⬅️ This keeps the subscriber running
    except KeyboardInterrupt:
        print("🔚 Stopping subscriber...")
        streaming_pull_future.cancel()

if __name__ == "__main__":
    listen()