from float2 import *

print("subtraction")        
a=Float([9,2,7,7],1)
b=Float([2,3,4,5],1)
c=a-b
assert str(c)=="+693.2"
print("\nsubtraction") 
a=Float([9,2,7,7],1)
b=Float([2,3,4,5],1,"-")
c=a-b
assert str(c)=="+1162.2"
print("\nsubtraction") 
a=Float([9,2,7,7],1,"-")
b=Float([2,3,4,5],1)
c=a-b
assert str(c)=="-1162.2"
print("\nsubtraction")
a=Float([9,2,7,7],1,"-")
b=Float([2,3,4,5],1,"-")
c=a-b
assert str(c)=="-693.2"
assertFalse(str(c)=="-693.22")

