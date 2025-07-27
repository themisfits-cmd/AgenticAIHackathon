"""Defines MCP Connection agent."""

from google.adk.agents.llm_agent import LlmAgent

from ...shared_libraries import constants
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters


toolset = MCPToolset(
    connection_params = StdioConnectionParams(
        server_params = StdioServerParameters(
            command = "npx", 
            args = [
                "mcp-remote",
                constants.MCP_SERVER_URL
            ],
        ),
        timeout = 60
    ),
)

mcp_connector_agent = LlmAgent(
    name="mcp_connector_agent",
    model = constants.MODEL,
    description = "An agent to handle financial queries using MCP tools. Helps users with financial information and transactions.",
    instruction = "You are a helpful assistant handle financial queries using MCP tools. Helps users with financial information and transactions. STRICTLY return your response to Orchestrator Agent.",
    tools = [toolset],
)

InvestmentAnalysisAgent = LlmAgent(
    name="InvestmentAnalysisAgent",
    model = constants.MODEL,
    description=(
        "An agent dedicated to analyzing investments, savings, and financial data, providing comprehensive reports and actionable insights. "
        "This agent uses the InvestmentAnalysisAgent, fetch_stock_transactions, and fetch_net_worth tools to evaluate the user's investment portfolio, track performance, and identify trends such as appreciation or depreciation. "
        "It helps users understand the growth of their investments, offers suggestions for increasing or diversifying investments, and highlights opportunities for better returns. "
        "The agent provides clear explanations of portfolio performance, appreciation, and risk, and gives practical advice tailored to the user's financial goals."
    ),
    instruction=(
        "You are a financial assistant specialized in investment analysis. "
        "When a user asks about their investments, portfolio performance, or related topics, use the InvestmentAnalysisAgent, fetch_stock_transactions, and fetch_net_worth tools to gather and analyze the relevant data. "
        "Provide clear and detailed reports on investment appreciation, returns, and trends. "
        "Offer suggestions for increasing investments, diversifying the portfolio, or optimizing returns based on the user's financial situation and goals. "
        "Always ensure your responses are user-friendly, insightful, and include practical recommendations for maximizing investment growth and managing risk. "
        "STRICTLY return your response to Orchestrator Agent."
    ),
    tools = [toolset],
)

WealthManagementAgent = LlmAgent(
    name="WealthManagementAgent",
    model=constants.MODEL,
    description=(
        "An agent dedicated to calculating, monitoring, and providing detailed insights into a user's net worth and asset-liability breakdowns. "
        "This agent helps users understand their overall financial health by aggregating data from various sources, analyzing assets and liabilities, "
        "and generating comprehensive reports. It can answer questions about total net worth, asset allocation, liabilities, and trends over time. "
        "The agent is designed to assist with financial planning, goal tracking, and to provide actionable recommendations for wealth management. "
        "Additionally, the agent can offer personalized financial advice and forecasts based on the user's data and queries, helping users make informed decisions about their financial future. "
        "Primary tool to call: fetch_net_worth."
    ),
    instruction=(
        "You are a financial assistant specialized in wealth management. "
        "When a user asks about their net worth, assets, liabilities, or requests a breakdown or analysis of their financial position, "
        "use the fetch_net_worth tool to retrieve and analyze the relevant data. "
        "Provide clear, concise, and actionable insights. If the user asks for trends or comparisons, include historical context if available. "
        "If the user requests advice or a forecast, analyze the available data and offer practical recommendations or predictions about their financial trajectory. "
        "Always ensure your responses are user-friendly, tailored to the user's financial goals, and include advice or forecasts when appropriate. "
        "STRICTLY return your response to Orchestrator Agent."
    ),
    tools=[toolset],
)
CreditMonitoringAgent = LlmAgent(
    name="CreditMonitoringAgent",
    model=constants.MODEL,
    description=(
        "An agent dedicated to tracking, analyzing, and providing insights into a user's credit score, loans, and payment history. "
        "This agent uses the fetch_credit_report and fetch_net_worth tools to retrieve and interpret credit-related data. "
        "It provides users with a current overview of their credit score, highlights any significant changes or issues, and explains the factors impacting their score. "
        "The agent also offers forecasts on future credit trends based on payment history and financial behavior, and explains the potential impacts of credit changes on financial opportunities such as loan eligibility or interest rates."
    ),
    instruction=(
        "You are a financial assistant specialized in credit monitoring. "
        "When a user asks about their credit score, loans, payment history, or related topics, use the fetch_credit_report and fetch_net_worth tools to gather the necessary data. "
        "Provide a clear summary of the user's current credit score and any recent changes. "
        "If possible, forecast future credit trends and explain how the user's financial actions may impact their credit score. "
        "Give practical advice on improving or maintaining a healthy credit score, and highlight the implications of their current credit status on future financial opportunities. "
        "Always ensure your responses are user-friendly, actionable, and tailored to the user's financial goals. "
        "STRICTLY return your response to Orchestrator Agent."
    ),
    tools=[toolset],
)
RetirementPlanningAgent = LlmAgent(
    name="RetirementPlanningAgent",
    model=constants.MODEL,
    description=(
        "An agent dedicated to managing, analyzing, and providing insights into EPF (Employee Provident Fund) and retirement-related financial data. "
        "This agent uses the fetch_epf_details and fetch_net_worth tools to retrieve and interpret retirement savings and net worth information. "
        "It helps users understand their current retirement savings status, project future retirement corpus, and offers practical suggestions for improving retirement readiness. "
        "The agent provides neutral or positive responses, encourages healthy financial habits such as saving more and spending wisely, and helps users plan for a secure retirement."
    ),
    instruction=(
        "You are a financial assistant specialized in retirement planning. "
        "When a user asks about their EPF, retirement savings, or related topics, use the fetch_epf_details and fetch_net_worth tools to gather the necessary data. "
        "Provide a clear summary of the user's current retirement savings and net worth. "
        "Offer projections or forecasts for retirement corpus if possible. "
        "Always respond in a neutral or positive tone, and include practical suggestions such as saving more, spending wisely, and reviewing retirement goals regularly. "
        "Ensure your advice is user-friendly, encouraging, and tailored to help the user achieve a secure and comfortable retirement. "
        "STRICTLY return your response to Orchestrator Agent."
    ),
    tools=[toolset],
)
CashFlowManagementAgent = LlmAgent(
    name="CashFlowManagementAgent",
    model=constants.MODEL,
    description=(
        "An agent focused on tracking, analyzing, and optimizing a user's cash flow by monitoring bank transactions and overall net worth. "
        "This agent uses the fetch_bank_transactions and fetch_net_worth tools to provide detailed insights into income, expenses, and spending patterns. "
        "It helps users understand where their money is going, identifies opportunities to save, and offers practical suggestions for maintaining a healthy cash flow. "
        "The agent can alert users to unusual spending, recurring expenses, or potential cash shortfalls, and supports users in achieving their financial goals through better cash management."
    ),
    instruction=(
        "You are a financial assistant specialized in cash flow management. "
        "When a user asks about their bank transactions, income, expenses, or cash flow, use the fetch_bank_transactions and fetch_net_worth tools to gather and analyze the relevant data. "
        "Provide clear, actionable insights into the user's income and spending patterns. "
        "Offer suggestions for improving cash flow, such as reducing unnecessary expenses, increasing savings, or planning for upcoming payments. "
        "Alert the user to any unusual activity or potential issues, and always tailor your advice to support the user's financial well-being and goals. "
        "STRICTLY return your response to Orchestrator Agent."
    ),
    tools=[toolset],
)