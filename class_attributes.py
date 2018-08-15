#!/usr/bin/python

def PRINT(arg):
    print arg;
    pass;

class base(object):
    b=200;
    c=777;
    def __init__(self,a=None):
        self.a=a;
        self.b=300;
        print "base class constructor";
    def display(self):
        print "base class display =  %d" % self.a;
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

    b1 = base(100);
    b1.display();
    print b1.a;
    print b1.__dict__;
    print base.__dict__;
    print b1.b; # if b is not present at instance level, it goes to take the value from Class level
    print base.b; # it always takes value from  class level

    d1 = derived(999);
    print d1.a; # value will be 999. 
    print d1.__dict__;
    print derived.__dict__;
    print d1.b; # value will be taken from base
    print d1.c; # not present at instance level. Hence taken from class level
    print derived.c;
    print derived.b; # value will be taken from base
    print d1.z;

# notes:

# Always see the value present at instance level. If not go to class level.
# In case of derived, if __init__ of base is called, order of checking is
# derived instance level
# base instance level
# derived class level
# base class level

