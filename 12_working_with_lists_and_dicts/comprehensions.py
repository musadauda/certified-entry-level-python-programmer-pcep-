numbers = [1,2,3,4,5,6,7,8,9]
doubled = []

doubled = [x * 2 for x in numbers]

print(doubled)

######## perform value or checks with list
even = [x for x in numbers if x % 2 == 0]
print(even)




people = [{"name": "A", "age": 55}, {"name":"B", "age":23}, {"name":"C", "age":15}]

peoples_name = [p["name"] for p in people]
over_20 = [p for p in people if p["age"] > 20]

print(over_20)
print(peoples_name)


d1 = {"a": 1, "b": 2, "c": 3, "d":5}
print(d1)
# dic comprehension ==> {key : value for key, value in dictionary.items() }
decom = {key.upper() : value*4 for key, value in d1.items()}
print(decom)


