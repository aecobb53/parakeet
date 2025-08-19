
from google.adk.agents import LlmAgent

from .prompt import CLIMATE_CHANGE_PROMPT
from parakeet.default_env import MODEL

# MODEL = "gemini-2.0-flash"

climate_change_agent = LlmAgent(
    name="climate_change_agent",
    model=MODEL,
    description="An agent that provides information about climate change.",
    instruction=CLIMATE_CHANGE_PROMPT,
)
