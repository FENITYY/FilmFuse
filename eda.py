import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the backend for Matplotlib
plt.switch_backend('Agg')

# Load the preprocessed dataset
df = pd.read_csv('movies_cleaned.csv')

# Summary Statistics
print(df.describe())
print(df['genre'].value_counts())
print(df['release_country'].value_counts())

# Data Distribution
# Histograms for numerical columns
df.hist(bins=30, figsize=(15, 10))
plt.tight_layout()
plt.savefig('histograms.png')  # Save the plot instead of showing it
plt.close()

# Box plots for numerical columns
plt.figure(figsize=(15, 10))
sns.boxplot(data=df[['budget', 'gross', 'runtime', 'score', 'votes']])
plt.savefig('boxplots.png')  # Save the plot instead of showing it
plt.close()

# Bar plots for categorical columns
plt.figure(figsize=(15, 10))
sns.countplot(y='genre', data=df, order=df['genre'].value_counts().index)
plt.savefig('barplots.png')  # Save the plot instead of showing it
plt.close()

# Correlation Analysis
# Select only numeric columns for correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Correlation matrix
corr_matrix = numeric_df.corr()
print(corr_matrix)

# Heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.savefig('heatmap.png')  # Save the plot instead of showing it
plt.close()