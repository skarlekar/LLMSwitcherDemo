import streamlit as st
import os
import sys
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_fireworks import ChatFireworks


# Check and load environment variables
# These are required for accessing the respective LLM APIs
required_env_vars = [
    "OPENAI_API_KEY",
    "HUGGINGFACE_API_KEY",
    "ANTHROPIC_API_KEY",
    "FIREWORKS_API_KEY"
]

# Verify that all required environment variables are set
for var in required_env_vars:
    value = os.getenv(var)
    if not value:
        print(f"Error: {var} environment variable is missing or empty.")
        sys.exit(1)

# Retrieve API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
fireworks_api_key = os.getenv("FIREWORKS_API_KEY")

def create_llm(option, temperature, max_tokens, top_k, top_p):
    """
    Create and return an LLM based on the selected option and parameters.
    Parameters are dynamically set using sliders in the UI.
    """
    if option == "OpenAI":
        return ChatOpenAI(model_name="gpt-4o-mini", temperature=temperature, api_key=openai_api_key, max_tokens=max_tokens)
    elif option == "Anthropic":
        return ChatAnthropic(model="claude-3-haiku-20240307", temperature=temperature, anthropic_api_key=anthropic_api_key, top_k=top_k, top_p=top_p, max_tokens=max_tokens)
    elif option == "HuggingFace":
        return ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta", temperature=temperature, huggingfacehub_api_token=huggingface_api_key, top_k=top_k, top_p=top_p, max_new_tokens=max_tokens, task="text-generation"))
    elif option == "Fireworks":
        return ChatFireworks(model="accounts/fireworks/models/llama-v3p1-70b-instruct", temperature=temperature, max_tokens=max_tokens)

def generate_response(llm, user_input):
    """
    Generate a response using the selected LLM.
    Constructs a prompt and processes the response through a chain of operations.
    """
    # Define the prompt template
    prompt = PromptTemplate(
        input_variables=["question"],
        template="Question: {question}\n\nAnswer:",
    )
    # Create a processing chain with the prompt, LLM, and output parser
    chain = prompt | llm | StrOutputParser()
    # Invoke the chain with the user's question
    response = chain.invoke({"question": user_input})
    return response

def main():
    # Set the title of the Streamlit app
    st.title("Multi-LLM Chat Application")

    # Sidebar for LLM selection
    st.sidebar.title("Select LLM")
    llm_option = st.sidebar.radio(
        "Choose an LLM:",
        ["OpenAI", "Anthropic", "HuggingFace", "Fireworks"],
        captions=["OpenAI/GPT-4o-mini", "Anthropic/claude-3-haiku-20240307", "HuggingFace/Zephyr-7B-Beta", "Fireworks/llama-v3p1-70b-instruct"],
        index=0
    )

    # Sliders for LLM parameters
    # Allow users to adjust parameters dynamically
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.sidebar.slider("Max Tokens", 25, 500, 300, 25)
    top_k = st.sidebar.slider("Top K", 20, 50, 36, 2)
    top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.9, 0.1)

    # Main section for user input
    # Default question is set to "What is an LLM?"
    user_input = st.text_area("Ask the LLM:", "What is an LLM?", height=150)
    if st.button("Ask"):
        if user_input:
            # Create the LLM with selected options and parameters
            llm = create_llm(llm_option, temperature, max_tokens, top_k, top_p)
            # Generate and display the response
            response = generate_response(llm, user_input)
            st.subheader(f"Response from {llm_option}:")
            st.markdown(response)
        else:
            # Warn the user if no input is provided
            st.warning("Please enter a question.")

# Entry point for the application
if __name__ == "__main__":
    main()
