

# use   \   in new line of continuous code
#even a space after \ cause error

john_grade = 97
fil_grade = 98
Luis_grade = 99

sum_grades = john_grade + fil_grade + \
Luis_grade

print(sum_grades)

#other statement is using  (   )

Mary_grade = 78
Barkley_grade = 88
Newbird_grade = 79

sum_new_grades = (Mary_grade + Barkley_grade + 
					Newbird_grade)

print(sum_new_grades)


numbers = [4,
			5,
			7,
			2]

student = {"name" : "john",
			"age" : 19
			}
			
			
text1 = "A string \
across multiple lines"
print(text1)


text2 = """Another string
across multiples lines"""
#in here the new line character is still in the string

print(text2)
