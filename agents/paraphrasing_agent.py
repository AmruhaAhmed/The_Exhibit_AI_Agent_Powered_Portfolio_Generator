import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
os.getenv("GROQ_API_KEY")

with open("prompts/2_paraphrasing_agent.md","r",encoding="utf-8") as f:
    prompt_2_text=f.read()

llm_2 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.55
    )

agent_2 = create_agent(
    model=llm_2,
    tools=[],
    system_prompt=prompt_2_text
)

def run_paraphrasing_agent(content):
    result = agent_2.invoke({
        "messages": [
            {"role": "user", "content": content}
        ]
    })
    ai_content = result['messages'][-1].content
    return ai_content
