import numpy as np
import pandas as pd

np.random.seed(42)
n = 1000

area = np.random.randint(50, 300, n)
bedrooms = np.random.randint(1, 6, n)
age = np.random.randint(0, 50, n)
proximity = np.random.uniform(1, 10, n)

price = (2000 * area + 5000 * bedrooms - 1000 * age - 5000 * proximity + np.random.normal(0, 20000, n)).astype(int)
price = np.maximum(price, 30000)

df = pd.DataFrame({'area': area, 'bedrooms': bedrooms, 'age': age, 'proximity': proximity, 'price': price})
df.to_csv('housing.csv', index=False)

print("✅ housing.csv ban gayi!")