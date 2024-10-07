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
print(df['rating'].value_counts())

# Data Distribution
# Histograms for numerical columns
numerical_columns = ['year', 'score', 'votes', 'budget', 'gross', 'runtime']
df[numerical_columns].hist(bins=30, figsize=(15, 10))
plt.tight_layout()
plt.savefig('histograms.png')  # Save the plot instead of showing it
plt.close()

# Box plots for numerical columns
plt.figure(figsize=(15, 10))
sns.boxplot(data=df[numerical_columns])
plt.savefig('boxplots.png')  # Save the plot instead of showing it
plt.close()

# Bar plots for categorical columns
categorical_columns = ['rating', 'genre', 'director', 'country', 'release_country']
for column in categorical_columns:
    plt.figure(figsize=(15, 10))
    sns.countplot(y=column, data=df, order=df[column].value_counts().index)
    plt.savefig(f'barplot_{column}.png')  # Save the plot instead of showing it
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