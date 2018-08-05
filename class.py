#!/usr/bin/python

class base(object):
    def __init__(self):
        self.a=100; # No use since __getattribute__ takes control
        self.b=200; # No use since __getattribute__ takes control
        self.c=300; # No use since __getattribute__ takes control
        print "base class constructor";
    def __getattr__(self,name):
        print "request for %s" % name;

    def __getattribute__(self,name): # it supercedes __getattr__. Hence this will be called for all
        print "invoke for present/absence of attributr. Request for %s" % name;
        # return self.a; # recursion occurs
        if name == "a":
           return 100;
        elif name == "b":
           return 200;
        elif name == "c":
           return 300;

if __name__ == "__main__":
    o = base();
    print getattr(o,"a");
    print o.b;
    print getattr(o,"c");
    
