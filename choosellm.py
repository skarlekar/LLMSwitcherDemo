import streamlit as st
import os
import sys
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_fireworks import ChatFireworks

TEMPERATURE = 0.7
MAX_TOKENS = 300
TOP_K = 35
TOP_P = 0.9

# Check and load environment variables
required_env_vars = [
    "OPENAI_API_KEY",
    "HUGGINGFACE_API_KEY",
    "ANTHROPIC_API_KEY",
    "FIREWORKS_API_KEY"
]

for var in required_env_vars:
    value = os.getenv(var)
    if not value:
        print(f"Error: {var} environment variable is missing or empty.")
        sys.exit(1)

openai_api_key = os.getenv("OPENAI_API_KEY")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
fireworks_api_key = os.getenv("FIREWORKS_API_KEY")

def create_llm(option):
    """
    Create and return an LLM based on the selected option.
    """
    if option == "OpenAI":
        return ChatOpenAI(model_name="gpt-4o-mini", temperature=TEMPERATURE, api_key=openai_api_key, max_tokens=MAX_TOKENS)
    elif option == "Anthropic":
        return ChatAnthropic(model="claude-3-haiku-20240307", temperature=TEMPERATURE, anthropic_api_key=anthropic_api_key, top_k=TOP_K, top_p=TOP_P, max_tokens=MAX_TOKENS)
    elif option == "HuggingFace":
        return ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta", temperature=TEMPERATURE, huggingfacehub_api_token=huggingface_api_key, top_k=TOP_K, top_p=TOP_P, max_new_tokens=MAX_TOKENS, task="text-generation"))
    elif option == "Fireworks":
        return ChatFireworks(model="accounts/fireworks/models/llama-v3p1-70b-instruct", temperature=TEMPERATURE, max_tokens=MAX_TOKENS)


def generate_response(llm, user_input):
    """
    Generate a response using the selected LLM.
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template="Question: {question}\n\nAnswer:",
    )
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"question": user_input})
    return response

def main():
    st.title("Multi-LLM Chat Application")

    # Sidebar for LLM selection
    st.sidebar.title("Select LLM")
    llm_option = st.sidebar.radio(
        "Choose an LLM:",
        ["OpenAI", "Anthropic", "HuggingFace", "Fireworks"],
        captions=["OpenAI/GPT-4o-mini", "Anthropic/claude-3-haiku-20240307", "HuggingFace/Zephyr-7B-Beta", "Fireworks/llama-v3p1-70b-instruct"],
        index=0
    )

    # Main section for user input
    user_input = st.text_area("Ask the LLM:", height=100)
    if st.button("Ask"):
        if user_input:
            llm = create_llm(llm_option)
            response = generate_response(llm, user_input)
            
            st.subheader(f"Response from {llm_option}:")
            st.code(response, language="markdown", wrap_lines=True)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
