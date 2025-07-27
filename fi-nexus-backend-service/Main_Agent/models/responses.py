from pydantic import BaseModel

class AgentResponse(BaseModel):
    response: str
    agent_name: str