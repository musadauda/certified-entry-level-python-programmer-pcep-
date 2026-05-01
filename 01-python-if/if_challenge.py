# FIRST CHALLENGE EVEN AND ODD NUMBER DETECTOR

# num = input("Insert a number: ")
# num = int(num)

# if num % 2 == 0:
#     print(f"Your number {num} is even")
# else:
#     print(f"Your number {num} is odd")


# SECOND CHALLENGE: GRADE CONVERTER

grade = int(input("Insert your grade (0 - 100): "))

if grade >= 90:
    print(f"{grade} is 'A'")
elif grade >= 80:
    print(f"{grade} is 'B'")
elif grade >= 70:
    print(f"{grade} is 'C'")
elif grade >= 60:
    print(f"{grade} is 'D'")
else:
    print(f"{grade} is 'F'")


### Challenge 3: Number Sorting
num1 = int(input("Insert the first number: "))
num2 = int(input("Insert the second number: "))
num3 = int(input("Insert the third number: "))

# if num1 > num2 and num2 > num3:
#     print(f"{num1},{num2},{num3}")
# elif num2 > num1  and num1 > num3:
#     print(f"{num2},{num1},{num3}")
# elif num3 > num1 and num1 > num2:
#     print(f"{num3},{num1},{num2}")
# elif num1 > num3 and num3 > num2:
#     print(f"{num1},{num3},{num2}")
# elif num2 > num3 and num3 > num1:
#     print(f"{num2},{num3},{num1}")
    
# else:
#     print(f"{num3},{num2},{num1}")

## Solution to Task3: 
if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            print(f"{num3},{num2},{num1}")
        else:
            print(f"{num2},{num3},{num1}")
    elif num2 > num1:
        if num2 > num3:
            if num1 > num3:
                print(f"{num3},{num1},{num2}")
            else:
                print(f"{num1},{num3},{num2}")
    elif num3 > num1:
        if num3 > num2:
            if num1 > num2:
                print(f"{num3},{num1},{num3}")
            else:
                print(f"{num2},{num2},{num3}")


                      


            
