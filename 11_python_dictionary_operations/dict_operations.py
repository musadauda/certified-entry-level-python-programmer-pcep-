# Dictionaries Operations

stats = {"hp": 100, "mp": 50, "xp":1200}
new_dict = {"name":"Musa", "age":1999}

print(stats["hp"])

print(stats.get("mp", "N/A"))

stats.update(new_dict)
print(stats)

# Modification and merging: Python 3.9 introduced the Union Operator ==> |

base_config = {"theme":"dark", "notification": True}
base_config.update(stats)
user_config = {"theme":"light", "font_size":"16px"}

combined = base_config | user_config #Note -> user_config overwritten theme because it came last
print(combined)

# accessing key, values and enteries
key = stats.keys()
values = stats.values()
items = stats.items()

print(key)
print(values)
print(items)


#iterate over pairs
for key, values in stats.items():
    print(f"Stats: {key} | Value {values}")

## COPYING A DICTIONARY

data1 = {"a": 1, "b":2, "c": 3}
data2 = data1 # Not a copy but a reference to a dictionary

copy_data1 = data1.copy() # This creates a real copy








## SETTING DEFAULTS IN A DICTIONARY
# Reverse from merging

person = {"name": "Musa Dauda", "hair_color": "black", "height": "5.7", "age": 100}
defaults = {"name": "N/A", "hair_color": "N/A", "height": "N/A", "age": 0}

# setdefaults

person.setdefault("graduated", "N/A")
print(person)
person.setdefault("eaten", "N/A")
person.setdefault("first_class", "N/A")
print(person)


 

