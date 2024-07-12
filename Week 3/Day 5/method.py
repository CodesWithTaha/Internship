# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity



# df = pd.read_csv('high.csv')

# # Preprocessing function to clean text
# def preprocess_text(text):
#     text = text.lower()  # Convert to lowercase
#     # Additional preprocessing steps (e.g., removing punctuation, stopwords) can be added here
#     return text

# # Combine header and summary
# df['Combined'] = df['Header'] + " " + df['Summary']

# # Preprocess combined and detail columns
# df['Combined'] = df['Combined'].apply(preprocess_text)
# df['Details'] = df['Details'].apply(lambda x: [preprocess_text(p) for p in x.split('\n')])

# # TF-IDF Vectorizer
# vectorizer = TfidfVectorizer()

# important_paragraphs = []

# for i, row in df.iterrows():
#     # Fit TF-IDF on combined text and detail paragraphs
#     tfidf_matrix = vectorizer.fit_transform([row['Combined']] + row['Details'])
    
#     # Calculate cosine similarity between combined text and each paragraph
#     cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
#     # Get the paragraph with the highest similarity score
#     most_important_idx = cosine_similarities.argmax()
#     most_important_paragraph = row['Details'][most_important_idx]
    
#     important_paragraphs.append(most_important_paragraph)

# # Add the most important paragraph to the DataFrame
# df['important_paragraph'] = important_paragraphs

# df.to_csv('nigga.csv', index = False, trincunate = False)
# print(df[['Header', 'Summary', 'important_paragraph']])

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV
df = pd.read_csv('Geo.csv')

# Preprocessing function to clean text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    # Additional preprocessing steps (e.g., removing punctuation, stopwords) can be added here
    return text

# Combine header and summary
df['Combined'] = df['Header'] + " " + df['Summary']

# Preprocess combined and detail columns
df['Combined'] = df['Combined'].apply(preprocess_text)
df['Details'] = df['Details'].apply(lambda x: [preprocess_text(p) for p in x.split('\n')])

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

important_paragraphs = []

for i, row in df.iterrows():
    # Fit TF-IDF on combined text and detail paragraphs
    tfidf_matrix = vectorizer.fit_transform([row['Combined']] + row['Details'])
    
    # Calculate cosine similarity between combined text and each paragraph
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # Get the paragraph with the highest similarity score
    most_important_idx = cosine_similarities.argmax()
    most_important_paragraph = row['Details'][most_important_idx]
    
    important_paragraphs.append(most_important_paragraph)

# Add the most important paragraph to the DataFrame
df['important_paragraph'] = important_paragraphs

# Save the DataFrame to CSV
df.to_csv('important_paragraphs.csv', index=False)
print(df[['Header', 'Summary', 'important_paragraph']])
