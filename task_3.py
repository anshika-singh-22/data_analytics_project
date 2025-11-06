import nltk
# You only need to run the following line once to download the lexicon:
# nltk.download('vader_lexicon') 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 1. Initialize the VADER analyzer
sia = SentimentIntensityAnalyzer()

# 2. Define a set of texts (our "Amazon reviews, social media, and news sites")
public_opinion = [
    "The new product is absolutely incredible and revolutionary. Highly recommended!", # Strongly Positive
    "I've seen better. It's just okay, nothing special.", # Neutral/Slightly Negative
    "This is the worst customer service experience I have ever had. Truly awful.", # Strongly Negative
    "A major announcement was made today regarding the economy.", # Neutral News
]

print("--- Sentiment Analysis using VADER ---")

# 3. Apply analysis on data sources
for text in public_opinion:
    # Get the sentiment scores
    scores = sia.polarity_scores(text)
    
    # Classify the sentiment based on the 'compound' score
    # Compound score is a normalized, weighted composite score:
    if scores['compound'] >= 0.05:
        sentiment = 'POSITIVE 😊'
    elif scores['compound'] <= -0.05:
        sentiment = 'NEGATIVE 😡'
    else:
        sentiment = 'NEUTRAL 😐'

    print(f"\nText: \"{text}\"")
    print(f"Classification: **{sentiment}**")
    print(f"VADER Scores (Compound): {scores['compound']:.4f}")