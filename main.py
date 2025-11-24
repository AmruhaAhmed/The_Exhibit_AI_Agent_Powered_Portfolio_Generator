from agents.structuring_agent import run_structuring_agent
from agents.paraphrasing_agent import run_paraphrasing_agent
from agents.enrichment_agent import run_enrichment_agent
from agents.html_generator import run_html_generator_agent
import random
from langchain_core.runnables import RunnableLambda, RunnableSequence

def create_file():
    name="portfolio_"+""+str(random.randint(0,1000))
    print(name)
    return f"portfolio_site/{name}.html"

def append_styling():
    file=create_file()
    with open("portfolio_site/style.html","r",encoding="utf-8") as f:
        style_content=f.read()
    
    with open(file,"w",encoding="utf-8") as f:
        f.write(style_content)
    
    return file

def append_html(html_content):
    file=append_styling()
    with open(file,"a",encoding="utf-8") as f:
        f.write(html_content)

    return file
    
def pipeline(content):
    structured_output=RunnableLambda(lambda content: run_structuring_agent(content))
    paraphrased_output=RunnableLambda(lambda structured_output: run_paraphrasing_agent(structured_output))
    enriched_output=RunnableLambda(lambda paraphrased_output: run_enrichment_agent(paraphrased_output))
    html_output=RunnableLambda(lambda enriched_output:run_html_generator_agent(enriched_output))
    file_path=RunnableLambda(lambda html_content:append_html(html_content))

    workflow= RunnableSequence(
        first=structured_output,
        middle=[paraphrased_output,enriched_output, html_output],
        last=file_path
    )
    result=workflow.invoke(content)
    return result

