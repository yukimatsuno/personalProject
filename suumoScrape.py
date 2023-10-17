#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests, random, time, csv, os.path


chintai = []
for pageNum in range(1, 2):
    url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&sc=13201&sc=13202&sc=13203&sc=13204&sc=13205&sc=13206&sc=13207&sc=13208&sc=13209&sc=13210&sc=13211&sc=13212&sc=13213&sc=13214&sc=13215&sc=13218&sc=13219&sc=13220&sc=13221&sc=13222&sc=13223&sc=13224&sc=13225&sc=13227&sc=13228&sc=13229&sc=13300&cb=0.0&ct=9999999&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50&page=' + str(pageNum)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser') #page変数はResponse．BeautifulSoup()にHTMLの内容が文字列として取り出して渡す
    for box in soup.find_all("div", class_="cassetteitem"):
        name = box.find("div", class_="cassetteitem_content-title").text.replace('\u3000', ' ')
        
        type = box.find("span", class_="ui-pct ui-pct--util1").text
        address = box.find("li", class_="cassetteitem_detail-col1").text
        temp_trainLine = box.find_all("li", class_="cassetteitem_detail-col2")
        trainLine = [i for i in temp_trainLine[0].text.split('\n') if i != '']
        temp_structure = box.find_all("li", class_="cassetteitem_detail-col3")
        structure = [j for j in temp_structure[0].text.split('\n') if j != '']

        #Each room
        roomList = []
        for rentBox in box.find_all("tr", class_="js-cassette_link"):
            roomInfo = []
            
            #extract rent
            rent = rentBox.find("span", class_="cassetteitem_other-emphasis ui-text--bold").text
            
            #extract floor
            count = 0
            for tdList in rentBox.find_all("td"):
                count += 1
                if count == 3:
                    floor = tdList.text
                    floor = floor.strip()
                    break

            #extract maintenance fee
            maintenanceFee = rentBox.find("span", class_="cassetteitem_price cassetteitem_price--administration").text
                            
            #extract deposit
            deposit = rentBox.find("span", class_="cassetteitem_price cassetteitem_price--deposit").text    
            
            #extract gratuity 
            gratuity = rentBox.find("span", class_="cassetteitem_price cassetteitem_price--gratuity").text 

            #extract madori 
            madori = rentBox.find("span", class_="cassetteitem_madori").text
        

            #extract menseki
            menseki = rentBox.find("span", class_="cassetteitem_menseki").text
            #extract link
            for link in rentBox.find_all("a", href=True):
                href = link.get("href")
                if href and not href.startswith("javascript:void"):
                    hyperLink = href
            
            for i in [floor, rent, maintenanceFee, deposit, gratuity, madori, menseki, hyperLink]:
                roomInfo.append(i)       
            roomList.append(roomInfo)
            
         
        #entry = [name, address, [trainLine], [structure], roomList[[floor, rent, maintenanceFee, deposit, gratuity, madori, menseki, href]]]
        entry = []             
        for i in [name, type, address, trainLine, structure, roomList]:
            entry.append(i)
        chintai.append(entry)

print(chintai)

"""

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
"""