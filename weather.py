from praisonaiagents import Agent, MCP
import os

os.environ["OPENAI_BASE_URL"]="http://localhost:11434/v1"

agent = Agent(
    instructions="You are helpful Assisant", 
    llm="llama3.2",
    tools=MCP("python -m mcp_weather_server")
)

agent.start("What is the weather in Sacramento?")