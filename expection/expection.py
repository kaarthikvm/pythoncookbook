#!/usr/bin/python

# if no expection handling is used then traceback (kind of core) is created
# if we use exception, then all other codes arfe executed
# BaseException is base class and it captures all exception rather speciufic exception
# always make variable to None after excpetion processing (good design practice)

def func(x,y):
    z=x/y
    print "statement after raise"
    return z # this statement cannaot be executed if exception occurs

def a():
    # raise a # summa oru exception...it says exception has to be derived from BAseException and not a function
    print "calling another func"
    raise StopIteration # if this is not captured using try block then traceback will be generated

if __name__ == '__main__':
    try:     
       func(22,10)
    except BaseException as e:
          print str(e)
          print repr(e)
    except StopIteration as i:
          print "Inside except Stop iteration"
          print   i
    print "Calling second function"
    try: 
        a()
    except StopIteration as i:
        print "Inside except Stop iteration"
    except BaseException as e:
        print "Base Exception"
        print str(e)   
        print i
    else:
        print "No exception is called"    


print __file__
#help(int)
#help(AssertionError)
# any class can be viewed using help function

try: 
    with open("a.txt",mode='r') as f:
        f.read()

except IOError as e:
    print e
