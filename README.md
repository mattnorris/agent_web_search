# Install

Install the dependencies.

```sh
poetry install
```

# Configure

[Get a Tavily API key](https://app.tavily.com/home) for the `TAVILY_API_KEY` environment variable.

[Visit your OpenAI settings](https://platform.openai.com/settings) then click _API keys_ to get an OpenAI API key for the `OPENAI_API_KEY` environment variable.

# Run

Run the Streamlit app.

```sh
poetry run streamlit run src/agent_web_search/app/ui.py
```

# Develop

Install pre-commit hooks.

```sh
poetry run pre-commit install
```
