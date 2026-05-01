###  Convert words to it's components
def get_words(words):
    word = words.split(" ")
    return word

print(get_words("This is a string thats about to be converted to a list"))

# a function that capitalize the first word in a string

def capitalize(words):
    first_letter = words[0]
    rest_letter = words[1:]
    return f"{first_letter.upper()}{rest_letter.lower()}"

print(capitalize("this is a string")) 

def capitalize_words(words):
    result_op = ""
    for word in get_words(words):
        capitalized_words = capitalize(word)
        result_op += capitalized_words + " "
    return result_op


print(capitalize_words("this is a string")) 
