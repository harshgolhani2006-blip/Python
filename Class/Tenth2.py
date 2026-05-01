#Dictionary
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
#1 Mutable
#key : 1imutal. 2 unique.

#Create dictionary.
# dt={}
# dt1=dict()
# print(dt,dt1)
# dt={1:5,2:10,3:15,"hello":"world","python":"programming","abc":123}
# print(dt)
# print(type(dt))

#list and dictionary
# list=[1,2,3,4,5]
# dt={1:5,2:10,3:15,"hello":"world","python":"programming","abc":123}
# print(list[0])  # Accessing the first element of the list
# print(dt[1])  # Accessing the value associated with the key 1 in the dictionary
# print(dt["hello"])  # Accessing the value associated with the key "hello" in the dictionary

#list of tuples and dictionary
# list_of_tuples=[(1,5),(2,10),(3,15),("hello","world"),("python","programming"),("abc",123)]
# dt=dict(list_of_tuples)
# print(dt)

#List of lists and dictionary
# list_of_lists=[[1,5],[2,10],[3,15],["hello","world"],["python","programming"],["abc",123]]
# dt=dict(list_of_lists)    
# print(dt)

#List of sets and dictionary
# list_of_sets=[{1,5},{2,10},{3,15},{"hello","world"},{"python","programming"},{"abc",123}]
# dt=dict(list_of_sets)
# print(dt)  # This will raise a TypeError because sets are unhashable and cannot be used as keys in a dictionary   

#set of tuples and dictionary
# set_of_tuples={(1,5),(2,10),(3,15),("hello","world"),("python","programming"),("abc",123)}
# dt=dict(set_of_tuples)
# print(dt)

#set of list and dictionary.
# set_of_list=[{1,5},{2,10},{3,15},{"hello","world"},{"python","programming"},{"abc",123}]
# dt=dict(set_of_list)
# print(dt)  # This will raise a TypeError because lists are unhashable and cannot be used as keys in a dictionary

#set of sets and dictionary
# set_of_sets=[{1,5},{2,10},{3,15},{"hello","world"},{"python","programming"},{"abc",123}]
# dt=dict(set_of_sets)
# print(dt)  # This will raise a TypeError because sets are unhashable and cannot be used as keys in a dictionary.

# dictionary properties
# dt={1:5,2:10,3:15,"hello":"world","python":"programming","abc":123}
# print(dt)
# print(dt.keys())
# print(dt.values())
# print(dt.items())

#dictionary loop.
# dt={1:5,2:10,3:15,"hello":"world","python":"programming","abc":123}
# for key in dt:
#     print(key,dt[key])  # This will print the keys of the dictionary
# for value in dt.values():
#     print(value)  # This will print the values of the dictionary
# for key,value in dt.items():
#     print(key,value)  # This will print the key-value pairs of the dictionary

dt={1:5,2:10,3:15,"hello":"world","python":"programming","abc":123}
dt[1]=50  # Modifying the value associated with the key 1
print(dt)