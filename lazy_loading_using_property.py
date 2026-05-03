class LazyLoadingUsingProperty:
    
    def __init__(self):
        self._database = None

    @property
    def database(self):
        if self._database is None:
            print(f"Setting Database...")

            self._database = list(range(1_00_000))

        return self._database


import time

st = time.time()
l1 = LazyLoadingUsingProperty()
print(f"1. Checkpoint {time.time() - st}")

st = time.time()
l1.database
print(f"2. Checkpoint {time.time() - st}")

st = time.time()
l1.database
print(f"3. Checkpoint {time.time() - st}")