#!/usr/bin/python
import helloext


print helloext.myfunc_noarg();

helloext.myfunc_witharg(10,"apple");
helloext.myfunc_witharg(100,"orange");
#helloext.myfunc_witharg(qty=100, item_desc="orange");
print helloext.myfunc_witharg_returnlist("milk");
print helloext.myfunc_witharg_returndict("spiderman");


# output #
# Hello, Python extensions - Function with No args
# Item Desc:       apple
# Total Quantity:  10
# Item Desc:       orange
# Total Quantity:  100
# Item Desc:       milk
# ('milk', 'full of sugar')
