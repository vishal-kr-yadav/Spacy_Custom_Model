import numpy as np

dataset=np.load("final_dataset.npy").tolist()
# print((dataset[:]))
# TRAIN_DATA = [
#     ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
#     ("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
# ]
a=[]
for each in dataset:
    for i in each:
        a.append(i)
print(len(a))
# a =[]
# for each in dataset:
#     print(each)




# TRAIN_DATA = [
#     ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
#     ("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
# ]