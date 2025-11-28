import plotly.express as px
import pandas as pd

# Load features
features = pd.read_csv("data/features.csv")

# Scatter map
fig = px.scatter_map(
    features,
    lat='latitude',
    lon='longitude',
    color='temp_winning_prob',
    size='turnout_pct',
    hover_name='Booth_ID',  # match column name exactly
    map_style="carto-positron"  # rename argument to map_style
)

fig.write_html("output/booth_map.html")
print("Booth-level map created!")
