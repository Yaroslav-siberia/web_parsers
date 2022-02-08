# scraper.py
import requests
from bs4 import BeautifulSoup
from lxml import html
import re


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
url_list = 'http://www.laughfactory.com/jokes'
request = requests.get(url_list, headers = headers)
soup = BeautifulSoup(request.text, "html.parser")

links = soup.findAll("div", class_="jokes-nav")
links2 = links[0].find_all('a', href=True)
list_of_links = []
for link in links2:
    list_of_links.append(link['href'])

with open('file.txt', 'a') as file:
    for teme in list_of_links:
        if 'popular-jokes' in teme:
            continue
        if 'latest-jokes' in teme:
            continue
        if 'joke-of-the-day' in teme:
            continue
        else:
            for i in range(1,1000):
                url = teme + f'/{i}'
                print(url)
                request = requests.get(url, headers=headers)
                soup = BeautifulSoup(request.text, "html.parser")
                jokes = soup.findAll("div", class_="joke-text")
                if len(jokes) == 0:
                    break
                else:
                    for j in jokes:
                        try:
                            j = str(j)
                            res = re.search(r'\d">\s+(.*?)</p>', j).group()
                            res = res.replace('<br/>',';')
                            res = res.split('>')[1]
                            res = res.split('   ')[8]
                            file.write(res+'\n\r')
                        except:
                            print('error')
file.close()




