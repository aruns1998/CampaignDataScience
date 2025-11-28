import pandas as pd

# Load CSV files
election = pd.read_csv("data/election_history.csv")
booths = pd.read_csv("data/booth_level_with_geo.csv")
posts = pd.read_csv("data/sentiment_posts.csv")
features = pd.read_csv("data/features.csv")

print("Data loaded successfully!")
print(election.head())
