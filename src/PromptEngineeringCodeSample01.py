import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)
print(df.head())
print(df.columns)
t_col = 'Type 1'
df['is_w'] = df[t_col].apply(lambda x: 1 if x == 'Water' else 0)
df = df.dropna(subset=['Attack', 'Defense', 'Speed', 'HP'])
ftrs = ['Attack', 'Defense', 'Speed', 'HP']
X = df[ftrs]
y = df['is_w']
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
sns.countplot(x='is_w', data=df)
plt.title("Dist of Water vs. Non-Water")
plt.show()
sc = StandardScaler()
X_tr_s = sc.fit_transform(X_tr)
mdl = LogisticRegression(max_iter=1000)
mdl.fit(X_tr_s, y_tr)
X_te_s = sc.transform(X_te)
preds = mdl.predict(X_te_s)
print(classification_report(y_te, preds))
print(confusion_matrix(y_te, preds))
samp = X.sample(1, random_state=random.randint(0, 100))
samp_s = sc.transform(samp)
pred = mdl.predict(samp_s)
print(f"Prediction: {'Water' if pred[0] == 1 else 'Non-Water'}, Actual: {'Water' if df.loc[samp.index, 'is_w'].values[0] == 1 else 'Non-Water'}")