""" Test code to explain in interview """
#!/usr/bin/python


class base(object):
     def __init__(self):
          pass;

     def __setattr__(self, name, value):
         print "Inside setattr";
         #self.name = value;
         return object.__setattr__(self, name, value);
 
     def __getattribute__(self, name):
         #return self.name;
         return object.__getattribute__(self, name);



for i in range(1,999999999):
    if (i== 999999999):
       print i;

if __name__ == "__main__":
    i = base();
    i.cat = 100;
    print i.cat;
