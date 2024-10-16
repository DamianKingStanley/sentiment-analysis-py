from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    # sentiment is a float in the range [-1.0, 1.0]
    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return {
        'text': text,
        'sentiment': sentiment_label,
        'polarity': sentiment
    }
