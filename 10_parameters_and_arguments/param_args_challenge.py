# Extend add to calculate("add", *args)
# custom print function say pr("message", **kwargs, eg ip address, location)
# implement default arguments without using regular syntax

def calculate(operation, *args):
    if operation.lower() == "add":
        return sum(args)
    
    elif operation.lower() == "multiply":
        return args[0] * args[1]
    
    elif operation.lower() == "subtract":
        return args[0] - args[1]
    
    elif operation.lower() == "divide":
        return args[0] / args[1]
    
    else:
        return "Invalid operation"
    

print(calculate("add", 1, 2, 3, 4, 5))
print(calculate("multiply", 1, 2))
print(calculate("subtract", 10, 5))
print(calculate("divide", 10, 2))


def pr(message, **kwargs):
    print(f"{message} from {kwargs} ")



print(pr("Hello World", username= "Musa Dauda", password = "12345"))