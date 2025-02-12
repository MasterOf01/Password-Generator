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

def generate_weaker_password():
    word1=fetch_word()
    word2=fetch_word()
    word1=replaceletter(word1)
    word2=replaceletter(word2)
    password=word1+word2
    return password

def replaceletter(word):
    word=word[0].upper()+word[1:]

    if "a" in word:
        word=word.replace("a","@")
        word=word.replace("s","$")
        word=word.replace("o","0")
    
    return word

print(generate_weaker_password())