fruits = ["Banana", "Apple", "Papaya", "Guava", "Eggplant"]

fruits_copy = fruits[:]

reverse_fruits = fruits[::-1]

print(fruits_copy)
print(reverse_fruits)

li = [3,5,6,3,554,33,]
fruits_copy.remove("Eggplant")
fruits_copy.insert(2, li)
fruits_copy.extend(li)
print(fruits_copy)


print("#######################################################")


def rotate(l):
    l.append(l.pop(1))
    return l

print(rotate(fruits))


fruit = ["Banana", "Apple", "Papaya", "Guava", "Eggplant"]


def rotate_left(li):
    li.append(li.pop(0))
    return li
    

def rotate_right(li):
    li.insert(0, li.pop(-1))
    return li

print("*********************")
print(rotate_right(fruit))



def rotate_special(l, number_to_rotate, direction="left"):
    if direction == "left":
        for i in range(number_to_rotate):
            rotate_left(l)
    elif direction == "right":
        for i in range(number_to_rotate):
            rotate_right(l)
    else:
        print("Wrong input")    
    
    return l

print("rotations")
print(rotate_special(fruit, 2, "right"))
print(rotate_special(fruit, 1, "left"))


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44")

def ispalindrome(str):
    return str  == str[::-1]

print(ispalindrome("madam"))
print(ispalindrome("hello"))