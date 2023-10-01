import pandas as pd
import os
import sys
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

def train_model():
    # Charger les données
    df = pd.read_csv('youtube_titles.csv')
    titles = df['Title'].tolist()

    # Prétraitement
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(titles)
    total_words = len(tokenizer.word_index) + 1

    # Créer des séquences d'entrée
    input_sequences = []
    for line in titles:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)

    # Pad sequences 
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre')

    # Créer des prédicteurs et des étiquettes
    X, y = input_sequences[:,:-1], input_sequences[:,-1]
    y_one_hot = np.zeros((len(y), total_words), dtype=np.int8)
    for i, value in enumerate(y):
        y_one_hot[i, value] = 1

    # Créer le modèle
    model = Sequential()
    model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
    model.add(LSTM(150))
    model.add(Dense(total_words, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y_one_hot, epochs=100, verbose=1)
    model.save('mon_modele.h5')

def generate_title(seed_text="Boom Bap", next_words=10):
    model = load_model('mon_modele.h5')
    tokenizer = Tokenizer()
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py [train/generate]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "train":
        train_model()
    elif command == "generate":
        print(generate_title())
    else:
        print("Unknown command. Use 'train' or 'generate'.")
