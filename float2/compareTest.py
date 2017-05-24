from float2 import *
print("\ncomparing")

a=Float([9,2,7,7,2],2,"-")
b=Float([2,3,1,4],1)
                
a.absolute().display()
assert b>a
assert a.absolute()>b.absolute()
assertFalse(a>b)


a=Float([1,2,3],1)
b=Float([1,2,3],2)
assert a>=b
assertFalse(b>=a)

