import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '6f34a5d2e04afa483f14642c7ba03c0a'
Header = {'Content-Type' :'application/json', 'trainer_token': Token
          }
Trainer_id = 12524

def test_trainer_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : Trainer_id})
    assert response.status_code == 200

def test_trainer_name():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : Trainer_id})
    assert response_name.json()["data"][0]['trainer_name'] == 'Nikita'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Nikita'), ('city', 'Msk')])

def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : Trainer_id})
    assert response_parametrize.json()['data'][0][key] == value