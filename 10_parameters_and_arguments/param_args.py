# keywords arguments: describe_pet(name="Chew", animal_type="Hamster")
# positional arguments: describe_pet("Hamster", "Chew")
# default parameters: def greet(name, msg="Good morning!")
# variable length parameters: def sum_numbers(*args):
# *args (Arbitrary Positional Arguments) - Captures extra positional arguments as a tuple.
# **kwargs (Arbitrary Keyword Arguments) - Captures extra keyword arguments as a dictionary.
# Forced Constarints - def strict_func(pos_only, /, standard, *, kw_only) 


# positional only

def add(a, b, /, c, d,  *, e, f,): # positional only
    return a + b + c + d + e + f


# print(add(1, 2, 3, 4, 5, 6))
# print(add(a = 1, b = 2, c= 3, d = 4, e = 5, f = 6)) #error

print(add(1, 2, 3, 4, e = 5, f = 6))


############

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

print(build_profile('Albert', 'Einstein', field='Physics', prize='Nobel'))