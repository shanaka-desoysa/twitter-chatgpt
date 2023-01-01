import tweepy
import logging
import os
import time
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv(".env")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

logger.info("Starting Twitter bot")

# Read Twitter API credentials from environment variables
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
keyword = os.environ.get("TWITTER_SEARCH_KEYWORD", "#AI1Chat")
last_replied_to_id = os.environ.get(
    "TWITTER_LAST_REPLIED_TO_ID", 1609669651868295168)

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up Twitter API authentication
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
api = tweepy.API(auth)

# Set the keyword you want to search for
keyword = keyword.lower()


while True:
    # Search for tweets containing the keyword
    tweets = api.search_tweets(q=keyword)

    logger.info(f"Found {len(tweets)} tweets")

    # Respond to each tweet
    for tweet in tweets:
        username = tweet.user.screen_name
        status_id = tweet.id
        # Check if this tweet has already been replied to
        if tweet.id > last_replied_to_id:
            # Get the text of the tweet
            tweet_text = tweet.text
            # Remove the keyword from the tweet text
            # tweet_text = tweet_text.replace(keyword, "")

            # print the username, tweet and status_id
            logger.info(f"username: {username}, tweet: {tweet_text}")
            # Use the OpenAI chat API to generate a response to the tweet
            tweet_text = f"please answer  following question and keep the response less than 270 characters. {tweet_text}"
            logger.info(f"OpenAI prompt: {tweet_text}")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=tweet_text,
                temperature=0.7,
                max_tokens=128,
            )
            response_text = response["choices"][0]["text"]
            logger.info(
                f"OpenAI response_text: {response_text}, length: {len(response_text)}")

            # Reply to the tweet with the generated response
            username = tweet.user.screen_name
            status_id = tweet.id

            try:
                api.update_status(
                    f"@{username} {response_text}",
                    in_reply_to_status_id=status_id
                )
            except tweepy.error.TweepError as e:
                logger.info(f"Error: {e}")
                response_text = "I'm sorry, I'm not sure how to answer that. Please ask me something else."

            logger.info(f"Replied to tweet {status_id}")
            # Update the ID of the last replied-to tweet
            last_replied_to_id = tweet.id

            # Write the ID of the last replied-to tweet to environment variable
            os.environ["TWITTER_LAST_REPLIED_TO_ID"] = str(last_replied_to_id)

    logger.info(f"Sleeping for 10 seconds")
    time.sleep(10)
