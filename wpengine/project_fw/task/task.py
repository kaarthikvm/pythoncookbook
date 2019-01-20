#!/usr/bin/python
import sys
import csv
import constant as c
import requests
from collections import OrderedDict

def debug_print ( args ):
    #print "#################################\n";
    print args;
    #print "\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n";

def get_account_status ( account_id ):
    debug_print("URL ==> " + c.URI + account_id);
    resp = requests.get(c.URI + account_id);
    resp.raise_for_status(); # raises exception for other than 200 status code
    debug_print("URL API response ==> " + str(resp.json())); 
    return resp.json();

def process_csv ( ifileName, ofileName ):
    ofdata = OrderedDict([('Account ID', None),
                           ('First Name', None),
                           ('Created On', None),
                           ('Status', None),
                           ('Status Set', None)]);
 
    with open( ifileName, 'rb') as rd_hdlr:
        csv_rdr = csv.DictReader(rd_hdlr, delimiter=',');
        # init csv file for writing
        with open(ofileName, 'wb') as wr_hdlr:
            csv_wr = csv.DictWriter(wr_hdlr, delimiter=',', fieldnames=ofdata)
            csv_wr.writeheader();
            for data in csv_rdr:
                debug_print("\nInput file content ==> " + str(data));
                resp = get_account_status(data['Account ID']);
                ofdata = {'Account ID': resp['account_id'],
                          'First Name': data['First Name'],
                          'Created On': str(resp['created_on']),
                          'Status': str(resp['status']),
                          'Status Set': 'On'};# if resp['status'] != None};
                debug_print("Output to csv file ==>  " + str(ofdata));
                csv_wr.writerow(ofdata); 

def main (input_file, output_file):
    try:
        process_csv(input_file, output_file); 
    except requests.exceptions.RequestException as e:
        debug_print("REST API exception \n %s" % (e));
        sys.exit(1);  
    except IOError as e:
        debug_print("I/O error({0}): {1}".format(e.errno, e.strerror));
    
if __name__ == "__main__":
    debug_print("Length of arguments  %d" % (len(sys.argv)));
    debug_print("List of arguments    %s" % (str(sys.argv)));
    if len(sys.argv) != c.COMMAND_LEN:
        debug_print("Command Usage task.py <input file path> <output file path>");
        sys.exit(1);
    main(sys.argv[1], sys.argv[2]);
