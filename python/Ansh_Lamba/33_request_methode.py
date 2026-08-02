import requests

response = requests.get("https://www.youtube.com/watch?v=ZvU7lupoXQE")
print(response)
data = response.json
print(data)