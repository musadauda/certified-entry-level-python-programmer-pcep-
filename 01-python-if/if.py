height = input("Insert your height in cm or m: ")
weight =  input("Insert your weight in kg: ")
cm_m = input("Is your height in cm or m? ")


if cm_m == "cm" :
    height = float(height)/100
    weight = float(weight)
    bmi = weight/height**2
    # print(f"Your BMI is {bmi}")


elif cm_m == "m":
    height = float(height)
    weight = float(weight)
    bmi = weight/height**2
    # print(f"Your BMI is {bmi}")


else:
    print("Wrong input")

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")

elif bmi >18.5 and bmi <= 24.9:
    print(f"Your bmi is {bmi}, you are normal weight")

elif bmi >= 25 and bmi <=29.9:
    print(f"Your bmi is {bmi}, you are overweight")
else:
    print(f"Your bmi is {bmi}, you are obese")


# #calculate BMI

# bmi_m = float(weight)/float(height)**2
# bmi_cm, = bmi*10_000


# print(f"Your BMI is {bmi} and converted: {bmi_converted}")