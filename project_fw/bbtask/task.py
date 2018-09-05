""" Python module to generate sum of two numbers """
#!/usr/bin/python


def sum(a,b):
    print "value of a = %d      b = %d " % (a,b);
    if a == 100:
        return 100;
    if b == 200:
        return 200; 
    return a+b;

if __name__ == "__main__":
    print "sum = %d " %(sum(10,20));
    print "sum = %d " %(sum(100,20));
    print "sum = %d " %(sum(10,200));
