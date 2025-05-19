import os
import telegram
import tweepy

# Telegram Bot token
TELEGRAM_TOKEN = '6998662602:AAFMmKfp8Cg4bwCOnBC7CVs-o2Zd-2Ac8c4'

# Twitter API credentials
TWITTER_API_KEY = 'YOUR_TWITTER_API_KEY'
TWITTER_API_SECRET = 'YOUR_TWITTER_API_SECRET'
TWITTER_ACCESS_TOKEN = 'YOUR_TWITTER_ACCESS_TOKEN'
TWITTER_ACCESS_TOKEN_SECRET = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

# Initialize Telegram Bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token_key=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Function to post a message to Twitter
def post_to_twitter(message):
    api.update_status(message)


# Get channel messages
channel_id = '@channel_id'  # Replace with your channel ID
messages = bot.get_chat_history(chat_id=channel_id,
                                limit=10)  # Adjust limit as needed

# Post each message to Twitter
for message in messages:
    post_to_twitter(message.text)
