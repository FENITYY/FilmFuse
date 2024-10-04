import pandas as pd

# Load the dataset
df = pd.read_csv('movies.csv')

# Inspect the dataset
print(df.info())
print(df.describe())

# Preprocess each attribute

# name: Fill missing values with 'Unknown'
df['name'] = df['name'].fillna('Unknown')

# rating: Convert to numeric, fill missing values with the mean, and normalize
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['rating'] = (df['rating'] - df['rating'].mean()) / df['rating'].std()

# genre: Fill missing values with 'Unknown'
df['genre'] = df['genre'].fillna('Unknown')

# year: Ensure it's an integer
df['year'] = df['year'].astype(int)

# released: Extract date and country, convert date to datetime
df[['release_date', 'release_country']] = df['released'].str.extract(r'([A-Za-z]+\s\d{1,2},\s\d{4})\s\((.*)\)')
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['release_country'] = df['release_country'].fillna('Unknown')

# score: Fill missing values with the mean
df['score'] = df['score'].fillna(df['score'].mean())

# votes: Fill missing values with the mean
df['votes'] = df['votes'].fillna(df['votes'].mean())

# director: Fill missing values with 'Unknown'
df['director'] = df['director'].fillna('Unknown')

# writer: Fill missing values with 'Unknown'
df['writer'] = df['writer'].fillna('Unknown')

# star: Fill missing values with 'Unknown'
df['star'] = df['star'].fillna('Unknown')

# country: Fill missing values with 'Unknown'
df['country'] = df['country'].fillna('Unknown')

# budget: Fill missing values with the mean
df['budget'] = df['budget'].fillna(df['budget'].mean())

# gross: Fill missing values with the mean
df['gross'] = df['gross'].fillna(df['gross'].mean())

# company: Fill missing values with 'Unknown'
df['company'] = df['company'].fillna('Unknown')

# runtime: Fill missing values with the mean
df['runtime'] = df['runtime'].fillna(df['runtime'].mean())

# Remove duplicates
df = df.drop_duplicates()

# Handle outliers (example: removing rows where 'budget' is more than 3 standard deviations from the mean)
budget_mean = df['budget'].mean()
budget_std = df['budget'].std()
df = df[(df['budget'] >= budget_mean - 3 * budget_std) & (df['budget'] <= budget_mean + 3 * budget_std)]

# Standardize text data (example: converting 'name' and 'genre' to lowercase)
df['name'] = df['name'].str.lower()
df['genre'] = df['genre'].str.lower()

# Correct data types (example: ensuring 'year' is an integer)
df['year'] = df['year'].astype(int)

# Handle inconsistent data (example: removing special characters from 'company')
df['company'] = df['company'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)

# Save the cleaned dataset
df.to_csv('movies_cleaned.csv', index=False)