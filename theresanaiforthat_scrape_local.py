from bs4 import BeautifulSoup
import requests

url = "https://theresanaiforthat.com/ai/molin/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') #page変数はResponse．BeautifulSoup()にHTMLの内容が文字列として取り出して渡す

name = soup.find_all("div", class_="title_wrap")
use_case = soup.find_all("div", id="use_case")
tags = soup.find_all("a", class_="tag")
description = soup.find_all("div", class_="description")
image = soup.find_all("img", class_="ai_image")

name = name[0].text.split('\n')[1].strip()
print("NAME", name)
use_case = use_case[0].text
print("USE_CASE", use_case)
tags = [tag.text for tag in tags]
print("TAGS", tags)
description = description[0].text[24:]
print("DESCRIPTION", description)
image = image[0]["src"]
print("IMAGE", image)
