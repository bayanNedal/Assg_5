sample_dict ={"name" : "kelly", "age" : 25, "salary" : 8000 , "city" : "NewYork"}
delKeys = ["name", "salary"]
for delKey in delKeys:
    del sample_dict[delKey]
print(sample_dict)
# or use " sample_dict.pop(delkey)