import os
from functools import lru_cache

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # Load environment variables from .env file

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)


def get_current_directory() -> str:
    """Get the current working directory."""
    try:
        return os.getcwd()
    except Exception as e:
        return str(e)


def list_local_files(path: str = "./") -> str:
    """List all files in a local directory."""
    try:
        files = [file for file in os.listdir(path) if not file.endswith(".env")]
        return "\n".join(files)
    except Exception as e:
        return str(e)


def open_local_file(file_path: str) -> str:
    """Open and read a local file."""
    try:
        if file_path.endswith(".env"):
            return "Open .env.example instead of .env file."
        else:
            with open(file_path, "r") as file:
                content = file.read()
            return content
    except Exception as e:
        return str(e)


@lru_cache(maxsize=1)
def get_self_aware_agent():
    """Create and cache the self-aware agent on first use.

    This avoids performing potentially heavy initialization at import time.
    Call this function to get the agent instance.
    """
    return create_agent(
        model=llm,
        tools=[list_local_files, open_local_file, get_current_directory],
        system_prompt="You are a helpful assistant, by accessing your local files, you can understand what you can do.",
    )


__all__ = ["get_self_aware_agent"]
