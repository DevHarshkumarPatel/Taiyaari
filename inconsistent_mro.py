class A:
    pass

class B(A):
    pass


class C(A,B):
    pass


# here Rule is Parent can be Inherited After Child only. So class C(B,A) this is right and this will generate Type Error

"""
Traceback (most recent call last):
  File "/workspaces/Taiyaari/inconsistent_mro.py", line 8, in <module>
    class C(A,B):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B
"""