
### What does the `divmod()` function return in Python?

The `divmod(a, b)` function in Python returns **a tuple containing two values**:

1. **The quotient of the integer division `a // b`**
2. **The remainder of the division `a % b`**

In other words:
divmod(a, b) == (a // b, a % b)

result = divmod(10, 3)
print(result)

Output:
(3, 1)

##This happens because:

10 // 3 → 3 (quotient)

10 % 3 → 1 (remainder)

So, divmod(10, 3) returns the tuple (3, 1).

Summary
Expression	Meaning	Result
a // b	Quotient	3
a % b	Remainder	1
divmod(a, b)	Tuple result	(3, 1)

The divmod() function is a convenient way to obtain both the quotient and the remainder at the same time.
