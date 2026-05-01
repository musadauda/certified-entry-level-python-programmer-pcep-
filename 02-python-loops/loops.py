# # WHILE LOOP
# number_of_attempts = 4

# password = "123456789"

# while number_of_attempts >= 0:
#     attempt = input(f"Enter your password ({number_of_attempts} attempts left): ")
#     if attempt == password:
#         print("You are correct, Welcome on board!.")
#         break
#     else:
#         print(f"Incorrect Password ({number_of_attempts} attempts left)")
#     number_of_attempts -= 1


for x in range(100):
    print(f"{x}")
    if x==99:
        print("LIFTOFF!")