import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer
import random

# Chargement du modèle spaCy
nlp = spacy.load("en_core_web_sm")

# Fonction pour analyser les titres et extraire des n-grams significatifs
def extract_significant_ngrams(titles, n=2):
    vectorizer = CountVectorizer(ngram_range=(n, n), stop_words='english').fit(titles)
    ngrams = vectorizer.get_feature_names_out()
    return ngrams

# Fonction pour générer un titre en utilisant des n-grams
def generate_title_with_ngrams(ngrams, producer_name="Your Name", artist_name="Joey Bada$$"):
    # Sélection aléatoire de n-grams
    selected_ngram = random.choice(ngrams)
    year = "2023"
    style = "Boom Bap"
    # Construction du titre
    new_title = f"{artist_name} x \"{selected_ngram.title()}\" {style} Beat {year} | Prod. by {producer_name}"
    return new_title

# Fonction principale
def main(csv_file):
    df = pd.read_csv(csv_file)
    titles = df['Title'].tolist()
    
    # Extraction des n-grams significatifs des titres
    ngrams = extract_significant_ngrams(titles, n=2)  # Vous pouvez ajuster n pour tester différents n-grams
    
    # Génération d'un nouveau titre basé sur les n-grams
    producer_name = "DJ Analytic"
    new_title = generate_title_with_ngrams(ngrams, producer_name)
    print("Nouveau titre généré:", new_title)

if __name__ == "__main__":
    main('youtube_titles.csv')
