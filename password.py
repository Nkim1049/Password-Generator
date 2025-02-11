
import random
import string
import requests 

# function that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

int(input("what length for the password?"))

# function that generates a password of random characters
def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()

# function that gets a random word from a dicinotary api
def fetch_word():
    url = "https://random-word.herokuapp.com/word?length=6"

    response = requests.get(url)
    word = response.json()[0]
    return word

#function to generate weaker but memorable password
def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetchword()
    password = word1+ word2
    return password

print(generate_weaker_password())
