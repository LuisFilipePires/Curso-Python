



#index  0123456789....
text = "Steve Jobs"

new_st = text[0] 
print(new_st)
#output: S

new_st = text[-1] # negative numbers gives the index by the end character in the string
print(new_st)
#output: s

st2 = text[-3]
print(st2)
#output: o


#start:end:step
#end index is excluded

st3 = text[1:4]
print(st3)
#output: tev

#[1:]  [:4] [-4:-2]


#step
st4 = text[0:10:1]
print(st4)

st5 = text[0:10:2]
print (st5)
#output: SeeJb

#step -1  invert the string
st6 = text[::-1]
print(st6)
#output: sboJ evetS


#Using slice object     #to take the product number
#            man-5   prod-?     co-3
inventory = '12346 AASDRttY45  LUX'
slice_object = slice(6, -4)
print(inventory[slice_object])

#output: AASDRttY45


inventory2 = "12324 FFRTd POR"
print(inventory2[slice_object])

#output: FFRTd


