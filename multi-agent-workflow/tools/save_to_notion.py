import asyncio

from langchain.tools import tool

from notion_mcp.notion_mcp_client import create_page

@tool
def save_notes_to_notion(title: str, content: str) -> str:
    """
    Save study notes or exam material to Notion.
    Use this when the user asks to save, write, or store notes in Notion.
    """
    print(f"Saving to Notion with title: {title} and content: {content}")
    return asyncio.run(create_page(title, content))