import requests
import json
import wolframalpha


url = "http://www.wolframalpha.com/queryrecognizer/query.jsp?appid=PY2VE67L9AV92EH9&mode=Default&i=Norway"
url = "http://www.wolframalpha.com/summaryboxes/v1/query?appid=PY2VE67L9AV92EH9&path=countries/e/l5/vw/el"
r = requests.get(url).content
print(r)
client = wolframalpha.Client("PY2VE6-7L9AV92EH9") 
country = input('Country: ') 

res = client.query('What is the population of ' + country + '?')
answer = next(res.results).text 
print(answer)
res = client.query('What is the life expectancy of ' + country + '?')
answer = next(res.results).text 
print(answer)
res = client.query('What is the capital of ' + country + '?')
answer = next(res.results).text 
print(answer)
res = client.query('What is the GDP of ' + country + '?')
answer = next(res.results).text 
print(answer)
res = client.query('What is the GDP per capita of ' + country + '?')
answer = next(res.results).text 
print(answer)
res = client.query('What are the three largest cities in ' + country + '?')
answer = next(res.results).text 
print(answer)