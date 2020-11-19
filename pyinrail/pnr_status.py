import requests

url = "https://indianrailways.p.rapidapi.com/index.php"

querystring = {"pnr":"1234567890"}

headers = {
    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
    'x-rapidapi-key': "YOUR_API_KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)