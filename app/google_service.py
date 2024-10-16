import requests
from app.config import Config

def get_google_reviews(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={Config.GOOGLE_API_KEY}"
    response = requests.get(url)
    reviews = response.json().get('result', {}).get('reviews', [])
    return [{'author_name': review['author_name'], 'text': review['text']} for review in reviews]

def reply_to_google_review(review_id, reply_text):
    # Google Places API does not support direct replies to reviews.
    # This functionality might need manual intervention or a different approach.
    return {'message': 'Replying to Google reviews is not supported through this API'}
