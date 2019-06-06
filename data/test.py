import requests
from bs4 import BeautifulSoup
import json
import numpy as np



def prepare_dataset(text,keyword,entity_name):

    start_index = text.find(keyword)

    if start_index == -1:

        return 0

    end_index = start_index + len(keyword) -1

    # preparing the structure of training dataset
    data = (text,{"entities":[(start_index,end_index,entity_name)]})

    return data

def extract_website_content(url):

    website = requests.get(url)

    soup = BeautifulSoup(website.content)

    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]

    return text

def get_training_data(url):

    content=extract_website_content(url)

    final_list = []
    for each in content:
        final_list.append(each.split('.'))
    result=[]

    with open("data.json") as f:
        pre_defined_data = json.load(f)

    for each_set in pre_defined_data:

        for each in final_list:

            for inner_each in each:

                if len(inner_each) > 0 :

                    single_set_tuple = prepare_dataset(inner_each,each_set['entityName'],each_set['entityType'])

                    if single_set_tuple != 0:

                        result.append(single_set_tuple)
    return result


with open("mikeHabib_link.json") as f:
    link_data = json.load(f)

counter = 0
final_result = []
for each_link in link_data:
    try :

        final_dataset = get_training_data(each_link['link'])
        # print("final_dataset=====>",final_dataset)
        if len(final_dataset) > 0 :
            final_result.append(final_dataset)
            # print("---",final_dataset)
        np.save("mikeHabib_dataset.npy", final_result)
        # with open('testFile.json', 'a') as outfile:
        #     json.dump(final_dataset, outfile)
        counter+=1
        print("counter====>",counter)
    except :
        print("in Exception")
        pass






# dataset=np.load("final_dataset.npy")
# print("dataset=",dataset)
#

