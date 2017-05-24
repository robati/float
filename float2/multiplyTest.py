from float2 import *
print("multiply")
a=Float([9,2,7,7,2],2,"-")
b=Float([2,3,1,4],1)
            
c=a*b
assert str(c)=="-214674.408"

print("multiply")
a=Float([2,6,4,5],3,"-")
b=Float([1,2,8,4,5,8],2,"-")
            
c=a*b
assert str(c)=="+03397.71410"
assertFalse(str(c)=="-03397.71410")

