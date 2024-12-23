import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = 'value'
Header = {'Content-Type' :'application/json', 'trainer_token': Token
          }
body_createpokemon = {
    "name": "string",
    "photo_id": 1
}
body_changename = {
    "pokemon_id": "string",
    "name": "New Name",
    "photo_id": 1
}
body_catchpokemon = {
    "pokemon_id": "string"
}

create_response = requests.post(url =f'{URL}/pokemons' , headers = Header, json = body_createpokemon)
print(create_response.text)

change_response = requests.put(url =f'{URL}/pokemons' , headers = Header, json = body_changename)
print(change_response.text)

catch_response = requests.post(url =f'{URL}/trainers/add_pokeball' , headers = Header, json = body_catchpokemon)
print(catch_response.text)

