class Flyable:
    def fly(self):
        print(f"I can Fly")

class Swimmable:
    def swim(self):
        print("I can Swim")


class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack ... Quack...")

d = Duck()
d.quack()
d.fly()
d.swim()

# this is multilevl inheritance and we are using this type of inheritance in Mixin classes