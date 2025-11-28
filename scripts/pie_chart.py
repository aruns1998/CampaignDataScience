import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('output', exist_ok=True)

election = pd.read_csv('data/election_history.csv')

# Pie chart for 2021 winner vote share
latest = election[election['Year'] == 2021]
labels = latest['Party']
sizes = latest['Vote_Share']

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Vote Share 2021')
plt.savefig('output/vote_share_2021.png')
plt.close()

print("Pie chart generated!")
