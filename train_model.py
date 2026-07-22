import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('housing.csv')
X = df[['area', 'bedrooms', 'age', 'proximity']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = RandomForestRegressor(n_estimators=100, random_state=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"🎯 R² Score: {r2_score(y_test, y_pred):.3f}")
print(f"📉 RMSE: {mean_squared_error(y_test, y_pred) ** 0.5:.2f}")

joblib.dump(model, 'house_price_model.pkl')
print("✅ Model save ho gaya!")