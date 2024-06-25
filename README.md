# ai-podcast-generator


## Installation

Requirements:
- Python 3.11
- Poetry (https://python-poetry.org/docs/)

It is recommended to use a virtual environment:

Linux/MacOS:
```bash 
python -m venv .venv
source .venv/bin/activate
```

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

To install the project, run the following command:

```bash
poetry install
```

For development, we recommend to also install the pre-commit hooks by running the following command:

```bash
pre-commit install
```

Required environment variables:

```bash
export AI_PODCAST_GENERATOR_OPEN_AI__API_KEY="your-api-key"
```

## Next Steps for PoC
- [x] Search very basic test data, e.g. paper, blog & extract to pdf
- [ ] Create function to get summaries for the test data using an OpenAI API
- [ ] Setup BaseClass
- [ ] Setup pydantic config
- [ ] Create SubClass for fixed contents
- [ ] Create first easy prompt template to create podcast script
- [ ] Integrate TTS-API of OpenAI


## Flow of the program
1. Save raw information, including multi-media
2. Create a summary for each new information (also incl. author, etc.), if word count >= 400 words
3. Use summaries & previous episodes to create a new podcast episode using a prompt template
4. Use TTS in order to create the *.mp3


## Requirements (sorted by priority)
- Sources: RSS, Medium, Paper, Twitter, Reddit, YouTube, etc.
- Create summaries for each information from each source, if word count >= 400 words
- Prompt template to create a podcast script
- Generate audio based on the script using a Text-to-speech (TTS) engine (start with OpenAI, not abstracted)
- Later: podcast script for 2 moderators
- Language should be configurable
- Sources, links & topics should be configurable based on the source
- Config for API keys should be local
- Later: Create a medium blog with sources for each podcast episode
