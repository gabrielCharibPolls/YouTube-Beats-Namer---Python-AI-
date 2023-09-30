import requests
from bs4 import BeautifulSoup

# URL de la recherche YouTube
url = "https://www.youtube.com/results"
params = {
    "search_query": "Free Bombap Beats",
    "sp": "EgIQAQ%253D%253D"  # Cette chaîne de requête filtre les vidéos par pertinence.
}

# Effectuer la requête HTTP
response = requests.get(url, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser le contenu de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraire les titres des vidéos
    titles = [a.text for a in soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")]
    
    # Filtrer les titres commençant par "Free Bombap Beats"
    bombap_titles = [title for title in titles if title.startswith("Free Bombap Beats")]

    # Afficher les titres
    for title in bombap_titles:
        print(title)
else:
    print("La requête a échoué avec le code :", response.status_code)
