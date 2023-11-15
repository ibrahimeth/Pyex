
import requests
import json

api_URL = "http://api.exchangeratesapi.io/v1/latest?"
apiKey = "YOUR__URL"

bozulan_doviz_TYPE= input("Bozulan Döviz Türü :")
alınan_döviz_TYPE = input("Alınan Döviz Türü :")

miktar = float(input(f"Ne Kadar {bozulan_doviz_TYPE} Bozdurmak iistiyorsunuz : "))
result = requests.get(api_URL+apiKey)
k = json.loads(result.text)
print(k)
print(k["rates"][alınan_döviz_TYPE])
#print("1" + " "+ bozulan_doviz_TYPE + " " + "=" + " " + k["rates"][bozulan_doviz_TYPE])
# miktar + " " + bozulan_doviz_TYPE + "=" +  k[bozulan_doviz_TYPE]*miktar

# %%
# import requests
# import json
# r = requests.get("https://github.com/berkocan/Doviz-Kurlari-Api-Json-Kodu/blob/main/doviz-api.php")
# print(r.text)

#%%
'''
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/moviemeter/?sort=ir,desc&mode=simple&page=1"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
list = soup.find("tbody",{"class" : "lister-list"}).findAll("tr",limit=93)
say = 0
for tr in list :
    say += 1
    title =  tr.find("td",{ "class":"titleColumn"}).find("a").text
    year =  tr.find("td",{ "class":"titleColumn"}).find("span").text
    imdb =  tr.find("td",{ "class":"ratingColumn imdbRating"}).find("strong").text
    print(f" {say}.film = {title} , yapım yılı : {year} , imbd değeri : {imdb}  ")



'''