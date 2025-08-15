
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .prompt import ROOT_AGENT_PROMPT

from .sub_agents.unhinged_advice import unhinged_advice_agent


MODEL = "gemini-2.0-flash"
DESCRIPTION = """
This is a fun project to provide some hilarity and absurdity to the users.
"""

root_agent = LlmAgent(
    name="root_agent",
    model=MODEL,
    description=DESCRIPTION,
    instruction=ROOT_AGENT_PROMPT,
    tools=[
        AgentTool(unhinged_advice_agent),
    ],
)
