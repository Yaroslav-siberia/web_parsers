import requests
from bs4 import BeautifulSoup

url = 'https://upjoke.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)

quotes = soup.find_all('div', class_='random-categories-wrapper')
#print(len(quotes))
#print(quotes)

#categories = quotes[0].find_all
categories_list = []
for a in quotes[0].find_all('a', href=True):
    categories_list.append(a['href'])

#print(categories_list)
with open('./upjoke.txt','a') as file:
    for cat in categories_list:
        new_url = url[0:-1]+cat
        #print(new_url)
        response = requests.get(new_url)
        soup = BeautifulSoup(response.text, 'lxml')
        jokes = soup.find_all('div', class_='joke-content')
        for joke in jokes:
            title = joke.find_all('h3', class_='joke-title')
            content = joke.find_all('div', class_='joke-body')
            joke_str = ''
            title = BeautifulSoup(str(title), 'lxml')
            title1 = title.find('h3').contents[0]
            joke_str += title1
            content = BeautifulSoup(str(content), 'lxml')
            content1 = content.find('div')
            for c in content1.contents:
                c = str(c)
                if c != '<br>' and c != r'<br/>':
                    joke_str += ';' + c
            file.write(joke_str + '\n')
            print(joke_str)
file.close()
