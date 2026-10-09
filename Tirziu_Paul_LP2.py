import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
penguins_df = sns.load_dataset('penguins')
penguins_df.head()

# TODO 1.1
print(penguins_df.shape)

# TODO 1.2
print(penguins_df.dtypes)

# TODO 1.3
print(penguins_df.describe(include='all'))

# TODO 1.4
print(penguins_df['species'].nunique())
print(penguins_df['species'].unique())

# TODO 2.1
print(penguins_df[['species', 'island', 'body_mass_g']])

# TODO 2.2
gentoo_df = penguins_df[penguins_df['species'] == 'Gentoo']
print(gentoo_df)

# TODO 2.3
print(penguins_df.sample(10))

# TODO 3.1
print(penguins_df.isnull().sum())

# TODO 3.2
penguins_clean = penguins_df.dropna()

# TODO 3.3
print(penguins_clean.shape)
print(penguins_df.shape[0] - penguins_clean.shape[0])\

# TODO 4.1
print(penguins_clean.groupby('species')['body_mass_g'].mean())

# TODO 4.2
print(penguins_clean.groupby('species')['flipper_length_mm'].mean().idxmax())

# TODO 4.3
print(penguins_clean['island'].value_counts())

# TODO 4.4
print(penguins_clean['sex'].value_counts(normalize=True) * 100)

# TODO 5.1
sns.countplot(data=penguins_clean, x='species')
plt.show()

# TODO 5.2
sns.barplot(data=penguins_clean, x='species', y='body_mass_g', hue='sex')
plt.show()

# TODO 5.3
sns.relplot(data=penguins_clean, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.show()

# TODO 5.4
sns.catplot(data=penguins_clean, x='species', y='flipper_length_mm', kind='box')
plt.show()

# TODO 5.5
corelatii = penguins_clean.corr(numeric_only=True)
sns.heatmap(corelatii, annot=True)
plt.show()
