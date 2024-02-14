"""
Colorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '5b53648f75d5c4bb95a07d60be0c70c2'}

# Отправляем запрос для создания покемона
body = {
    "name": "Pokeone",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
if response.status_code == 201:
    pokemon_id = response.json()['id']
    print("Покемон создан:", response.text)
    
    # Отправляем запрос для смены имени, используя id из первого запроса
    body = {
        "pokemon_id": pokemon_id,  # Используем значение pokemon_id из первого запроса
        "name": "Poketwo",
        "photo": "https://dolnikov.ru/pokemons/albums/002.png"
    }
    response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
    print("Покемон переименован:", response.text)

    # Отправляем запрос поймать в покебол, используя id из первого запроса
    body = {
        "pokemon_id": pokemon_id,  # Используем значение pokemon_id из первого запроса
    }
    response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
    print("Покемон пойман в покебол:", response.text)
    
else:
    print("Ошибочка:", response.text)
