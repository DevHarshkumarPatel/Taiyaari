def check_dict(d1, d2, d3):
    print(d1)
    print(d2)
    print(d3)


a = check_dict(d1=1,d2=3,d3=4)



def now_check_kwargs(**kwargs):
    print(f"kwargs :: {kwargs}")


b = now_check_kwargs(d1=34,d2=23,d3=45,d5=56)