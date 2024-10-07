import pandas as pd

# Load the dataset
df = pd.read_csv('movies.csv')

# Preprocess each attribute

# name: Fill missing values with 'Unknown'
df['name'] = df['name'].fillna('Unknown')

# rating: Fill missing values with 'Unknown'
df['rating'] = df['rating'].fillna('Unknown')

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

# budget: Convert to numeric and fill missing values with the mean
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['budget'] = df['budget'].fillna(df['budget'].mean())

# gross: Convert to numeric and fill missing values with the mean
df['gross'] = pd.to_numeric(df['gross'], errors='coerce')
df['gross'] = df['gross'].fillna(df['gross'].mean())

# company: Fill missing values with 'Unknown'
df['company'] = df['company'].fillna('Unknown')

# runtime: Fill missing values with the mean
df['runtime'] = df['runtime'].fillna(df['runtime'].mean())

# Save the preprocessed dataset
df.to_csv('movies_cleaned.csv', index=False)