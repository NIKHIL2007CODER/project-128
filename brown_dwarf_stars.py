from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"


time.sleep(3)

page = requests.get(START_URL)
soup = BeautifulSoup(page.text , "html.parser")
star_table = soup.find_all("table" , attrs = {"class" , "wikitable sortable"})
total_table = len(star_table)

# Define Exoplanet Data Scrapping Method

tempList = []
table_body = star_table[0].find('tbody')
table_rows = table_body.find_all('tr')
print(table_rows)
for col in table_rows:
    td = col.find_all('td')
    data = [i.text.rstrip() for i in td]
    tempList.append(data)


star_name = []
distance = []
mass = []
radius = []


for i in range(1,len(tempList)):
    star_name.append(tempList[i][0])
    distance.append(tempList[i][5])
    mass.append(tempList[i][7])
    radius.append(tempList[i][8])
    

 

headers = ["star_name" , "distance" , "mass" , "radius"]

star_df = pd.DataFrame(list(zip(star_name,distance,mass,radius,)), columns = headers )
star_df.to_csv("Brown_dwarf.csv" , index = True , index_label = "id")


        
# Calling Method    


# Define Header


# Define pandas DataFrame   


# Convert to CSV

    


