my_tuple = (1,2,3,4,5,6,5,6,5,5,5,6,"gh")

print(my_tuple)

print(my_tuple[:-1])

# Tuple Methods

# count ==> used to count how many value in a list and tuples

print(my_tuple.count(5))
print(my_tuple.count("gh"))
print(my_tuple.count("bh"))

print("###########################################")

tuple2 = (3,5,5,6,3,6,24,664, 10,10,245,3,5,335,5)

print(tuple2.index(10))
print(tuple2.index(664))
print(tuple2.index(5))


########################################################


simple_tuple = ("a", 43, 54, "end")

for letter in simple_tuple:

    print(letter)


print(simple_tuple)
print(list(simple_tuple))
print(set(simple_tuple))



simple_list = [3,5,6,7,2,5,6]

tuple = tuple((x*2 for x in simple_list))

print(tuple)



