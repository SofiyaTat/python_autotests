import requests
import pytest

URL='https://api.pokemonbattle.me:9104'
HEADER={'Content-Type': 'application/json',
        'trainer_token': 'a27f95626765fb768ede0b86d2c30681'}
qwery={'trainer_name':'sofiya'}

def test_status_code():
    #1. Тест на проверку статус кода
    response=requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=5)
    assert response.status_code==200, 'Unexpected status code'

def test_id_trainer():
    #3. Тест на проверку наличия имени тренера в ответе
    response=requests.get(url=f'{URL}/trainers', params=qwery, headers=HEADER, timeout=5)
    assert response.status_code==200, 'Unexpected status code'