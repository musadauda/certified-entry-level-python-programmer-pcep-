## Reverse_halves(lists) - splits down a middle - first half at end and vice versa


def reverse_halves(lists):
    middle = int(len(lists) / 2)
    first_half = lists[:middle]
    last_half  = lists[middle:]
    return [*last_half, *first_half]

print(reverse_halves([1,2,3,4,5,6,7,8]))
print(reverse_halves([1,2,3,4,5,6,7,8,9]))

## Apply defaults

def apply_defaults(dict, defaults):
    return { **defaults, **dict }

print(apply_defaults({"a":1, "b":2, "c":3}, {"d":4, "e":5}))



## Upper case keys from a dict

def uppercase_keys(dict):
    return [keys.upper() for keys in dict.keys()]

print(uppercase_keys({"a":1, "b":2, "c":3, "done": "True"}))


# take a number say 10 and generate to 10 square

def square_map(max_num):
    return [x * x for x in range(1, max_num + 1)]


print(square_map(50))