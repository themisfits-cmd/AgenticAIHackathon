import os
from dotenv import load_dotenv
load_dotenv()

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
project_id = os.getenv("PROJECT_ID")
topic_id = os.getenv("TOPIC_ID")
subscription_id = os.getenv("SUBSCRIPTION_ID")

if not credentials_path:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS not set in environment.")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

# Use the loaded values for your app
PROJECT_ID = project_id or "your-default-project-id"
TOPIC_ID = topic_id or "my-topic"
SUBSCRIPTION_ID = subscription_id or "my-subscription"