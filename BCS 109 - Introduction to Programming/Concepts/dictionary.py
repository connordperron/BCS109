# Connor Perron

released = {
    "iPhone" : 2008,
    "iPhone 7" : 2015,
    "iPhone 8" : 2016,
    "iPhone 9" : 2017,
    "iPhone 10" : 2019,
    }
print(released)

#add a new item to the dictionary
released["iPhone 11"]=2020
print("\nNew item added", released)

#delete am item
del released["iPhone"]
print("\niPhone from 2008 deleted", released)

#print the number of key value pairs
print("\nThere are this many key value pairs:", len(released))

#get a value from the specified key
print("-" * 10)
print("iPhone releases so far: ")
print("-" * 10)
for release in released:
    print(release)
