import sys
import ctypes


# Python memory addresses
test = 10

print("The memory address of the Test variable is: ", id(test))
print("The memory address (in HEX) of the Test variable is: ", hex(id(test)))

# Now let's update the value
test = 100
print("The memory address of the Test variable is: ", id(test))
print("The memory address (in HEX) of the Test variable is: ", hex(id(test)))

# References Memory
var_x = 2000
var_y = var_x
print(var_y is var_x)


var_a = 1000
var_b = 1000
print(var_a is var_b)

var_c = "Hello"
var_d = "Hello"
print(var_c is var_d)

"""
Create Python object(1000)
Assign the name x to that object
Create Python object (300)
Create Python object (700)
Add these two objects together
Create a new Python object (1000)
Assign the name y to that object
"""
var_e = 1000
var_f = 300 + 700
print(var_e is var_f)

# Find the reference count
var_h = [1, 2, 3]
print(sys.getrefcount(var_h))
print(ctypes.c_long.from_address(id(var_h)).value)
var_h_address = id(var_h)
var_h = None
print(ctypes.c_long.from_address(var_h_address).value)

# Everything is an object
isinstance(1, object)
isinstance(list(), object)
isinstance(True, object)

def foo():
    pass

isinstance(foo, object)
