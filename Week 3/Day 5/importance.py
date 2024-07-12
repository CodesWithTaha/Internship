from sklearn.feature_extraction.text import TfidfVectorizer

# News Headline
prompt = "Karachi to experience partly cloudy skies with chance of light rain"

# News Detail Paragraphs
Documents = ['KARACHI: The Pakistan Meteorological Department (PMD) has forecast partly cloudy skies and strong winds in the port city in next 24 hours.', 'The PMD also said that while partly cloudy conditions are expected to persist today (Thursday), the residents of Karachi may also look forward to light rain or drizzle in the evening or at night.', 'According to the forecast by the Met Office, the maximum temperature is expected to range between 34Â°C to 36Â°C today with a humidity level of 79%.', 'Meanwhile, the minimum temperature in the last 24 hours was recorded at 30.5Â°C.', 'Additionally, the meteorology department also revealed that the sea breezes have returned to the provincial capital of Sindh and are blowing at a gentle pace.', 'For the past few weeks, Karachiites had looked forward to the beginning of monsoon rains in hopes for some respite from the heat spell which has gripped the entire city.', 'But, while the city has\xa0experienced a slight drop in temperatures recently, following heavy showers earlier this week, residents have not yet experienced a significant respite from the heat.', 'Fortunately, there is still hope for the residents and the city as the PMD has predicted heavy rains in the metropolis after July 20.']

# extracting unique words from the prompt by using sets
unique_terms_prompt = list(set(prompt.lower().split()))

# Initialize a TfidfVectorizer object
vectorizer = TfidfVectorizer()

#getting the tf-idf scor
tfidf_matrix = vectorizer.fit_transform(Documents)

# getting the vectoriezed unique words from the docoments
terms = vectorizer.get_feature_names_out()


# converting the scores to array
tfidf_array = tfidf_matrix.toarray()

# determining the importance of the documents for their corresponding scores
importance_scores = []
for doc_idx, doc in enumerate(tfidf_array):
    score = sum(doc[terms.tolist().index(term)] for term in unique_terms_prompt if term in terms)
    importance_scores.append((doc_idx, score))

# Find the document with the highest importance score
most_important_doc_idx = max(importance_scores, key=lambda x: x[1])[0]
most_important_doc = Documents[most_important_doc_idx]

# Print the results
print("Unique Terms from Prompt:\n", unique_terms_prompt)
print("\nImportance Scores for Each Document:")
for doc_idx, score in importance_scores:
    print("Document", doc_idx + 1, " :" , score)

print("\nMost Important Document based on Prompt Terms:")
print(most_important_doc)
