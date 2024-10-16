import praw
from app.config import Config

reddit = praw.Reddit(client_id=Config.REDDIT_CLIENT_ID,
                     client_secret=Config.REDDIT_SECRET,
                     user_agent='your_user_agent')

def get_reddit_comments(subreddit):
    comments = reddit.subreddit(subreddit).comments(limit=10)
    return [{'id': comment.id, 'text': comment.body} for comment in comments]

def reply_to_reddit_comment(comment_id, reply_text):
    comment = reddit.comment(comment_id)
    comment.reply(reply_text)
    return {'status': 'success'}
