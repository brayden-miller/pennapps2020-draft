import requests
import json

url = "http://www.wolframalpha.com/queryrecognizer/query.jsp?appid=DEMO&mode=Default&i=Norway"
table = requests.get(url).json()