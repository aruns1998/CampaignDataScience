import pandas as pd
import matplotlib.pyplot as plt

election = pd.read_csv("data/election_history.csv")

# Vote share trend
election.groupby('Year')[['DMK_votes','AIADMK_votes','Others_votes']].sum().plot(kind='line')
plt.title("Vote Share Trend (2006-2021)")
plt.xlabel("Year")
plt.ylabel("Votes")
plt.savefig("output/vote_share_trend.png")
plt.show()
