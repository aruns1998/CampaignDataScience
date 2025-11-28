import pandas as pd
from textblob import TextBlob

posts = pd.read_csv("data/sentiment_posts.csv")

# Sentiment score
posts['sentiment_score'] = posts['post_text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Aggregate by booth
sentiment_summary = posts.groupby('booth_id')['sentiment_score'].mean().reset_index()
sentiment_summary.to_csv("output/sentiment_summary.csv", index=False)
print("Sentiment analysis complete!")
