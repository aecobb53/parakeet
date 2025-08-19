
from google.adk.agents import LlmAgent

from .prompt import CURRENT_EVENT_PROMPT
from parakeet.default_env import MODEL

# MODEL = "gemini-2.0-flash"

current_event_agent = LlmAgent(
    name="current_event_agent",
    model=MODEL,
    description="An agent that provides current event information.",
    instruction=CURRENT_EVENT_PROMPT,
)
