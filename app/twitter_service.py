# app/twitter_utils.py
import tweepy
from tweepy import TweepyException
from app.config import Config
from app import mongo
import requests
from flask_cors import CORS


def get_api():
    auth = tweepy.OAuthHandler(Config.TWITTER_API_KEY, Config.TWITTER_API_SECRET)
    auth.set_access_token(Config.TWITTER_ACCESS_TOKEN, Config.TWITTER_ACCESS_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True)


def create_tweet(tweet_text):
    try:
        api = get_api()
        tweet = api.update_status(status=tweet_text)
        return {'id': tweet.id, 'text': tweet.full_text, 'user': tweet.user.screen_name}
    except tweepy.TweepyException as e:
        print(f"Tweepy Error: {e}")
        raise
    except Exception as e:
        print(f"General Error: {e}")
        raise

def delete_tweet(tweet_id):
    try:
        api = get_api()
        api.destroy_status(tweet_id)
        return {'message': 'Tweet deleted successfully'}
    except tweepy.TweepyException as e:
        print(f"Tweepy Error: {e}")
        raise
    except Exception as e:
        print(f"General Error: {e}")
        raise
def get_user_by_username(username):
    try:
        api = get_api()
        user = api.get_user(screen_name=username)
        user_info = {
            'id': user.id,
            'name': user.name,
            'username': user.screen_name,
            'followers_count': user.followers_count,
            'profile_image_url': user.profile_image_url_https
        }
        return user_info
    except tweepy.TweepyException as e:
        print(f"Tweepy Error: {e}")
        raise
    except Exception as e:
        print(f"General Error: {e}")
        raise

# def get_tweets_v2(keyword):
#     url = f"https://api.twitter.com/2/tweets/search/recent?query={keyword}"
#     headers = {"Authorization": f"Bearer {Config.TWITTER_BEARER_TOKEN}"}
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         tweets = response.json().get("data", [])
#         tweets_list = [{'text': tweet['text'], 'user': tweet['author_id']} for tweet in tweets]
        
#         if tweets_list:
#             mongo.db.tweets.insert_many(tweets_list)
        
#         return tweets_list
#     else:
#         print(f"Error: {response.status_code} - {response.text}")
#         return []

# def reply_to_tweet(tweet_id, reply_text):
#     try:
#         api = get_api()
#         api.update_status(status=reply_text, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
#         return {'message': 'Reply posted successfully'}
#     except tweepy.TweepyException as e:
#         print(f"Tweepy Error: {e}")
#         raise
#     except Exception as e:
#         print(f"General Error: {e}")
#         raise



# def get_tweets(keyword):
#     try:
#         api = get_api()
#         # Use the updated search method
#         tweets = api.search_tweets(q=keyword, count=10, tweet_mode='extended')
#         tweets_list = [{'text': tweet.full_text, 'user': tweet.user.screen_name} for tweet in tweets]
        
#         if tweets_list:
#             mongo.db.tweets.insert_many(tweets_list)
        
#         return tweets_list
#     except tweepy.TweepyException as e:
#         print(f"Tweepy Error: {e}")
#         raise
#     except Exception as e:
#         print(f"General Error: {e}")
#         raise