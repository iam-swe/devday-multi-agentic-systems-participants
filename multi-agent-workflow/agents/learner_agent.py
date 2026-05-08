"""
Learner Agent

Provides in-depth, exam-ready structured learning material for university students.
Uses a ReAct agent with a Firecrawl web-scraping tool for external enrichment.
"""

import os

import structlog
from langchain_core.messages import AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from tools.firecrawl_tool import get_learner_tools

logger = structlog.get_logger(__name__)

LEARNER_AGENT_PROMPT = """
# 🛠️ TODO: Write the System Prompt for the Learner Agent here

CONVERSATION CONTEXT:
{context}

"""


def _extract_text_from_message(message) -> str:
    """Convert a message's content (string or list of blocks) into plain text."""
    content = message.content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                parts.append(block.get("text", ""))
            elif isinstance(block, str):
                parts.append(block)
            else:
                parts.append(str(block))
        return "\n".join(p for p in parts if p.strip())
    return content


class LearnerAgent:
    """Agent that provides exam-ready structured learning material with web enrichment."""

    def __init__(self, model_name: str = "gemini-2.5-flash", temperature: float = 0.7) -> None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not set in environment.")
        self.model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=temperature,
        )
        self.tools = get_learner_tools()
        self.agent = create_react_agent(
            self.model,
            self.tools,
            prompt=LEARNER_AGENT_PROMPT,
        )
        logger.info("LearnerAgent initialized with tools", model=model_name, tools=[t.name for t in self.tools])

    def run(self, query: str) -> str:
        """Run the learner ReAct agent on a given query and return the response."""
        try:
            result = self.agent.invoke({"messages": [HumanMessage(content=query)]})
            final_message = result["messages"][-1]
            return _extract_text_from_message(final_message)
        except Exception as e:
            logger.error("LearnerAgent failed", error=str(e))
            return f"Sorry, I couldn't generate study material right now. Error: {e}"
