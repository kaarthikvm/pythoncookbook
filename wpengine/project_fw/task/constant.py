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

def debug_print (args):
    """
        Debug function - to assist development
        For production purpose, use logging framework
        provided in python to filter logs like DEBUG, INFO, DETAIL etc
    """
    print args;
    pass;
 
