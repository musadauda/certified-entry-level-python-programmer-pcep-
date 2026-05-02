# create a function "combine" that takes two dictionary and return a new dictionary with the two dictionaries combined.

def combine(d1, d2):
    dict_com = {}
    for i in d1:
        dict_com[i] = d1[i]
    for i in d2:
        dict_com[i] = d2[i]
    return dict_com

print(combine({"H":1, "a":3,"b":43,"c":54}, {2:4,4:54,4:54}))

def combine_strict(d1, d2):
    dict_com = {}
    for key in d1:
        if key in d2:
            print("This dictionaries contained duplicate keys... Exiting")
            return {} ## Short circuiting
    for i in d1:
        dict_com[i] = d1[i]
    for i in d2:
        dict_com[i] = d2[i]
    return dict_com

print(combine_strict({"H":1, "a":3,"b":43,"c":54}, {"a":4,4:54,4:54}))


def access_entry(d, key_name):
    for key in d:
        if key.lower() == key_name.lower():
            return d[key]
        
    return None

print(access_entry({"name": "Shawn", "Boy":"Yes"}, "NAME"))