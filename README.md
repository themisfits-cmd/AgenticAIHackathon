# AgenticAIHackathon
Code Base for the use case 6 - Let AI Speak to your money


# Fi Money MCP Multi-Agent Hackathon Project

This repository contains a multi-agent AI application built for the Google Cloud Agentic AI Hackathon. It leverages Fi Money's MCP (Model Context Protocol) for financial data access, Google ADK (Agent Development Kit) for agent logic, Vertex AI for reasoning with Gemini models, and Cloud Run for deployment. The architecture includes an orchestrator agent routing queries to functional finance agents (e.g., Wealth Management, Investment Advisory), using 6 tool calls derived from the Fi MCP dev repo.

## Features
- *Orchestrator Agent*: Routes user queries to specialized agents based on intent.
- *Functional Agents*: 9 agents covering wealth management, investments, debt, cash flow, credit, planning, risk, retirement, and fixed income.
- *Tool Calls*: 5 core from Fi MCP (fetch_net_worth, get_credit_report, get_epf_details, get_mutual_fund_transactions, get_bank_transactions) + 1 custom (analyze_loans).
- *Integration*: A2A protocol simulation for agent collaboration, mock MCP server for testing.
- *Tech Stack*: Python (Flask), Google ADK, Vertex AI (Gemini-2.5-pro), Cloud Run, Fi MCP mock endpoints.

## Prerequisites
- Google Cloud Project with Vertex AI and Cloud Run enabled.
- Deployed Vertex AI Endpoint for Gemini-2.5-pro (get endpoint ID via gcloud ai endpoints list).
- Fi Money MCP access (use mock server for dev; generate passcode via Fi app for production).
- Python 3.9+ and gcloud CLI installed/authenticated (gcloud auth application-default login).


## Deployed URL:

Firebase URL - https://studio--fi-wise.us-central1.hosted.app/dashboard

Fi MCP Deployed - https://mcp-agent-service-654936667955.us-central1.run.app/static/login.html

App Link - https://fi-nexus-backend-service-654936667955.us-central1.run.app/dev-ui/?app=Main_Agent
