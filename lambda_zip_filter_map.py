#!/usr/bin/python

# lambda function - anonymous function which provides function object as value
# always single line function
# it has only return statement
func_obj = lambda x,y,z: x+y+z;
print func_obj(1,2,3);


# map function 
def func(x,y):
   return x+y;
#   if x < 10:
#     return x+1;
#   elif y >=10:
#     return y+1;
#   return 999;
print map(func, [1,2,3,4,5,6,7,8],[10,20,30,40,50,60,70,80]);

# filter acts on true or false/None
def func2(x):
   if (x >= 3):
     return True;
   else:
     return None; # return False
     # if True, then all elements will be printed 

print filter(func2,[1,2,3,4]);


print zip([1,2],[3,4]);
