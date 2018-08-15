#!/usr/bin/python

def PRINT(arg):
    print arg;
    pass;

class base(object):
    def __init__(self,a=None):
        print "base class constructor";
    def display(self):
        print "base class display"
    def __str__(self):
        print "base class string representation"
        return "base string";
    def __repr__(self):
        print "base class representation"
        return "base representation";  
		
		
		
class derived(base):
    def __init__(self,a=None):
        print "derived class constructor";
        base.__init__(self,a);

    def display(self): # overriding method
        print "derived class display"
        base.display(self); 

    def __str__(self): # overriding method else call base class  __str__
        print "derived class string representation"	
        base.__str__(self); # return value from base is not handled
        return "derived string";

    def __repr__(self): # invokes when __str__ method is not present. It is also overiding base class method
        print "derived class representation";
        return "derived representation";  


		
if __name__ == "__main__":

    b1 = base();
    d1 = derived();
    b1.display();
    d1.display();
    PRINT(b1);
    PRINT(d1);
    PRINT(eval ("1+2"));
    PRINT(eval("b1")); # always __str__ is given high priority than __repr__
    PRINT(eval("d1")); # always __str__ is given high priority than __repr__


