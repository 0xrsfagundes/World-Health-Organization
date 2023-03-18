import requests, json
import pandas as pd
import matplotlib.pyplot as plt

url = "https://apps.who.int/gho/athena/api/GHO/WHOSIS_000001.json"

params = {
    "filter": "COUNTRY:*",
}

response = requests.get(url, params=params)

data = response.json()

countries = []
years = []
rates = []
for item in data['fact']:
    rates.append(item['value']['numeric'])
    for dim in item['Dim']:
        if dim['category'] == 'COUNTRY':
                countries.append(dim['code'])
        if dim['category'] == 'YEAR':
                years.append(dim['code'])

print(years)

plt.plot(years, rates)
plt.title('Yearly Data')
plt.xlabel('Year')
plt.ylabel('rates')
plt.show()