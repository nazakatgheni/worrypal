import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os
# pandas: Used to structure and store our data
# TfidfVectorizer: Turns text into numerical features
# LogisticRegression: Our ML model (a simple, fast classifier)
# joblib: Saves and loads large objects like models
# os: For creating directories like model/

# Example labeled data
data = {
    "text": [
        "What if they misunderstood my email?",
        "I think I'm okay with that decision.",
        "I can't stop thinking about what I said.",
        "I'm fine. It's not a big deal.",
        "Am I annoying them? Should I text again?",
        "All good, I've let it go.",
        "This is driving me insane. I can't sleep.",
        "It's probably nothing.",
        "What if they hate me now?",
        "I did my best, that's enough.",
        "Am i being extra?",
        "Does my boss hates me?",
        "Is he cheating?",
        "I keep checking my phone for their reply.",
        "Maybe I should apologize again?",
        "I'm overthinking this situation.",
        "They haven't responded in hours.",
        "I feel like I messed up.",
        "Should I double text?",
        "I can't focus on anything else.",
        "Maybe I'm being too sensitive.",
        "I need to stop obsessing over this.",
        "They probably don't even care.",
        "I should just let it go.",
        "This is consuming my thoughts."
    ],
    "label": [
        "Godd, stop think too much",
        "Chill, you good",
        "Drop the phone and go for a walk or something",
        "Chill, you good",
        "Godd, stop think too much",
        "Chill, you good",
        "Drop the phone and go for a walk or something",
        "Chill, you good",
        "Drop the phone and go for a walk or something",
        "Chill, you good",
        "Drop the phone and go for a walk or something",
        "Godd, stop think too much",
        "Drop the phone and go for a walk or something",
        "Godd, stop think too much",
        "Godd, stop think too much",
        "Godd, stop think too much",
        "Drop the phone and go for a walk or something",
        "Godd, stop think too much",
        "Godd, stop think too much",
        "Drop the phone and go for a walk or something",
        "Chill, you good",
        "Drop the phone and go for a walk or something",
        "Godd, stop think too much",
        "Chill, you good",
        "Drop the phone and go for a walk or something"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Data validation
print(f"Total examples: {len(df)}")
print(f"Unique labels: {df['label'].unique()}")
print(f"Label distribution:\n{df['label'].value_counts()}")

# Basic text preprocessing
df['text'] = df['text'].str.lower()  # Convert to lowercase
df['text'] = df['text'].str.strip()  # Remove leading/trailing whitespace

# TF-IDF Vectorization with improved parameters
vectorizer = TfidfVectorizer(
    max_features=1000,  # Limit vocabulary size
    min_df=2,          # Ignore terms that appear in less than 2 documents
    max_df=0.95,       # Ignore terms that appear in more than 95% of documents
    ngram_range=(1, 2) # Use both unigrams and bigrams
)
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train Logistic Regression model with improved parameters
model = LogisticRegression(
    C=1.0,              # Regularization strength
    max_iter=1000,      # Maximum iterations
    class_weight='balanced'  # Handle class imbalance
)
model.fit(X, y)

# Evaluate model performance
from sklearn.metrics import classification_report
y_pred = model.predict(X)
print("\nModel Performance:")
print(classification_report(y, y_pred))

# Save model and vectorizer
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model and vectorizer saved.")
