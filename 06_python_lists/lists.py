# Copy a list from an existing list

test_list = ["Boy", "A Car", 89000, "BMW M340i", "Mercedes Benz G63s", 4-3j,  3.43]
copy_list = []
for i in test_list:
    copy_list.append(i)

print(copy_list)

## append a list to another

list_appeding = ["Guava", "Mango", "Banana"]

appended_list = test_list + list_appeding
print(appended_list)

### Get a position of a list

def get_position_list(list_name, pos):
    return list_name[pos - 1]

print("###############################")
print(get_position_list([2,44,45,5, "Hi", "A Good try", "Be"], 5))



# iterate in python list



# Reverse a list

reverse_list = test_list[::-1]

print(reverse_list)