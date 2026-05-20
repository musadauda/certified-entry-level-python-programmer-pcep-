# Create a func index_all(list, item) and it should return a list of the indexes of all the arguments passed


def index_all(search_list, item):
    indices = []
    for index, value in enumerate(search_list):
        if value == item:
            indices.append(index)
    return indices


print(index_all([2,2,5,3,2,5,1,2,2,2,3,3,42,2,2,3], 2))


def index_all2(search_list, item):
    indices = []
    # loop from 0 to lenth of list minus 1
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append(i)
    return indices

print(index_all2([45,1,2,2,2,3,3,42,2,2,3], 2))
  

# create an append function that can be used for tuples. take tuples as arguments and an value you want to add by returning a new tuple add_tuple(tuple, item)

def append_tuple(init_tuple, item):
    list_t = list(init_tuple)
    list_t.append(item)
    return tuple(list_t)


print(append_tuple((2,4,5,3), "Hello World"))





### recreate the insert method for tuples insert(tuples, index, value)

def insert_t(init_tuples, index, value):
    tuple_list = list(init_tuples)
    tuple_list.insert(index, value)
    return tuple(tuple_list)

print(insert_t((3,4,5,2,5), 4, "Insert this!"))
