#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests, random, time, csv, os.path


def scrape(lastPage):
    list_ = []
    filename = "/file/path/.csv" 
    # if file exist, append, otherwise create a new file
    for j in range(1, lastPage+1):    
        url = 'https://sapporo-premium2023.jp/shoplist?page=' + str(j)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser') #page変数はResponse．BeautifulSoup()にHTMLの内容が文字列として取り出して渡す

        shopBlocks = soup.find_all("div", class_="shopNameBlock")
        addresses = soup.find_all("p", class_="address")
         #tels = soup.find_all("p", class_="tel")
        len_ = len(shopBlocks)-1
        if len_ != len(addresses):  #or len_ != len(tels):
            print('Error: length of lists does not match')
            return
        else:
            shopBlocks = shopBlocks[1:]
            for i in range(len_):
                name = shopBlocks[i].text.split("\n")[1]
                category = shopBlocks[i].text.split("\n")[2:-1]
                address = addresses[i].text
                 #tel = tels[i].text
                dict_ = {"name": name, "category": category, "address": address} #, "tel": tel}
                list_.append(dict_)   


        file_exists = os.path.isfile(filename)
        keys = list_[0].keys()
        if file_exists:
            with open(filename, 'a', newline='') as sapporo:
                dict_writer = csv.DictWriter(sapporo, keys)
                dict_writer.writeheader()
                dict_writer.writerows(list_)
        if not file_exists:
            with open(filename, 'a', newline='') as sapporo:
                dict_writer = csv.DictWriter(sapporo, keys)
                dict_writer.writerows(list_)
        print('Completed page '+ str(j))     
        time.sleep(random.randint(3,5)) #次のスクレイぷに進むまで3〜5秒ランダムに待つ
    print("Completed all scrape")
    return
