# Scope in Python
# The LEGB RULE
# Local - names assigned within a  function or lambda
# Enclosing - Names in the local scope of any enclosing functions
# Global - names assigned at top level or declared global
# Built-in - Nmaes preinstalled in python e.g len, print, ValueError



x = "Global"

def define_x():
    x = "Local"
    print(x)
    def nested():
        x = "Nested"
        print(x)
    nested()

print(x)

define_x()
print(x)

test = "global"

def myfunc():
    t = "local"

    print(test) #Python looks in L then E and finds in G
    print(t) # finds in L

myfunc()

#Global keyword - modify a global value from a function

count = 0

def increment():
    global count
    count += 1

    print(count)

increment()

# Enclosing - nonlocal scope - when nested function, inner can read from outer but cant modify unless using nonlocal

def outer_func():
    msg = "Hello"

    def inner_func():
        nonlocal msg
        print(msg)
        msg = "Hi"
        print(f"Inner {msg}")
    inner_func()
    print(f"Outer {msg}")


outer_func()