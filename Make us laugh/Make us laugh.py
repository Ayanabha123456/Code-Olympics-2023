#do install requests using pip
import requests

what_joke = input("Enter 'Dark' for dark joke, 'Pun' for a pun, 'Programming' for programming joke: ")
response = requests.get("https://v2.jokeapi.dev/joke/"+what_joke+"?type=single")
results = response.json()
print("The joke: ")
joke = results['joke']
print(joke)
