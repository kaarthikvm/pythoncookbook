#!/usr/bin/python

l = [10,"orange"];
v = [2, "carrot"];
s = [3, "lux"];

# print l; # donot use print globally. During import, this will be executed.

d = { "fruits":l,
      "vege":v,
      "soap":s};

# print d;

def printlist (d):
    """ print grocery list """
    for k in d:
        if k == "soap":
           continue; 
        print k;
        print d[k];
    return "success" # default return value is None
    
if __name__ == "__main__":
    printlist(d);
