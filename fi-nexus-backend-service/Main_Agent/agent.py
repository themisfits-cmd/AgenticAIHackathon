from google.adk.agents.llm_agent import LlmAgent
from .shared_libraries import constants
from .sub_agents.mcp_agent.agent import mcp_connector_agent, InvestmentAnalysisAgent, WealthManagementAgent, CreditMonitoringAgent, RetirementPlanningAgent, CashFlowManagementAgent
from . import prompt
from google.adk.tools.agent_tool import AgentTool


root_agent = LlmAgent(
    model = constants.MODEL,
    name = constants.AGENT_NAME,
    description = constants.DESCRIPTION,
    instruction = prompt.ROOT_PROMPT,
    tools = [
        AgentTool(InvestmentAnalysisAgent),
        AgentTool(mcp_connector_agent),
        AgentTool(WealthManagementAgent),
        AgentTool(CreditMonitoringAgent),
        AgentTool(RetirementPlanningAgent),
        AgentTool(CashFlowManagementAgent),
    ],
)
