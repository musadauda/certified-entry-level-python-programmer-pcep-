word = input("Statement or words we should count from: ")
l = input("Which letter do you want to count? ")
counter = 0

for i in word:
    if i == l:
        counter += 1


print(f"The word '{l}' appeared {counter} times.")