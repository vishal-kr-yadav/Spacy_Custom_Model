import requests
from bs4 import BeautifulSoup
def extract_aff_content(url):

    website = requests.get(url)
    soup = BeautifulSoup(website.content)
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    return text


content=extract_aff_content("https://www.myirstaxrelief.com/")
print(type(content))
final_list = []
for each in content:
    final_list.append(each.split('.'))

for each in final_list:
    for inner_each in each:
        print("==",inner_each)
        print(type(inner_each))
        print(len(inner_each))