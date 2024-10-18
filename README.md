# LLM Switcher Demo

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Examples](#examples)
7. [Configuration](#configuration)
8. [Limitations](#limitations)
9. [Troubleshooting](#troubleshooting)
10. [FAQ](#faq)
11. [Contributing](#contributing)
12. [License](#license)
13. [Acknowledgments](#acknowledgments)
14. [Contact Information](#contact-information)

## Introduction
The LLM Switcher Demo is a quick demonstration of how to switch between different Large Language Models (LLMs) using LangChain's LCEL (Langchain Expression Language). This project showcases seamless integration and switching between various LLM providers such as OpenAI, Anthropic, HuggingFace, and Fireworks.

## Features
- Seamless switching between multiple LLMs.
- Dynamic parameter adjustment for LLMs using Streamlit UI.
- Example scripts to demonstrate LLM usage and response generation.

## Prerequisites
- Python 3.7 or higher
- API keys for OpenAI, Anthropic, HuggingFace, and Fireworks.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llm-switcher-demo.git
   cd llm-switcher-demo
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Export the necessary API keys as environment variables:
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   export ANTHROPIC_API_KEY='your_anthropic_api_key'
   export HUGGINGFACE_API_KEY='your_huggingface_api_key'
   export FIREWORKS_API_KEY='your_fireworks_api_key'
   ```

## Usage
- To run the Streamlit application:
  ```bash
  streamlit run choosellm.py
  ```

- To execute the command-line demonstration:
  ```bash
  python callall.py
  ```

## Examples
- **Streamlit App**: Use the sidebar to select an LLM and adjust parameters. Enter a question and click "Ask" to see the response.
- **Command-line**: The `callall.py` script runs a predefined question through all LLMs and prints their responses.

## Configuration
- Modify `choosellm.py` and `callall.py` to change default parameters like `TEMPERATURE`, `MAX_TOKENS`, `TOP_K`, and `TOP_P`.
- Update the prompt template in the scripts to customize the question format.

## Limitations
- Requires valid API keys for all LLM providers.
- Limited to the models and parameters supported by the LangChain library.

## Troubleshooting
- Ensure all environment variables are set correctly.
- Verify API keys are valid and have sufficient permissions.
- Check for any network issues that might affect API calls.

## FAQ
**Q: Can I add more LLM providers?**  
A: Yes, you can extend the scripts to include additional LLMs supported by LangChain. Simply add the new LLM to the `create_llm` function in `choosellm.py`. See the LangChain documentation for details on how to add new LLMs: https://python.langchain.com/docs/integrations/chat/

**Q: How do I change the default question?**  
A: Modify the `question` variable in `callall.py` or the default value in the Streamlit text area in `choosellm.py`.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the LangChain team for their powerful library.
- Special thanks to all contributors and users who have provided feedback.

## Contact Information
For questions or support, please contact [skarlekar@yahoo.com](mailto:skarlekar@yahoo.com).