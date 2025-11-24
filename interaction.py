import gradio as gr
from main import pipeline
import html

def render_iframe(text):
    file_path = pipeline(text)
    with open(file_path, "r", encoding="utf-8") as f:
        raw_html = f.read()
    escaped = html.escape(raw_html)

    iframe = f"""
    <iframe style="width:100%; height:1000px; border:none;" 
            srcdoc="{escaped}">
    </iframe>
    """
    return iframe,file_path


with gr.Blocks() as demo:
    gr.Markdown("Portfolio Generation")

    with gr.Row():
        input = gr.Textbox(placeholder="Please enter the description",label="Description")
        generate_button = gr.Button("Generate")
    
    download_button=gr.File(label="Download HTML")
    output = gr.HTML()

    generate_button.click(
        fn=render_iframe,
        inputs=input,
        outputs=[output,download_button]
    )

demo.launch()
