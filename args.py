def addition(a,b):
    return a + b

a = addition(10,15)

print(a)

# b = addition(10,14,12)

"""

Generates Error 

Traceback (most recent call last):
  File "/workspaces/Taiyaari/args.py", line 8, in <module>
    b = addition(10,14,12)
        ^^^^^^^^^^^^^^^^^^
TypeError: addition() takes 2 positional arguments but 3 were given


Now if we want that kind of function that will accept any number of arguments and add those all numbers without changing any functions definition

"""


