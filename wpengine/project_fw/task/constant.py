""" Global constants """
#!/usr/bin/python
from collections import OrderedDict

COMMAND_LEN = 3
URI = 'http://interview.wpengine.io/v1/accounts/'

# global dictionary to hold final data to be written to output file
OFDATA = OrderedDict([('Account ID', None),
                     ('First Name', None),
                     ('Created On', None),
                     ('Status', None),
                     ('Status Set', None)]);
 
