import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

features = pd.read_csv("data/features.csv")

X = features[['turnout_pct','dmk_strength','aiadmk_strength','others_strength',
              'avg_sentiment_score','engagement_score','urban_rural_index','sc_population_pct','youth_pct']]
y = features['temp_winning_prob']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBRegressor(n_estimators=100, max_depth=5)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, preds))

# Feature importance
plt.barh(X.columns, model.feature_importances_)
plt.title("Feature Importance")
plt.savefig("output/feature_importance.png")
plt.show()
