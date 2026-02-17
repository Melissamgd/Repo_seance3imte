import requests

# URL de l'API pour obtenir une citation aléatoire
url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"

try:
    response = requests.get(url)
    response.raise_for_status()  # Vérifie s'il y a une erreur HTTP
    
    data = response.json()
    
    print("Citation aléatoire de Donald Trump :")
    print(f'"{data["message"]}"')

except requests.exceptions.RequestException as e:
    print("Erreur lors de l'appel à l'API :", e)
