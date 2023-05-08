#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests, random, time, csv, os.path

firstPage = 1
lastPage = 5
for j in range(firstPage,lastPage):
    print('Started page ' + str(j))
    url = 'https://sub.nagoya-shouhinken.com/prd/c_app/shoplists?page=' + str(j)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser') #page変数はResponse．BeautifulSoup()にHTMLの内容が文字列として取り出して渡す

    names = soup.find_all("h2", class_="p-area-shoplist__headline")
    areas = soup.find_all("dd", class_="-area")
    categories = soup.find_all("dd", class_="-category")
    addresses = soup.find_all("dl", "p-area-shoplist__address")


    l = []
    d = {}
    for i in range(len(names)):
        name = names[i].text.split('\n')[1].strip()
        area = areas[i].text
        category = categories[i].text
        address = addresses[i].text.split("\n")[3]
        tel = addresses[i].text.split("\n")[-3]
        d = {"name": name, "area": area, "category": category, "address": address, "tel": tel}
        l.append(d)
    

# if file exist, append, otherwise create a new file
    filename = [path/of/file/name]
    file_exists = os.path.isfile(filename)
    
    keys = l[0].keys()
    if file_exists:
        with open([path/of/file/name], 'a', newline='') as nagoya:
            dict_writer = csv.DictWriter(nagoya, keys)
            dict_writer.writeheader()
            dict_writer.writerows(l)
    if not file_exists:
        with open([path/of/file/name], 'a', newline='') as nagoya:
            dict_writer = csv.DictWriter(nagoya, keys)
            dict_writer.writerows(l)
    print('Completed page '+ str(j))     
    time.sleep(random.randint(3,5)) # wait randomly for next scrape
print("Completed all scrape")

