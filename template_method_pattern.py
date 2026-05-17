from abc import ABC, abstractmethod

class IndianBread(ABC):
    def make_bread(self):
        self.prepare_dough()
        self.roll_the_dough()
        self.cook_on_tawa()
        self.serve()

        print(f"Bread is Yummy!!\n")


    def roll_the_dough(self):
        print(f"Rolling the dough")


    def serve(self):
        print(f"Serving the Bread with Pickle...")

    @abstractmethod
    def prepare_dough(self):
        pass

    @abstractmethod
    def cook_on_tawa(self):
        pass


class Roti(IndianBread):
    def prepare_dough(self):
        print(f"Prepare Dough with Wheat...")

    def cook_on_tawa(self):
        print(f"Cook the Roti on Tawa...")




class Paratha(IndianBread):
    def prepare_dough(self):
        print(f"Preparing the Dough with Oil...")

    def cook_on_tawa(self):
        print(f"Cooking Paratha with Ghee...")


class Thepla(IndianBread):

    def prepare_dough(self):
        print(f"Preparing the Dough with Methi and Masala")


    def cook_on_tawa(self):
        print(f"Cooking Thepla on Tawa with low flame...")



r = Roti()

r.make_bread()

p = Paratha()

p.make_bread()

t = Thepla()

t.make_bread()