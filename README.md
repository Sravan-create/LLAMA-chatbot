# LLAMA-chatbot
A simple Streamlit web application that interacts with Groq's LLaMA3-8b model for single-turn question answering.
This Streamlit app lets you chat with Meta’s LLaMA model via Groq’s API in three simple steps:

1. **Input**
   You type your question or prompt into the text area on the page.

2. **Request**
   When you click “Get Answer,” the app sends your text to Groq’s API (authenticated by your API key) using the `groq` Python client and the specified LLaMA 3 model.

3. **Response**
   Groq returns the model’s reply, which the app immediately displays under “Answer.”

All of the heavy lifting (tokenization, model inference, decoding) happens on Groq’s servers—Streamlit simply provides the UI, handles your input/output, and shows any errors if something goes wrong.
