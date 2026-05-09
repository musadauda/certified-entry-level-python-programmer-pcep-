# packing list in python

a = [3,5,7,5]
b = [67,654,32,44]
c = ["hi","high"]



d = [0, *a, 43, "boy", * b, *c] # Un-packing list

print(d)


# Unpacking Dictionaries

e = {"a": "boy", "b": "girl", "c": "mate"}
f = {"d":4, "e":54, 5:65}
g = {43:54, 5:443}

using_merge = e | f | g

unpacked_list = {**e, 
                 **f, 
                 "Testing": "Dont give in",
                 **g   
                 }

print(using_merge)  

print(f"unoacked: {unpacked_list}")


print("###############################################")

# COMPREHENSIONS - Apply operation to each and everyelement in a list.

tl = [2,4,5,77,4,5,33,22]
doubled = []


for x in tl:
    doubled.append(x * 2)

print(doubled) # traditional method

# for dictionary

ppl = [{"name":"Musa", "age":23}, {"name": "Dauda",}, {"name": "Lainsheymo"}]
names = []

for p in ppl:
    names.append(p["name"])

print(names)


############ USING LIST COMPREHENSION

bbb = [x for x in tl if x % 2 == 0]
print(bbb)