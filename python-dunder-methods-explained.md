# 🐍 Python Dunder Methods Deep Dive (FAANG-Level)

## 📌 Topics Covered

* `__new__`
* `__init__`
* `__setattr__`
* `__getattribute__`
* `__getattr__`
* Class Variables vs Instance Variables

---

# 🧠 1. `__new__` (Object Creation)

## 🔹 What is it?

`__new__` is responsible for **creating the object (instance)**.

👉 It runs **before `__init__`**

---

## 🔹 Syntax

```python
class MyClass:
    def __new__(cls):
        instance = super().__new__(cls)
        return instance
```

---

## 🔹 Key Points

* First method called during object creation
* Must return an object
* Used for:

  * Singleton pattern
  * Immutable objects (int, str, tuple)

---

## 🔹 Example

```python
class Test:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")

t = Test()
```

### Output:

```
Creating object
Initializing object
```

---

## ⚠️ Important

If `__new__` does NOT return an object → `__init__` will NOT run

---

## 💼 Interview Insight

> “`__new__` controls object creation, which is why it's used in Singleton patterns.”

---

# 🧠 2. `__init__` (Object Initialization)

## 🔹 What is it?

Initializes the object after it is created.

---

## 🔹 Syntax

```python
class User:
    def __init__(self, name):
        self.name = name
```

---

## 🔹 Key Points

* Runs after `__new__`
* Cannot return anything (must return `None`)
* Used to assign attributes

---

## 🔹 Example

```python
u = User("Harsh")
print(u.name)  # Harsh
```

---

## 🧠 Analogy

* `__new__` → builds house 🏠
* `__init__` → furnishes house 🛋️

---

# 🧠 3. `__setattr__` (Setting Attributes)

## 🔹 What is it?

Called whenever you assign a value:

```python
obj.x = 10
```

Internally:

```python
obj.__setattr__("x", 10)
```

---

## 🔹 Example

```python
class Test:
    def __setattr__(self, key, value):
        print(f"Setting {key} = {value}")
        super().__setattr__(key, value)

t = Test()
t.x = 10
```

---

## ⚠️ Common Mistake

```python
def __setattr__(self, key, value):
    self.key = value   # ❌ infinite recursion
```

---

## ✅ Correct Way

```python
super().__setattr__(key, value)
```

---

## 🔥 Use Cases

* Validation (age > 0)
* Logging changes
* Immutable objects

---

# 🧠 4. `__getattribute__` (Accessing Attributes - ALWAYS)

## 🔹 What is it?

Called for **EVERY attribute access**

```python
obj.x → obj.__getattribute__("x")
```

---

## 🔹 Example

```python
class Test:
    def __getattribute__(self, name):
        print(f"Accessing: {name}")
        return super().__getattribute__(name)

t = Test()
t.x = 10
print(t.x)
```

---

## ⚠️ Dangerous

```python
def __getattribute__(self, name):
    return self.name   # ❌ infinite recursion
```

---

## ✅ Correct Way

```python
return super().__getattribute__(name)
```

---

## 🔥 Use Cases

* Logging access
* Security checks
* Proxy objects

---

# 🧠 5. `__getattr__` (Fallback for Missing Attributes)

## 🔹 What is it?

Called **ONLY when attribute is NOT found**

---

## 🔹 Example

```python
class Test:
    def __getattr__(self, name):
        return f"{name} not found"

t = Test()
print(t.x)
```

### Output:

```
x not found
```

---

## 🔥 Difference

| Method             | Called When       |
| ------------------ | ----------------- |
| `__getattribute__` | Always            |
| `__getattr__`      | Only if not found |

---

## 🔥 Use Cases

* Default values
* Lazy loading
* Dynamic attributes

---

# 🧠 6. Attribute Access Flow (VERY IMPORTANT)

When you do:

```python
obj.x
```

Python follows:

```
1. __getattribute__
2. instance __dict__
3. class
4. parent classes (MRO)
5. __getattr__ (if not found)
```

---

# 🧠 7. Class Variables vs Instance Variables

---

## 🔹 Instance Variables

Defined inside `__init__`

```python
class User:
    def __init__(self, name):
        self.name = name
```

👉 Each object has its own copy

---

## 🔹 Class Variables

Defined at class level

```python
class User:
    company = "Google"
```

👉 Shared across all objects

---

## 🔹 Example

```python
u1 = User("Harsh")
u2 = User("Amit")

print(u1.name)  # Harsh
print(u2.name)  # Amit

print(u1.company)  # Google
print(u2.company)  # Google
```

---

## ⚠️ Important Trap

```python
class Test:
    count = 0

t1 = Test()
t1.count = 5
```

Now:

```python
print(Test.count)  # 0
print(t1.count)    # 5
```

👉 You created an instance variable, not modified class variable

---

## 🔥 Key Difference

| Feature | Instance Variable | Class Variable |
| ------- | ----------------- | -------------- |
| Scope   | Per object        | Shared         |
| Memory  | Separate          | One copy       |
| Defined | Inside `__init__` | Inside class   |

---

# 🧠 8. Final Mental Model

---

## 🔁 Object Lifecycle

```
obj = MyClass()

1. __new__ → create object
2. __init__ → initialize
3. __setattr__ → assign values
4. __getattribute__ → access attribute
5. __getattr__ → fallback if missing
```

---

# 💼 Interview Summary (Must Remember)

👉 You should be able to say:

> “`__new__` creates the object, `__init__` initializes it. `__setattr__` intercepts attribute assignment, `__getattribute__` handles all attribute access, and `__getattr__` is a fallback for missing attributes. Class variables are shared across instances, while instance variables are unique per object.”

---

# 🚀 Pro Tips

* Always use `super()` in dunder methods to avoid recursion
* Avoid modifying state in `__str__` or access methods
* Be careful with `__getattribute__` (performance + recursion risk)
* Understand flow, not just syntax

---

# 🔥 Next Steps

* Learn `__hash__` + `__eq__`
* Learn operator overloading deeply
* Build real systems (LRU cache, ORM)

---

✨ You’re now moving toward **FAANG-level Python understanding**
