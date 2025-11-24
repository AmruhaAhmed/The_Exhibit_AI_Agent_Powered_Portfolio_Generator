import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
os.getenv("GROQ_API_KEY")

with open("prompts/1_structuring_agent.md","r") as f:
    prompt_1_text=f.read()

llm_1 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.1
    )

agent_1 = create_agent(
    model=llm_1,
    tools=[],
    system_prompt=prompt_1_text
)

def run_structuring_agent(content):
    result = agent_1.invoke({
        "messages": [
            {"role": "user", "content": content}
        ]
    })
    ai_content = result['messages'][-1].content
    return ai_content
