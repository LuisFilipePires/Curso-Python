
#variadict functions

def arbitrary(*args):
	print(args)
	print(type(args))

arbitrary(1,2,3)  #(1, 2, 3) #<class 'tuple'>
'''
(1, 2, 3)
<class 'tuple'>
'''   
 

def arbitrary1(x,*args,y):
	print(args)
	print(type(args))
	print("x: ", x)
	print("args[0]: ", args[0])
	print("args[1]: ", args[1])
	print("y: ", y)
	
arbitrary1(1,2,3,y=4)
'''
<class 'tuple'>
x:  1
args[0]:  2
args[1]:  3
y:  4
''' 



def arbitrary2(x,*args,y):
	print(args)
	print(type(args))
	print("x: ", x)
	print("args[0]: ", args[0])
	print("args[1]: ", args[1])
	print("y: ", y)
	
arbitrary2(1,2,3,y=4)



#kwargs   set to K = keys  w = words   arguments    -> dictionaire
def arbitrary3 (**kwargs):
	print("type **kwargs: ", type(kwargs))
	print("First name: ", kwargs["fname"])
	print("age: ", kwargs["age"])
	

arbitrary3 (fname = "Joel", age = 23)
'''
type **kwargs:  <class 'dict'>
First name:  Joel
age:  23

'''


def arbitrary3 (x, *args,**kwargs):
	print("x: ", x)
	print("args[0]: ", args[0])
	print("args[1]: ", args[1])
	print("type **kwargs: ", type(kwargs))
	print("First name: ", kwargs["fname"])
	print("age: ", kwargs["age"])
	

arbitrary3 (100,20,33,fname = "Joel", age = 23)
