num = {2, 3, 5, 7}

for numbers in num:
    print(numbers)


empty_set = set()

some_set = set([3,5,6,6,3,2,2,5,9])

print(some_set)

# dict_set = {{"a":99}, 5, 6,} ## unhashable error
# print(dict_set)


# sets used for membership testing => very efficient

prime_numbers = {2,3,5,7,10,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,79}

if 10 in prime_numbers:
    print(f"10 is prime numbers")

else:
    print(f"10 is not prime numbers")


prime_numbers.add(73)

print(prime_numbers)

prime_numbers.remove(10) # Give KeyError when key not found

print(prime_numbers)

prime_numbers.discard(111) # does not give KeyError when key not found

print(prime_numbers)

prime_numbers.clear()
print(prime_numbers)


# SET OPERATIONS

prime_numbers = {2,3,5,7,11,13,17,19,23,29,31}
even_numbers = {2,4,6,8,10,12,14,16,18,20,22,24,26,28}
odd_numbers = {1,3,5,7,9,11,13,15,17,19,21,23,25,27,29}

# UNION "|" ==> Join 2 sets  into one set

union = prime_numbers | even_numbers | odd_numbers
print(union)


# INTERSECTION "&" ==> Only elements common in sets

intersection = prime_numbers & even_numbers
print("Intersection")
print(intersection)


# DIFFERENCE "-", ==> Eements in set1 and not in set2 or the intersection

diff = prime_numbers - even_numbers
print("Difference")
print(diff)

# SYMMETRIC DIFFERENCE "^"==> Elements in set1 or set2 but not in both

sym_diff = prime_numbers ^ even_numbers
print("Symmetric Difference")
print(sym_diff)



