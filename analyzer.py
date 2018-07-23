from textblob import TextBlob
import tweepy
import sys
from config import consumer_key, consumer_secret, access_token, access_token_secret
from model import Model
import time
import string

# authenticating with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Twitter user
screen_name = str(sys.argv[1]) if len(sys.argv) > 1 else 'realDonaldTrump'
print('Reading {} ..'.format(screen_name))

# Vectorize words in user timeline
def vectorize(show=True):
    tweets = []

    for n_tweets, tweet in enumerate(tweepy.Cursor(api.user_timeline, screen_name=screen_name).items()):

        if n_tweets > 999:
            break

        # append array of split words in each tweet
        processed = [w.translate(str.maketrans("", "", string.punctuation)) for w in tweet.text.split(' ')]
        cleaned = ([word for word in processed if word.isalpha()])
        tweets.append(cleaned)

    # Vectorize with model
    m = Model()
    print('Fitting model ..')
    m.fit(tweets)
    
    # Show plot of 2d PCA applied to word vectors
    m.plot(n=25) if show else 0

# Analyze sentiment in user timeline
def sentiment():
    tweets = []
    sentiment = 0

    for tweet in enumerate(tweepy.Cursor(api.user_timeline, screen_name=screen_name).items()):
        tweets.append(tweet.text)

        tweet_analysis = TextBlob(tweet.text)
        sentiment += tweet_analysis.sentiment.polarity 
        if tweet_count % 1000 == 0:
            print('Analyzed {} ..'.format(tweet_count))
    
    print('Analyzed a total of: ' + str(tweet_count) + ' tweets.')
    #print('Users overall sentiment: ' + str(sentiment))
    print('Average sentiment per tweet: ' + str(sentiment/len(tweets)))

if __name__ == '__main__':
    #sentiment()
    n_tweets = 0
    vectorize()
