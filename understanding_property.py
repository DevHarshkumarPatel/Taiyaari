class User:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print(f"Inside name property....")
        return self._name

    # setter method name should be same as the property name
    @name.setter
    def name(self, name):
        print(f"Inside setter method for name property....")
        self._name = name

    # deleter method name should be same as the property name
    @name.deleter
    def name(self):
        self._name = None


u = User("Harsh")

print(u.name)

# I can read property only until I have not used setter and deleter method

try:

    u.name = "Swayam"

    print(u.name)

except AttributeError as error:
    print(f"Attribute Error Generated :: {error}")

# now after defining the setter method for the property we can set the value of the property.
# but If I want to try to remove that property I can not until defining the deleter method.

del u.name

print(u.name)