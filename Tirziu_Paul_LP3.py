import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

titanic = sns.load_dataset('titanic')
df = titanic[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked', 'deck']].copy()
df.head()

# TODO 1.1 — procentul de valori lipsă pe coloană
procent_lipsa = (df.isnull().mean() * 100).sort_values(ascending=False)
print(procent_lipsa)

# TODO 1.2 — eliminați coloanele cu > 50% valori lipsă
coloane_de_eliminat = procent_lipsa[procent_lipsa > 50].index
df = df.drop(columns=coloane_de_eliminat)
print(df.columns)


# TODO 2.1 — imputare age (mediană) și embarked (mod)
age_inainte = df['age'].copy()
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# TODO 2.2 — verificare + comparație deviație standard
print(df.isnull().sum())
print("Std inainte:", age_inainte.std())
print("Std dupa:", df['age'].std())


# TODO 3.1 — skewness fare
print(df['fare'].skew())

# TODO 3.2 — coloana log_fare + skewness
df['log_fare'] = np.log1p(df['fare'])
print(df['log_fare'].skew())

# TODO 3.3 — două histograme
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].hist(df['fare'], bins=30)
axs[0].set_title('fare')
axs[1].hist(df['log_fare'], bins=30)
axs[1].set_title('log_fare')
plt.show()


# TODO 4.1 — limite IQR + număr de outlieri
Q1 = df['fare'].quantile(0.25)
Q3 = df['fare'].quantile(0.75)
IQR = Q3 - Q1
limita_jos = Q1 - 1.5 * IQR
limita_sus = Q3 + 1.5 * IQR
print(limita_jos, limita_sus)
outlieri = df[(df['fare'] < limita_jos) | (df['fare'] > limita_sus)]
print(len(outlieri))

# TODO 4.2 — fare_capped (clip) + maxim înainte/după
df['fare_capped'] = df['fare'].clip(lower=limita_jos, upper=limita_sus)
print("Max inainte:", df['fare'].max())
print("Max dupa:", df['fare_capped'].max())


# TODO 5.1 — One-Hot Encoding pentru sex și embarked
df = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True, dtype=int)
print(df.head())

# TODO 5.2 — StandardScaler pentru age și fare_capped + verificare medie/std
scaler = StandardScaler()
df[['age', 'fare_capped']] = scaler.fit_transform(df[['age', 'fare_capped']])
print(df[['age', 'fare_capped']].mean())
print(df[['age', 'fare_capped']].std())

# age are putine valori lipsa (circa 20%), deci putem sa le completam cu mediana si sa pastram coloana, care e utila.
# deck are peste 77% valori lipsa, deci ar trebui inventate prea multe date, iar imputarea ar fi nesigura, de aceea am eliminat-o.
