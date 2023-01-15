import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# print(r)
# print(r.content)
# print(r.url)
# print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)

s = soup.find('div', class_='entry-content')
content = s.find_all('p')
for line in content:
    print(line.text)

print("-------BREAK-------")

# Finding by id
s1 = soup.find('div', id= 'main')
# Getting the leftbar
leftbar = s1.find('ul', class_='leftBarList')
# All the li under the above ul
content1 = leftbar.find_all('li')
for line1 in content1:
    print(line1.text)
# print(content1)

print('-------BREAK1-------')
for link in soup.find_all('a'):
    print(link.get('href'))
