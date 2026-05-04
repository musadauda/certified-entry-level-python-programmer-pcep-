# Dictionaries Operations

stats = {"hp": 100, "mp": 50, "xp":1200}

print(stats["hp"])

print(stats.get("mp", "N/A"))

# Modification and merging: Python 3.9 introduced the Union Operator ==> |

base_config = {"theme":"dark", "notification": True}
user_config = {"theme":"light", "font_size":"16px"}

combined = base_config | user_config #Note -> user_config overwritten theme because it came last
print(combined)

stats = {"hp": 100, "mp": 50, "xp":1200}
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

## Merging

 

