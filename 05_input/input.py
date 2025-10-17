print("Enter your name")
 
name = input("Name :")
print ("Hello ", name)

age = input("age: ")
print ("your age: ", age, "years old")

#input() returns a string

#next_year = age + 1 #error
age_number = int (age)
next_year = age_number + 1
print ("next year you'll be: ", next_year, "years old")


price = float(input("price:"))
after_taxes = price * 1.10
print ("price after taxes = ", after_taxes)
