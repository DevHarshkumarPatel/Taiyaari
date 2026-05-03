class User:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print(f"Inside name property....")
        return self._name


u = User("Harsh")

print(u.name)

# I can read property only until I have not used setter and deleter method

try:

    u.name = "Swayam"

except AttributeError as error:
    print(f"Attribute Error Generated :: {error}")