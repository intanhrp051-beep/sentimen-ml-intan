import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

reviews = [
    "produk ini sangat bagus dan memuaskan",
    "saya suka sekali barangnya",
    "kualitasnya buruk dan mengecewakan",
    "produk jelek sekali",
    "lumayan, tidak terlalu bagus atau jelek"
]

labels = [
    "Positif",
    "Positif",
    "Negatif",
    "Negatif",
    "Netral"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)

model = MultinomialNB()
model.fit(X, labels)

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model berhasil dibuat!")
