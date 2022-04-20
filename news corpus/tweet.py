import pandas as pd
import tweepy
from tweepy import OAuthHandler




    ################# Twitter API Connection #######################
    
consumer_key = "kvSRXawYtSh32pknAZh7NRAFv"
consumer_secret = "yEWEEnR5wqWUxUUUDT03N3uIpfDbdN5kgNOqXXQinWrqo2os2o"
access_token = "3104698248-9cv98abLhM1GTSQFZNGTdpYDgjqpra8JY7XxWca"
access_token_secret = "6na5TRSSNIck1smYecrygwSZBosbCW6yxkFxmHSyIvrEw"

auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
auth.set_access_token( access_token , access_token_secret )
api = tweepy.API(auth)
    ################################################################

    
def get_tweets(Topic,Count):
            i=0
            df = pd.DataFrame(columns=["User","Tweet"])
            for tweet in tweepy.Cursor(api.search_tweets, q=Topic,count=50, lang="en",exclude='retweets').items():
                df.loc[i,"User"] = tweet.user.name
                df.loc[i,"Tweet"] = tweet.text
                i=i+1
                if i>Count:
                    break
                else:
                    pass
            return df

df = get_tweets("North Korea",20)
df.to_csv("tweets.csv")
