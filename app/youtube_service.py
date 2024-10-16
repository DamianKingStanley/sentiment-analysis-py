from googleapiclient.discovery import build
from app.config import Config

service = build('youtube', 'v3', developerKey=Config.YOUTUBE_API_KEY)

def get_youtube_comments(video_id):
    request = service.commentThreads().list(part='snippet', videoId=video_id)
    response = request.execute()
    comments = response.get('items', [])
    return [{'id': comment['id'], 'text': comment['snippet']['topLevelComment']['snippet']['textDisplay']} for comment in comments]

def reply_to_youtube_comment(comment_id, reply_text):
    # YouTube API does not support replying to comments
    return {'status': 'not supported'}
