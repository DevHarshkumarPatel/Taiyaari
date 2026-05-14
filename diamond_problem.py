class Animal:
    def hello(self):
        print(f"Animal says hello!!")

class MotherDog(Animal):
    def hello(self):
        print(f"Cute.... Cute.....")
        super().hello()

class FatherDog(Animal):
    def hello(self):
        print(f"Bhaw... Bhaw....")
        super().hello()

class Puppy(MotherDog, FatherDog):
    def hello(self):
        print(f"Pue.... Pue...")
        super().hello()


p = Puppy()

p.hello()


"""
          Animal
            /\
           /  \
          /    \ 
    MotherDog  FatherDog
          \    /
           \  /
            \/
          Puppy
"""
