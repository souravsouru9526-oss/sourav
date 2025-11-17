import os
import gradio
from groq import Groq
client = Groq(
    api_key=os.enivron.get("GROQ_API_KEY"),
)
def initialize_messages():
    return [{"role": "system",
             "content": """you are a skilled cook with successfull records."""}]
    messages_prmt = initialize_messages()
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to food"),
                     title="food ChatBot",
                     description="Chat bot for food information",
                     theme="soft",
                     examples=["hi"]
                     )
iface.launch(share=True)