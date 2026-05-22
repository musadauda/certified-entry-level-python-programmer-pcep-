# create_set([4,3,4,2]) ==> returns a dictionary representing the set 

def create_set(item_list):
    some_set = {}
    for item in item_list:
        # Item doesnt matter, the key is what makes it unique
        some_set[item] = None

    return some_set

print(create_set([3,4,5,3,2,"this", "that"]))

# add_to_set(dictionary, value) ==>  it should return a dictionary including the value

def add_to_set(some_dict, value):
    some_dict[value] = True
    return some_dict

print(add_to_set(create_set([3,4,5,3,2,"this", "that"]), "this"))




# discard_set(dictionary, value_to_remove) ==> returns dictionary without the value

def discard_set(some_dict, value_to_remove):
    # .pop(key, default_value) ==> remove key if it exists
    some_dict.pop(value_to_remove, None)
    return some_dict


my_set = create_set([4, 3, 4, 2,5])
print(discard_set(my_set, 56)) 
