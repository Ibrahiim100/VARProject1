import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(paragraph):
   
    nltk.download('vader_lexicon')
    
    
    sid = SentimentIntensityAnalyzer()

    # sentiment analysis
    sentiment_score = sid.polarity_scores(paragraph)

    # Classify sentiment
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

