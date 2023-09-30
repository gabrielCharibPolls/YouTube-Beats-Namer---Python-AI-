import csv
import requests
from bs4 import BeautifulSoup

# URL de la recherche YouTube
url = "https://www.youtube.com/results"
params = {
    "search_query": "Free Bombap Beats"
}

# Effectuer la requête HTTP
response = requests.get(url, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser le contenu de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraire les titres des vidéos
    titles = [a.get_text() for a in soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")]
    print('titles')
    # Filtrer les titres commençant par "Free Bombap Beats"
    bombap_titles = [title for title in titles if title.startswith("Free Bombap Beats")]

    # Enregistrer les titres dans un fichier CSV
    with open('bombap_beats_titles.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Titre de la vidéo'])

        for title in bombap_titles:
            csv_writer.writerow([title])

    print("Les titres ont été enregistrés avec succès dans 'bombap_beats_titles.csv'.")
else:
    print("La requête a échoué avec le code :", response.status_code)
