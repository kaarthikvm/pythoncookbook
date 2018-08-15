#!/usr/bin/python
# ref : https://www.python-course.eu

class base(object):

    def __init__(self, arg):
        print "base class constructor";
        self.count = arg; # this method invokes setter method

    def display(self):
        print "base class display %d " % self.count; # this invokes getter method

    # to do opertions on public attribute, property method can be used
    @property
    def count(self):
        return self.__count;
    @count.setter
    def count(self,value):
        if value < 100:
           self.__count = 999;
        else:
           self.__count = value; 
		
if __name__ == "__main__":

    b1 = base(333);
    b1.display();
    b1.count = 20;
    print b1.count;
    b1.count = 222;
    print b1.count;
    


