#!/usr/bin/python


def hello( arg ):
    print "hello " + arg ;

# argument is function
def hello_wrapper( func ):
    print "hello wrapper";
    temp = "world";
    func(temp);

hello_wrapper(hello);

# alias or variable assignment
hello_var = hello_wrapper;
hello_var(hello);

# function inside function
def hello_wrapper_nested_func(func):
    print "hello wrapper nested func";
    temp = "input 1";
    def nested_func():
        func(temp);
    return nested_func;

func_obj = hello_wrapper_nested_func(hello);
print "\n \n";
func_obj(); # this is equivalent to decorator
