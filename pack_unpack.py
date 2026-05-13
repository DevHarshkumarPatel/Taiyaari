lst = [10, 20, 30]

print(f"lst :: {lst}")

print(f"*lst ::",*lst)

def test(**abc):
    print(abc)

test(abc = "kw")