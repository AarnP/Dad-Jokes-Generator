import requests
from random import choice
import pyfiglet
from termcolor import colored
header = pyfiglet.figlet_format("DAD JOKE HAHA!!")
coloured_header = colored(header, color="blue")
print(coloured_header)

user_input = input("What would you like to search for: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term":user_input}
).json()

num_jokes = res["total_jokes"]
result = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}, here's one: ")
    print(choice(result)["joke"])
elif num_jokes == 1:
    print(f"There is one joke about {user_input}")
    print(result[0]['joke'])
else: 
    print(f"There are no jokes with your term: {user_input}")
    

