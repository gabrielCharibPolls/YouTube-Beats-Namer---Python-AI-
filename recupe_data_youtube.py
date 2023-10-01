import requests
import re
import csv

url = "https://www.youtube.com/results"
params = {
    "search_query": "Free Bombap Beats"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    content = response.text
    #################################################################
    # Utiliser des expressions régulières pour extraire les informations
    titles = re.findall(r'\"text\":\"(\(FREE\) .*?)\"', content)


    with open('youtube_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Video Number", "Title", "URL", "Video ID"])  # Écrire les en-têtes

        for i in range(min(50, len(titles))):
            title = titles[i]
            print(f"Video {i+1}:")
            print("Titre:", title)
            print("-" * 50)

            # Écrire les données dans le fichier CSV
            writer.writerow([i+1, title])

else:
    print("La requête a échoué avec le code :", response.status_code)
