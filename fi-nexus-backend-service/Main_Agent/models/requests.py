from pydantic import BaseModel

class AgentQuery(BaseModel):
    query: str