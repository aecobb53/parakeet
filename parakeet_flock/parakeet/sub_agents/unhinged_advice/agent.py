
from google.adk.agents import LlmAgent

from .prompt import UNHINGED_ADVICE_PROMPT

MODEL = "gemini-2.0-flash"

unhinged_advice_agent = LlmAgent(
    name="unhinged_advice_agent",
    model=MODEL,
    description="An agent that provides unhinged advice.",
    instruction=UNHINGED_ADVICE_PROMPT,
)
