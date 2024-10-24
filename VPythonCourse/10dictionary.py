#dictionary 
'''
Collection of Key - Value pairs
also known as associative array
also known as map, hashmap
unordered
keys unique in one dictionary
storing, extracting
'''
student = {("name", "alice"), ("age", 20),("grade", "A")}

#dictionaries are mutable
student1 = {"name": "alice", "age": 20, "grade": "A"}
print(student)
print(student1)

emptyd = {} # most common way of creating a new dictionary
print(len(emptyd))
print(type(emptyd))

also_dict = dict()  # alternative way of making a blank dictionary
print(also_dict)  # when we print we see curly braces, that strongly implies a dictionary (although sets also use {})

tel = {'jack': 4098, 'sape': 4139} # so  { key: value, key2:value2, and so on}
print(tel)

# so what can be keys ? what happens if we add second identical key
tel = {'jack': 4098, 'sape': 4139, 'jack': 9000} # you generally should not do this, keys should be unique
print(tel)

# & C:/Users/grace/AppData/Local/Programs/Python/Python312/python.exe c:/Users/grace/VisualStudioProject/Self_Learning/VPythonCourse/10dictionary.py

# add a new key-value pair
tel['guido'] = 4127
print(tel.keys())
print(tel.values())

tel['valdis'] = [9000,2640,2911]  # I can store a list of numbers as value in my dictionary against some specific key
print(tel)

tel_list = [['jack',9000], ['valdis',9000]]
print(tel_list)  # 2D list  checking for specific entry will be slow unless I know the index

new_dict_from_tel_list = dict(tel_list)  # so i can pass a 2d list type of structure with 2 entries and create a new dictionary
print(new_dict_from_tel_list)

#we can have multiple valdis with multiple phone numbers
tel_list = [['jack',9000], ['valdis1',9000], ['valdis2',2640], ['valdis3',2911]]
print(tel_list)

#change it into dictionaries
new_dict_from_tel_list = dict(tel_list)  # so i can pass a 2d list type of structure with 2 entries and create a new dictionary
print(new_dict_from_tel_list)

tel['sape'] = 54545  # i can overwrite already existing value (no warning given!)
print(tel)

key = 'nnevaldis'
# key = 'valdis'
if key in tel:
    print(tel[key]) # we print the value of the key if there is such a key
else:
    print("No such key")


#memebership test
print('valdis' in tel)  # so we can check if a key is in the dictionary

print(tel.get('valdis')) # gets value by key without errors

print(tel.get('nevaldis')) #by default on bad key we get None

print(tel.get('nevaldis', '555-1212')) # we can change the return on bad keys to our own 

#usage of getting versus direct access
# remove key value pair
tel['sape'] = 665453 # create key or overwrite if it existed
del tel['sape']  # so i can delete a specific key
print(tel)

# del tel['sape'] # so for deletion we would need to check first if the key exists (no get alternative)
d = {'a':100, 'b':200, 'c':300, 'd':400}
d['b'] += 10
d['a'] += 20
d['b'] += 30
d['d'] += 50
e = d.get('b')
print(e)

d = {'a':100, 'b':200, 'c':300, 'd':400}
total = 0
for key, value in d.items():
    if value % 200 == 0:
        total += value
print(total)

d = {'foo':[1,2,3], 'bar':[4,5,6], 'beef':[7,8,9]}
d['foo'].append(4)
d['bar'].append(10)
d['bar'] = [11,12,13]
d['bar'].append(14)
result = sum(d['bar'])
print(result)

'''
food = "kartupelis"
d = {c:c.upper()*2 for c in food}
print(d['c'])
'''
