from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample documents
documents = [
    "I love programming.",
    "Programming is fun.",
    "I love fun!"
]

# Create a bag-of-words model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Display the feature names and the BoW representation
print("Feature Names:", vectorizer.get_feature_names_out())
print("Bag of Words Representation:\n", X.toarray())