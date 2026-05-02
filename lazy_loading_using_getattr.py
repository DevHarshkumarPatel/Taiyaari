class LazyLoadUsingGetattr:

    def __init__(self):
        self._loaders = {
            "database" : self.database_loader,
            "ml_load" : self.ml_load
        }

    def database_loader(self):
        print(f"Database Loading.....")
        return list(range(1_00_00_00))

    def ml_load(self):
        print(f"Ml Model is loading")
        return "ML MODEL"


    def __getattr__(self, name):
        
        if name in self._loaders:
            value = self._loaders[name]()

            setattr(self, name, value)

            return value
        
        raise AttributeError(f"{name} not found!!")

import time

st = time.time()
a = LazyLoadUsingGetattr()
print(f"1. Checkpoint :: {time.time()-st}")

st = time.time()
a.database   # ✅ triggers lazy loading
print(f"2. Checkpoint :: {time.time()-st}")

st = time.time()
a.database   # ✅ cached → instant
print(f"3. Checkpoint :: {time.time()-st}")