lst = [10, 20, 30]

print(f"lst :: {lst}")

print(f"*lst ::",*lst)

def test(**data):
    print(data)


kw = {

    "name" : "Harsh",
    "age" : 26
}

test(data = kw)