"""
Explainer Agent

Explains concepts in a simple, beginner-friendly way using analogies and examples.
"""

import asyncio
import os
from typing import Any, Dict, Optional

import structlog
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

logger = structlog.get_logger(__name__)

EXPLAINER_AGENT_PROMPT = """
# 🛠️ TODO: Write the System Prompt for the Explainer Agent here
"""


class ExplainerAgent:
    """Agent that explains concepts in a simple, beginner-friendly way."""

    def __init__(self, model_name: str = "gemini-2.5-flash", temperature: float = 0.7) -> None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not set in environment.")
        self.model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=temperature,
        )
        logger.info("ExplainerAgent initialized", model=model_name)

    def run(self, query: str) -> str:
        """Run the explainer agent on a given query and return the response."""
        try:
            messages = [
                SystemMessage(content=EXPLAINER_AGENT_PROMPT),
                HumanMessage(content=query),
            ]
            response = self.model.invoke(messages)
            return response.content
        except Exception as e:
            logger.error("ExplainerAgent failed", error=str(e))
            return f"Sorry, I couldn't explain that right now. Error: {e}"
