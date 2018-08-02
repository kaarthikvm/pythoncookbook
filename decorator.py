#!/usr//bin/python


def filtercoffee(original):
    def wrapper():
        original();
        print " Nature  : Fitler coffee";
    return wrapper; 



def instantcoffee(original):
    def wrapper():
        original();
        print " Nature  : Instant coffee";
    return wrapper; 

@filtercoffee
@instantcoffee
def shop():
    print "coffee shop";




def orangefruit(original):
    def wrapper(x):
        original(x);
        print " Type  : Orange Fruit value is Rs %d" % x;
    return wrapper; 



def applefruit(original):
    def wrapper(x):
        original(x);
        print " Nature  : Apple Fruit  value is Rs %d" %x;
    return wrapper; 

@orangefruit
@applefruit
def fruit(value):
    print "fruit shop";



 

if __name__ == "__main__":
    shop();
    fruit(400);
