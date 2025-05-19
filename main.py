import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from textblob import TextBlob
import tweepy
import os

# Twitter API Setup (Replace with your credentials or use secret.txt)
TWITTER_API_KEY = "YOUR_API_KEY"
TWITTER_API_SECRET = "YOUR_API_SECRET"
TWITTER_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
TWITTER_ACCESS_SECRET = "YOUR_ACCESS_SECRET"

auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)
twitter_api = tweepy.API(auth)

# OpenAI API Key (Replace with your key or use secret.txt)
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")

prompt_template = PromptTemplate(
    input_variables=["tweet", "name", "designation"],
    template="""
    Analyze this tweet: "{tweet}".
    Assume it's from a person named {name} who is a {designation}.
    Provide insights about tone, intent, and sentiment.
    """
)

chain = LLMChain(llm=llm, prompt=prompt_template)

def analyze_tweets(username, count=10):
    tweets = twitter_api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
    for tweet in tweets:
        text = tweet.full_text
        sentiment = TextBlob(text).sentiment
        print(f"\nTweet: {text}")
        print(f"Sentiment: Polarity={sentiment.polarity}, Subjectivity={sentiment.subjectivity}")
        result = chain.run(tweet=text, name="John Doe", designation="Analyst")
        print("AI Analysis:", result)

# Example
if __name__ == "__main__":
    analyze_tweets("elonmusk", count=3)
