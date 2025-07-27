from fastapi import FastAPI, Request, Body, APIRouter
from typing import Dict

from publisher import publish_message

app = FastAPI()

@app.post("/publish/")
async def publish_endpoint(request: Request):
    payload = await request.json()
    print(f"Received payload: {payload}")
    message_id = publish_message(payload)
    print(f"Published message ID: {message_id}")
    return {"message_id": message_id}


# @app.post("/investment/")
# async def publish_endpoint(request: Request):
#     payload = await request.json()
#     print(f"Received payload: {payload}")
#     message_id = publish_message(payload)
#     print(f"Published message ID: {message_id}")
#     return {"message_id": message_id}
