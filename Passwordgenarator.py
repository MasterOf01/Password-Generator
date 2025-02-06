import random
import string
import requests

def random_character():
    choices=string.ascii_letters+string.digits+string.punctuation
    return random.choice(choices)

passwordLengths=12

def generate_strong_password():
    password=""
    for i in range(passwordLengths):
        password = password + random_character()
    print(password)

generate_strong_password()

def fetch_word():
    response=requests.get("https://random-word-api.herokuapp.com/word?length=6")
    word=response.json()[0]
    return word

print(fetch_word())