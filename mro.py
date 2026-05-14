class Animal:
    def hello(self):
        print(f"Hello From Animal!!")


class Dog(Animal):
    def hello(self):
        print(f"Bhaw Bhaw...")
        super().hello()


class Puppy(Dog):
    def hello(self):
        print(f"Pue.. Pue...")
        super().hello()



p = Puppy()

help(p)

# using class' object we can not call __mro__ it will generate attribute error
"""
Traceback (most recent call last):
  File "/workspaces/Taiyaari/mro.py", line 23, in <module>
    print(p.__mro__)
          ^^^^^^^^^
AttributeError: 'Puppy' object has no attribute '__mro__'
"""

print(Puppy.__mro__)

print([
    cls_name.__name__
    for cls_name in Puppy.__mro__
])

p.hello()
