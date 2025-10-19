
#return a new string

text = "the best of the best"

replace_text = text.replace("best", "worst")
print("text: ", text)
print(replace_text)

#replace how many times needed
replace_times = text.replace("best", "worst", 1)
print(replace_times)


"""
output:

text:  the best of the best
the worst of the worst
the worst of the best
"""
