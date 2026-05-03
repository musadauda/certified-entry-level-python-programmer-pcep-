def calculate(operation, *args):
    if operation.lower() == "add":
        total = 0
        for num in args:
            total += num
            return total
        
    elif operation.lower() == "multiply":
        total = 1
        for num in args[1:]:
            total *= num
            return total
        
    elif operation.lower() == "subtract":
        total = args[0]
        for num in args[1:]:
            total -= num
            return total
        
    elif operation.lower() == "divide":
        total = args[0]
        for num in args[1:]:
            total /= num
            return total
        
    else:
        return "Invalid operation"
    

print(calculate("add", 1, 2, 3, 4, 5))
print(calculate("multiply", 1, 2,5,6,7,3,5,64,6))
print(calculate("subtract", 10, 5,568,8,3,65,2))
print(calculate("divide", 87, 2,1,6,4,6,3,2))


def pr(message, **data):
    extra_data = [f"{key}={value}" for key, value in data.items()]
    extra_data_str = ",".join(extra_data)
    print(f"{message} - {extra_data_str}")


print(pr("Hello World", username= "Musa Dauda", password = "12345"))

print(pr("Unpacking with **", **{"username": "Musa Dauda", "password": "12345"}))



def add(**kwargs):
    default_args = {"a": 1, "b": 2, "c": 3}
    args = default_args | kwargs # '|' ==> Merged with
    return args["a"] + args["b"] + args["c"]


print(add(a=10, b=20, c=30))
print(add(b=20, c=30))
print(add())




