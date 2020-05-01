import requests
import json


r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=427c499ac2b0474d86e3351137b0de9d')

content = r.text

news = json.loads(content)

with open('news.json', 'wb') as file:
    file.write(r.content)

for element in news['articles']:
    # print(element['title'])
    if element['source']['name'].find('India') != -1:
        print(element['title'])