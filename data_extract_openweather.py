import requests 
import pandas as pd 
import json
from datetime import datetime

API_key = ''

start = 1617223200  # Timestamp de début
end = 1617309600    # Timestamp de fin
lat = 37.7749       # Latitude (San Francisco)
lon = -122.4194     # Longitude (San Francisco)

def data_extract_openweather(start, end, lat, lon, API_key):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API_key}'
    
    r = requests.get(url)
    
    if r.status_code == 200:  # Vérifier si la requête a réussi
        data = r.json()
        
        if 'list' in data:
            df = pd.DataFrame(data['list'])
            df.to_csv('data.csv', index=False)  # Sauvegarde des données en CSV
            print('Data saved to data.csv')
        else:
            print("Aucune donnée trouvée.")
    else:
        print(f"Erreur {r.status_code}: {r.text}")

# Exécuter la fonction
if __name__ == "__main__":
    data_extract_openweather(start, end, lat, lon, API_key)
