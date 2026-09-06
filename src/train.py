# src/train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Nümunə məlumatlar
data = {'amount': [100, 5000, 200, 7000, 150, 8000], 'time': [1, 23, 2, 22, 1, 21], 'fraud': [0, 1, 0, 1, 0, 1]}
df = pd.DataFrame(data)

X = df[['amount', 'time']]
y = df['fraud']

model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
model.fit(X, y)

# Modeli saxla
joblib.dump(model, 'model.pkl')
print("Model 'model.pkl' olaraq saxlandı.")
