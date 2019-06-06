def extract_first_and_last_index(text,keyword):
    start_index = text.find(keyword)
    end_index = start_index + len(keyword) - 1
    print(start_index,end_index)

def data_preparation(text,start_index,end_index,entity_name):
    data = (text,[(start_index,end_index,entity_name)])
    print(data)



text="Offer in Compromise OIC Overview"
# extract_first_and_last_index(text,"OIC")
data_preparation("Uber blew through $1 million a week",0,4,'ORG')
# ("Uber blew through $1 million a week", [(0, 4, 'ORG')]),

