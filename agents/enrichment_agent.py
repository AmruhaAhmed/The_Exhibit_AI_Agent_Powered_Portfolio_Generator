import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
os.getenv("GROQ_API_KEY")

with open("prompts/3_enrichment_agent.md","r") as f:
    prompt_3_text=f.read()

llm_3 = ChatGroq(
    model="groq/compound-mini",
    temperature=0.6
    )

agent_3 = create_agent(
    model=llm_3,
    tools=[],
    system_prompt=prompt_3_text
)

def run_enrichment_agent(content):
    result = agent_3.invoke({
        "messages": [
            {"role": "user", "content": content}
        ]
    })
    ai_content = result['messages'][-1].content
    return ai_content

