import requests
from app.config import Config

def get_facebook_comments(post_id):
    url = f'https://graph.facebook.com/{post_id}/comments'
    params = {'access_token': Config.FACEBOOK_ACCESS_TOKEN}
    response = requests.get(url, params=params)
    comments = response.json().get('data', [])
    return [{'id': comment['id'], 'text': comment['message']} for comment in comments]

def reply_to_facebook_comment(comment_id, reply_text):
    url = f'https://graph.facebook.com/{comment_id}/comments'
    params = {
        'access_token': Config.FACEBOOK_ACCESS_TOKEN,
        'message': reply_text
    }
    response = requests.post(url, params=params)
    return {'status': 'success' if response.ok else 'failed'}
