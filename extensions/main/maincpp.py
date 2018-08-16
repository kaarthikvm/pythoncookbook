#!/usr/bin/python
import hellocppext


print hellocppext.myfunc_noarg();

hellocppext.myfunc_witharg(10,"apple");
hellocppext.myfunc_witharg(100,"orange");
#hellocppext.myfunc_witharg(qty=100, item_desc="orange");
print hellocppext.myfunc_witharg_returnlist("milk");
print hellocppext.myfunc_witharg_returndict("spiderman");


# output #
# Hello, Python extensions - Function with No args
# Item Desc:       apple
# Total Quantity:  10
# Item Desc:       orange
# Total Quantity:  100
# Item Desc:       milk
# ('milk', 'full of sugar')
