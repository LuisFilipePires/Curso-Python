


# 🧠 Type Casting in Python

**Type casting** means converting a value from one data type to another.  
In Python, there are two types of type casting:

---

## 🔹 1. Implicit Type Conversion

Python **automatically converts** one data type to another **during execution**, when it’s safe to do so (i.e., no data loss).

### ✅ Example
```python
num_int = 10       # int
num_float = 3.5    # float

result = num_int + num_float
print(result)        # 13.5
print(type(result))  # <class 'float'>

Explanation:
Python automatically converts num_int (an integer) into a float before
performing the addition, so the final result is a float.

##🔸 2. Explicit Type Conversion (Type Casting)

Also known as manual type conversion, this happens when the programmer explicitly
converts one data type into another using built-in functions.

🧩 Common Functions
Function	Description
int()	Converts to integer
float()	Converts to floating-point number
str()	Converts to string
bool()	Converts to boolean value

# Convert float to int
num_float = 7.8
num_int = int(num_float)
print(num_int)        # 7
print(type(num_int))  # <class 'int'>

# Convert string to int
num_str = "42"
num_int = int(num_str)
print(num_int + 10)   # 52

# Convert int to string
num = 100
text = str(num)
print("The value is " + text)
