# 🏢 FAANG-Level Python Interview: Dunder Methods Deep Dive

> **Interviewer Mindset:** These questions are asked at Google, Meta, Amazon, Airbnb, Booking.com, and Qualcomm to test whether you *truly understand* Python internals — not just memorized syntax.

---

## 📋 Table of Contents

1. [__new__ Questions](#1-__new__-questions)
2. [__init__ Questions](#2-__init__-questions)
3. [__setattr__ Questions](#3-__setattr__-questions)
4. [__getattribute__ Questions](#4-__getattribute__-questions)
5. [__getattr__ Questions](#5-__getattr__-questions)
6. [Class vs Instance Variables](#6-class-vs-instance-variables)
7. [Combined / System Design Questions](#7-combined--system-design-questions)

---

## 1. `__new__` Questions

---

### ❓ Q1. What is `__new__` and how is it different from `__init__`?

**🎯 Why asked:** Tests if you understand Python's two-step object creation — creation vs initialization.

**✅ Answer (Simple):**

Think of building a house:
- `__new__` = **building the house** (creating the structure/memory)
- `__init__` = **furnishing the house** (putting stuff inside)

`__new__` runs **first** and **creates** the object.
`__init__` runs **second** and **fills** the object with data.

```python
class Dog:
    def __new__(cls):
        print("Step 1: Creating the Dog object in memory")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("Step 2: Setting dog's name and age")
        self.name = "Buddy"

d = Dog()
# Output:
# Step 1: Creating the Dog object in memory
# Step 2: Setting dog's name and age
```

**Key Rule:** If `__new__` does NOT return anything → `__init__` is **never called**.

```python
class Broken:
    def __new__(cls):
        print("Creating...")
        # forgot to return!

    def __init__(self):
        print("This NEVER runs!")

b = Broken()
# Output: Creating...
# __init__ is skipped because __new__ returned None
```

---

### ❓ Q2. How do you implement a Singleton using `__new__`?

**🎯 Why asked:** Tests real-world pattern usage. Singleton is a classic design pattern question at FAANG.

**✅ Answer (Simple):**

A **Singleton** means — no matter how many times you create an object, you always get the **same object** (one and only one).

Think of it like a **President** — only one can exist at a time.

```python
class DatabaseConnection:
    _instance = None  # stores the one and only object

    def __new__(cls):
        if cls._instance is None:
            print("Creating new DB connection...")
            cls._instance = super().__new__(cls)
        else:
            print("Returning existing DB connection!")
        return cls._instance

# Test it
db1 = DatabaseConnection()  # "Creating new DB connection..."
db2 = DatabaseConnection()  # "Returning existing DB connection!"

print(db1 is db2)  # True — same object!
print(id(db1) == id(db2))  # True — same memory address!
```

**Where is this used in real life?**
- Database connections (expensive to create repeatedly)
- Config managers (you want one source of truth)
- Logger (one logger for whole app)

---

### ❓ Q3. Why can't you create a Singleton using `__init__` instead of `__new__`?

**🎯 Why asked:** Tests depth of understanding — `__init__` vs `__new__` traps.

**✅ Answer (Simple):**

Because by the time `__init__` runs, a **new object is already created**. `__new__` is the only place where you can **control whether a new object is created or not**.

```python
# Wrong approach — won't work as Singleton
class BadSingleton:
    _instance = None

    def __init__(self):
        if BadSingleton._instance is not None:
            print("Already exists!")
            return  # This doesn't help — object is ALREADY created!
        BadSingleton._instance = self

b1 = BadSingleton()
b2 = BadSingleton()
print(b1 is b2)  # ❌ False — two different objects exist!
```

**Bottom Line:** `__new__` = gatekeeper (decides IF object is created). `__init__` = decorator (runs AFTER object already exists).

---

## 2. `__init__` Questions

---

### ❓ Q4. What happens if `__init__` returns a value?

**🎯 Why asked:** Common Python gotcha. Tests if you've read the docs or actually tried it.

**✅ Answer (Simple):**

`__init__` **must return `None`**. If you try to return something else, Python raises a `TypeError`.

```python
class Wrong:
    def __init__(self):
        return 42  # ❌ ILLEGAL!

w = Wrong()
# TypeError: __init__() should return None, not 'int'
```

**Why?** Because Python's object creation system already handles the return. `__new__` gives you the object. `__init__` just fills it. Python doesn't want you messing with the return chain.

```python
class Correct:
    def __init__(self, name):
        self.name = name
        # No return needed — Python handles it

c = Correct("Harsh")
print(c.name)  # Harsh
```

---

### ❓ Q5. Can `__init__` call another method that raises an exception? What happens to the object?

**🎯 Why asked:** Tests understanding of Python memory management and object lifecycle.

**✅ Answer (Simple):**

If `__init__` raises an exception, the **object is created** (by `__new__`) but **never assigned** to your variable. Python garbage collects it immediately.

```python
class User:
    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative!")
        self.age = age

try:
    u = User(-5)  # __new__ runs, creates object, __init__ raises error
except ValueError as e:
    print(e)  # "Age cannot be negative!"

# u is never assigned — object is garbage collected
```

**Real world use:** This is how you do **validation in constructors** — the standard pattern in Python.

---

## 3. `__setattr__` Questions

---

### ❓ Q6. What is `__setattr__` and when does it get called?

**🎯 Why asked:** Tests if you know that attribute assignment is not "magic" — it goes through a method.

**✅ Answer (Simple):**

Every time you write `obj.x = 10`, Python **secretly calls** `obj.__setattr__("x", 10)`.

It's like a **security checkpoint** — before any value is stored, it passes through `__setattr__`.

```python
class Employee:
    def __setattr__(self, key, value):
        print(f"📝 Logging: Setting '{key}' to '{value}'")
        super().__setattr__(key, value)  # actually store the value

e = Employee()
e.name = "Harsh"   # 📝 Logging: Setting 'name' to 'Harsh'
e.salary = 50000   # 📝 Logging: Setting 'salary' to '50000'
```

---

### ❓ Q7. What is the most common mistake in `__setattr__` and why does it cause infinite recursion?

**🎯 Why asked:** This is a trap question. Interviewers LOVE this. Shows real debugging experience.

**✅ Answer (Simple):**

The most common mistake is writing `self.key = value` inside `__setattr__`. This creates **infinite recursion** because:

`self.key = value` → calls `__setattr__` → which calls `self.key = value` → calls `__setattr__`... forever!

```python
# ❌ WRONG — infinite recursion
class Bad:
    def __setattr__(self, key, value):
        self.key = value  # This calls __setattr__ again! BOOM 💥

b = Bad()
b.x = 10  # RecursionError: maximum recursion depth exceeded
```

```python
# ✅ CORRECT — use super() to bypass the trap
class Good:
    def __setattr__(self, key, value):
        super().__setattr__(key, value)  # Goes to object.__setattr__ directly

g = Good()
g.x = 10  # Works perfectly!
print(g.x)  # 10
```

**Why `super()` works:** `super().__setattr__` calls Python's built-in C-level setter that directly modifies `__dict__` without calling your `__setattr__` again.

---

### ❓ Q8. How would you use `__setattr__` to create a class where age must always be positive?

**🎯 Why asked:** Real-world validation use case — shows you can apply dunder methods practically.

**✅ Answer (Simple):**

```python
class Person:
    def __setattr__(self, key, value):
        if key == "age":
            if not isinstance(value, int):
                raise TypeError("Age must be an integer!")
            if value < 0:
                raise ValueError("Age cannot be negative!")
            if value > 150:
                raise ValueError("Age is unrealistically high!")
        
        super().__setattr__(key, value)  # Store if valid

p = Person()
p.name = "Harsh"   # Works fine
p.age = 25         # Works fine
p.age = -5         # ❌ ValueError: Age cannot be negative!
p.age = "hello"    # ❌ TypeError: Age must be an integer!
```

**Where this is used:** ORM frameworks like Django use this internally to validate model fields before saving to a database.

---

## 4. `__getattribute__` Questions

---

### ❓ Q9. What is `__getattribute__` and how is it different from `__getattr__`?

**🎯 Why asked:** The single most confusing dunder pair. FAANG interviewers use this to filter candidates.

**✅ Answer (Simple):**

| Method | Called When |
|--------|------------|
| `__getattribute__` | **ALWAYS** — every single time you access any attribute |
| `__getattr__` | **ONLY** when attribute is NOT found anywhere |

Think of it like airport security:
- `__getattribute__` = The **main gate** everyone passes through (every passenger)
- `__getattr__` = The **lost luggage counter** (only when something is missing)

```python
class Demo:
    def __init__(self):
        self.x = 10

    def __getattribute__(self, name):
        print(f"🔍 __getattribute__ called for: {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"❓ __getattr__ called — '{name}' not found!")
        return "DEFAULT"

d = Demo()
print(d.x)   # __getattribute__ called ✅, returns 10
print(d.y)   # __getattribute__ called, fails → __getattr__ called, returns "DEFAULT"
```

---

### ❓ Q10. What is the recursion trap in `__getattribute__` and how do you avoid it?

**🎯 Why asked:** Shows you understand the danger of overriding Python's most fundamental method.

**✅ Answer (Simple):**

```python
# ❌ WRONG — infinite recursion
class Dangerous:
    def __getattribute__(self, name):
        return self.name  # self.name calls __getattribute__ again! 💥

d = Dangerous()
d.anything  # RecursionError!
```

Every time you access `self.anything`, Python calls `__getattribute__`. Inside that method, `self.name` calls `__getattribute__` again. It never stops!

```python
# ✅ CORRECT — use super()
class Safe:
    def __getattribute__(self, name):
        print(f"Accessing: {name}")
        return super().__getattribute__(name)  # Goes to C-level, no recursion

s = Safe()
s.x = 5
print(s.x)  # Accessing: x → 5
```

**Why `super()` is safe:** It calls Python's C-level `object.__getattribute__` which reads from `__dict__` directly without calling your Python-level `__getattribute__` again.

---
