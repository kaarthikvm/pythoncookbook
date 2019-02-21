#!/usr/bin/python

# note: yield inside function only
# when yield is used, function becomes generator and first time
# when it is called, it gives object
# It wont run the code first time eg: o=f()
# when next(o) or list(o) is called, it executes the code and process it
# YIELD is like a return and never stores the value eg: r= yield 10 
# always r is NONE

def f():
    print("  hello world");
    for i in range(10):
        yield i;
        r=2+i;
        print r;
o=  f();
print( next(o));
print( next(o));
print( next(o));


class base():
    def display(self):
        print "base class display";
        yield 2

class d(base):
   def __init__(self):
       print "const";
   def process(self):
       yield self.display();
m=d();
t=m.process();
print t;
print next(next(t));
