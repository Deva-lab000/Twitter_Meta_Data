# Twitter Sentiment & AI Analysis Tool

This project analyzes tweets using sentiment analysis (`TextBlob`) and provides deeper insights using OpenAI's `gpt-3.5-turbo` via LangChain.

## Features

- Fetch tweets from a specified user.
- Analyze sentiment with TextBlob.
- Generate insights using GPT-3.5-turbo through LangChain.
- Integrates Twitter and OpenAI APIs.

## Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/twitter-ai-analyzer.git
    cd twitter-ai-analyzer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your API credentials in `secret.txt` or directly in `main.py`.

4. Run the script:
    ```bash
    python main.py
    ```

## Notes

- Make sure your Twitter developer account is approved and you have elevated access to read tweets.
- You can modify the prompt template to fit specific use cases or tones.

## License

MIT
