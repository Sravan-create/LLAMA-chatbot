import streamlit as st
from groq import Groq

def main():
    st.set_page_config(page_title="LLaMA Chatbot", layout="centered")
    st.title("Chat with LLAMA")

    # Hardcoded API key (Security Risk!)
    client = Groq(api_key="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")

    # Single prompt input
    user_input = st.text_area("Enter your question:", height=100)
    
    if st.button("Get Answer"):
        if not user_input.strip():
            st.warning("The Responses are generated very quickly due to optimizations")
            return

        try:
            # Single-turn conversation (no history)
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # Updated to LLaMA model
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7,
                max_tokens=512
            )
            
            # Display answer
            st.subheader("Answer:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
