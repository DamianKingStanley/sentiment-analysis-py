from flask import request, jsonify
from app import app, mongo
from app.twitter_service import create_tweet, delete_tweet, get_user_by_username
from app.google_service import get_google_reviews, reply_to_google_review
from app.sentiment_service import analyze_sentiment

@app.route('/api/tweet', methods=['POST'])
def tweet():
    data = request.json
    tweet_text = data.get('text')
    result = create_tweet(tweet_text)
    return jsonify(result)

@app.route('/api/tweet/<int:tweet_id>', methods=['DELETE'])
def remove_tweet(tweet_id):
    result = delete_tweet(tweet_id)
    return jsonify(result)

@app.route('/api/user/<string:username>', methods=['GET'])
def user_lookup(username):
    result = get_user_by_username(username)
    return jsonify(result)




@app.route('/api/google', methods=['GET'])
def google_reviews():
    place_id = request.args.get('place_id')
    reviews = get_google_reviews(place_id)
    return jsonify(reviews)

@app.route('/api/google/reply', methods=['POST'])
def google_reply():
    review_id = request.json.get('review_id')
    reply_text = request.json.get('reply_text')
    result = reply_to_google_review(review_id, reply_text)
    return jsonify(result)

@app.route('/api/sentiment', methods=['POST'])
def sentiment_analysis():
    text = request.json.get('text')
    result = analyze_sentiment(text)
    return jsonify(result)

@app.route('/api/save_review', methods=['POST'])
def save_review():
    review = request.json
    mongo.db.reviews.insert_one(review)
    return jsonify({'message': 'Review saved successfully'})


# @app.route('/api/get_tweets_v2', methods=['GET'])
# def fetch_tweets():
#     keyword = request.args.get('keyword')
#     if not keyword:
#         return jsonify({'error': 'Keyword is required'}), 400
#     try:
#         tweets = get_tweets_v2(keyword)
#         return jsonify(tweets), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/api/reply', methods=['POST'])
# def post_reply():
#     data = request.get_json()
#     tweet_id = data.get('tweet_id')
#     reply_text = data.get('reply_text')
#     if not tweet_id or not reply_text:
#         return jsonify({'error': 'tweet_id and reply_text are required'}), 400
#     try:
#         response = reply_to_tweet(tweet_id, reply_text)
#         return jsonify(response), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
