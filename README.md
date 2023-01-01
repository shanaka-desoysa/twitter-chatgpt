# twitter-chatgpt

Twitter bot that generates answers using OpenAI ChatGPT

# How to use

## Local development

1. Create a virtual environment

```bash
python3 -m venv venv
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following variables:

```bash
TWITTER_CONSUMER_KEY=
TWITTER_CONSUMER_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_TOKEN_SECRET=
TWITTER_SEARCH_KEYWORD=
OPENAI_API_KEY=
```

4. Run the bot

```bash
python3 twitter_bot.py
```

## Deploy with Fly.io

```
fly launch (if it's the first time)
# update fly.toml internal port to 3000
fly deploy
# Set your secrets from .env
fly secrets set --app ai1-twitter-chatgpt TWITTER_CONSUMER_KEY= \
  TWITTER_CONSUMER_SECRET= \
  TWITTER_ACCESS_TOKEN= \
  TWITTER_ACCESS_TOKEN_SECRET= \
  TWITTER_SEARCH_KEYWORD=#AI1Chat \
  TWITTER_LAST_REPLIED_TO_ID=1609669651868295168 \
  OPENAI_API_KEY=
```
