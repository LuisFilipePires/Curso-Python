# Print 😎😪

## 1️⃣ Using `sep` in the `print` function

- By **default**, `sep` is a space (`sep=" "`):

```python
print(1, 2, 3, 4, 5, 6, 7)
# Output: 1 2 3 4 5 6 7

You can change the separator using sep:

print(1, 2, 3, 4, 5, 6, 7, sep=",")
# Output: 1,2,3,4,5,6,7

2️⃣ Using end in the print function
By default, print() adds a newline at the end (\n).
You can change it using the end parameter:

print("Hello, how are you?")
print("Same line", end=" ")  # adds a space instead of newline
print("continuation")

Hello, how are you?
Same line continuation

#Explanation

By default, print() ends with a newline (\n).
When you change end, e.g. end=", ", the cursor stays on the same line.
The first print (output x, ) appears immediately, then Python waits 5 seconds.
After the sleep, the next print (then y!) continues on the same line.


# Force the first print to flush immediately
print("output x", end=", ", flush=True)  # 'flush=True' sends output directly to the terminal
time.sleep(5)  # pause 5 seconds to observe buffering effect
print("then y!")  # prints immediately after the pause, continuing on the same line



