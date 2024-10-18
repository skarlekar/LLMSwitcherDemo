from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_fireworks import ChatFireworks
import os

TEMPERATURE = 0.7
MAX_TOKENS = 300
TOP_K = 35
TOP_P = 0.9

# Function to run a chain and print the response
def run_chain(chain, name):
    print(f"\n{name} response:")
    response = chain.invoke({"question": question})
    print(response)

# Set your API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
fireworks_api_key = os.getenv("FIREWORKS_API_KEY")

# Print API keys (last 4 characters only for security)
print(f"OpenAI API key: ...{openai_api_key[-4:] if openai_api_key else 'Not set'}")
print(f"Anthropic API key: ...{anthropic_api_key[-4:] if anthropic_api_key else 'Not set'}")
print(f"HuggingFace API key: ...{huggingface_api_key[-4:] if huggingface_api_key else 'Not set'}")
print(f"Fireworks API key: ...{fireworks_api_key[-4:] if fireworks_api_key else 'Not set'}")

# Create LLM instances
openai_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=TEMPERATURE, api_key=openai_api_key, max_tokens=MAX_TOKENS)
anthropic_llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=TEMPERATURE, anthropic_api_key=anthropic_api_key, top_k=TOP_K, top_p=TOP_P, max_tokens=MAX_TOKENS)
hf_llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    temperature=TEMPERATURE,
    huggingfacehub_api_token=huggingface_api_key,
    top_k=TOP_K,
    top_p=TOP_P,
    max_new_tokens=MAX_TOKENS,
    task="text-generation"
)
huggingface_llm = ChatHuggingFace(llm=hf_llm)

fireworks_llm = ChatFireworks(
    model="accounts/fireworks/models/llama-v3p1-70b-instruct",
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)
# Create a PromptTemplate
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Please answer the following question: {question}"
)

# Create chains using the new recommended method
openai_chain = prompt_template | openai_llm | StrOutputParser()
anthropic_chain = prompt_template | anthropic_llm | StrOutputParser()
huggingface_chain = prompt_template | huggingface_llm | StrOutputParser()
fireworks_chain = prompt_template | fireworks_llm | StrOutputParser()
# Define the question
question = "What is an LLM?"

# Run the chains
run_chain(openai_chain, "OpenAI")
run_chain(anthropic_chain, "Anthropic")
run_chain(huggingface_chain, "HuggingFace")
run_chain(fireworks_chain, "Fireworks")