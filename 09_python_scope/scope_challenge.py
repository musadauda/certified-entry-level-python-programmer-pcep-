#Using closure create an advanced incrementer function

def create_counter():
    count = 0

    def incrementer():
        nonlocal count
        print(f"current: {count}")

        count += 1
        print(f"New Count = {count}")

        return count
    return incrementer

my_counter = create_counter()

print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())


### Making a more advanced incrementer

def create_counter_advanced():
    count = 0
    big_inc_amount = 6
    def inc():
        nonlocal count
        count += 1

    def reset():
        nonlocal count
        count = 0
    

    def print_count():
        print(f"Current count = {count}")


    def big_inc():
        nonlocal count
        count  += big_inc_amount


    def change_big_inc_amount(amount):
        nonlocal big_inc_amount
        big_inc_amount = amount


    return {
        "inc": inc,
        "reset": reset,
        "print_count": print_count,
        "big_inc": big_inc,
        "change_big_inc_amount": change_big_inc_amount
    }
###############################333

print("#############################################")

c = create_counter_advanced()

c["inc"]()
c["inc"]()
c["inc"]()
c["inc"]()
c["inc"]()
c["print_count"]()
c["reset"]()
c["print_count"]()
c["big_inc"]()
c["big_inc"]()
c["big_inc"]()
c["print_count"]()
c["change_big_inc_amount"](30)
c["big_inc"]()
c["big_inc"]()
c["big_inc"]()
c["big_inc"]()
c["print_count"]()


