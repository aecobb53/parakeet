
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .prompt import UNHINGED_ADVICE_PROMPT



advice_agent = LlmAgent(
    name="unhinged_advice_agent",
    model="gemini-2.0-flash",
    description="An agent that provides unhinged advice.",
    instruction=UNHINGED_ADVICE_PROMPT,
)

root_agent = advice_agent
