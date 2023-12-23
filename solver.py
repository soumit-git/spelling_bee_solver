import pandas as pd

df = pd.read_csv('words_alpha.csv', names=['word'])

letters = {'h', 'o', 'm', 'e', 's', 'a', 'g'}

# Drop rows with missing values in the 'word' column
df = df.dropna(subset=['word'])

# Convert each word in the 'word' column to a set and check if it is a subset of the given set of letters
filtered_list = df[df['word'].apply(lambda x: set(x)).apply(lambda x: x.issubset(letters)) & 
                   (df['word'].str.len() >= 4) & 
                   (df['word'].str.contains('g'))]
print(filtered_list.to_string())