import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()
os.getenv("GROQ_API_KEY")

with open("prompts/4_html_generating_agent.md","r") as f:
    prompt_4_text=f.read()


llm_4 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.1
    )

agent_4 = create_agent(
    model=llm_4,
    tools=[],
    system_prompt=prompt_4_text
)

def run_html_generator_agent(content):
  result = agent_4.invoke({
      "messages": [
          {"role": "user", "content": content}]})
  ai_content = result['messages'][-1].content
  return ai_content