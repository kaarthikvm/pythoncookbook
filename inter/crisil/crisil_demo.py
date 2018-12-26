#!/usr/bin/python
from crisil_module import display;

# Question 1: value of price 
# Answer : 200
def myfunc():
     def get_price():
         price = 100;
     price = 200;
     get_price(); 
     return price;

a = myfunc();
print a;


# Question 2: Function overloading. 
# Answer : It does not work since only last function overwrites previous one.Cannot perfrom name mangling

class base():
    def __init__(self):
        print " constructor ";
  
    def display(self, a, b):
        print a,b;
    
    def display(self, a, b, c):
        print a,b,c;
    

obj = base();
#obj.display(100,200); # It does not work and produce exception
obj.display(100,200,300);


# Question 3: Imported function method and local function method has same name. Which one it will take
# Answer : local function will overtakes gloabl function
def display():
    print "local display method";

display();



# Question 4: Inheritance
# Answer : Hierarchy is followed. Hence method in derived class overwrides base class
#          If there is no method in derived class than base class method will be called
class A1():
    pass;
class B1():
    pass;
class C1():
     pass;

class A(A1):
   def get_price(self):
      print " A method";

class B(B1):
   def get_price(self):
      print " B method";

class C(C1):
   def get_price(self):
      print " C method";

inst = B();
inst.get_price();
