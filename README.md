# OpenAI Twitter Chat Bot

Twitter bot that generates answers using OpenAI ChatGPT and DALL-E-2.

Read more about it here: https://betterprogramming.pub/creating-a-twitter-chatbot-with-openai-chatgpt-and-dall-e-2-d6bbf2d0230b

# Development

Create a `.env` file with the following variables:

```bash
TWITTER_CONSUMER_KEY=
TWITTER_CONSUMER_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_TOKEN_SECRET=
TWITTER_SEARCH_KEYWORD=#MyChatGPT
TWITTER_SEARCH_IMAGE_KEYWORD=#MyDALLE2
TWITTER_LAST_REPLIED_TO_ID=
OPENAI_API_KEY=
```

## Local Development with Docker and Docker Compose

1. Run the bot with docker-compose

```bash
docker-compose up
```

## Local Development with Virtual Environment

1. Create a virtual environment

```bash
python3 -m venv venv
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the bot

```bash
python3 twitter_bot.py
```

# Deploy Free with Fly.io

## Fly Launch

If it's the first time.

```bash
fly launch
```

Then update fly.toml and remove [[services]] section.

## Fly Deploy

```bash
fly deploy
```

## Set your secrets from .env

```bash
fly secrets set --app ai1-twitter-chatgpt TWITTER_CONSUMER_KEY= \
 TWITTER_CONSUMER_SECRET= \
 TWITTER_ACCESS_TOKEN= \
 TWITTER_ACCESS_TOKEN_SECRET= \
 TWITTER_SEARCH_KEYWORD=#AI1Chat \
 TWITTER_SEARCH_IMAGE_KEYWORD=#AI1Image \
 TWITTER_LAST_REPLIED_TO_ID=1609669651868295168 \
 OPENAI_API_KEY=

```
