"""Defines constants."""

import os

import dotenv

dotenv.load_dotenv(override=True)

AGENT_NAME = "orchestrator_agent"
DESCRIPTION = "A helpful assistant for orchestrating the project."
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "misfits-hackathon")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
MODEL = os.getenv("MODEL", "gemini-2.5-flash")

MCP_SERVER_URL = "https://mcp-agent-service-654936667955.us-central1.run.app/mcp/stream"