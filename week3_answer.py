# FTDS Week 3 Test

import requests
import json
from bs4 import BeautifulSoup

# Complete the functions below according to the questions provided.

def CarParkInfo():
    result = []
    content = json.loads(requests.get("https://openapi.westkowloon.hk/datagovhk/carpark").text)
    for i in range(2) :
        result.append(content['carParks'][i]['name']['en'])
        result.append(content['carParks'][i]['heightLimit'])
    #print() # uncomment to use for visualizing variables etc.

    return result

#CarParkInfo() # uncomment this line of code and run python week3.py to test function.

def findTotalSum(n):
    sum = 0
    for i in range(1,n+1) :
        soup = BeautifulSoup(requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html").text,"html.parser")
        data = soup.find_all("p",class_="price_color")
        for j in range(len(data)) :
            sum += float(data[j].text.replace("Â£",""))
    #print() # uncomment to use for visualizing variables etc.

    return sum

#findTotalSum(3) # uncomment this line of code and run python week3.py to test function.