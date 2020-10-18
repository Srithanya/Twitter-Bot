import tweepy
import time

print("This is a twitter bot")
# Authenticate to Twitter
auth = tweepy.OAuthHandler("wnlVXSxMKtWI9Ibxc5yQ920GW", 
    "UBxuiNZVFIEQVucsC8G9AUoSVu7O1PKYUomrSUXTb6I5otik3k")
auth.set_access_token("1286155990837018625-0BgdTgO3UaXw6lyRoa3t8ThdK6NED1", 
    "S0mHkjAQD2JP76uIb0IkHxSt3UmpgmiaOL7tOr37s9g2K")

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()
print(f"My user name is {user.screen_name}")

#code for liking the post based on hashtag
hashtag=input("give any hashtag to like that post:")
num=int(input("enter how many you want to like with that hashtag:"))
for tweet in tweepy.Cursor(api.search, q=hashtag, rpp=100).items(num):
    try:
        print(f"Liking tweet {tweet.id} with {hashtag}")
        tweet.favorite()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

#code for liking the post based on username
User=input("enter a username:")
nrTweets=int(input("enter how many you want to like with that username:"))
for tweet in tweepy.Cursor(api.search, User).items(nrTweets):
    try:
        print(f"Liking tweet {tweet.id}")
        tweet.favorite()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


