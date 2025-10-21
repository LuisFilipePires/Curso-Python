
def operations(x, y):
	summ = x + y
	diff = x - y
	product = x * y
	return (summ, diff, product)

total, diff, prod = operations(50, 20)
print("total: ", total)
print("diff: ", diff)
print("prod: ", prod)

r = operations(40, 20)
print("r: ", r)
print("type(r): ", type(r))

"""
total:  70
diff:  30
prod:  1000
r:  (60, 20, 800)
type(r):  <class 'tuple'>
"""
