import requests
from bs4 import BeautifulSoup

def prepare_dataset(text,keyword,entity_name):

    start_index = text.find(keyword)
    if start_index == -1:
        return 0
    end_index = start_index + len(keyword) - 1
    data = (text,[(start_index,end_index,entity_name)])

    return data

def extract_aff_content(url):

    website = requests.get(url)
    soup = BeautifulSoup(website.content)
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    return text

content=extract_aff_content("https://www.myirstaxrelief.com/")

final_list = []
for each in content:
    final_list.append(each.split('.'))
result=[]
for each in final_list:
    for inner_each in each:
        if len(inner_each) > 0 :
            single_set_tuple = prepare_dataset(inner_each,'IRS','ORG')
            if single_set_tuple != 0:
                result.append(single_set_tuple)
print(result)

