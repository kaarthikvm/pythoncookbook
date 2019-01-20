#!/usr/bin/python
import sys
import csv
import constant as c
import requests
from collections import OrderedDict

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
DEBUG_PRINT = debug_print


def get_account_status (account_id):
    """
       Construct URL
       Call REST API
       Fetch API response
    """
    DEBUG_PRINT("URL ==> " + c.URI + account_id);
    resp = requests.get(c.URI + account_id);
    resp.raise_for_status(); # raises exception for other than 200 status code
    DEBUG_PRINT("URL API response ==> " + str(resp.json())); 
    return resp.json();

def process_csv (ifileName, ofileName):
    """
       Read the input file
       Init output file 
       Write headers in output file
       Fetch information from input file
       Get status for each account id
       Construct data to be written to output file
    """
    with open( ifileName, 'rb') as rd_hdlr:
        csv_rdr = csv.DictReader(rd_hdlr, delimiter=',');
        # init csv file for writing
        with open(ofileName, 'wb') as wr_hdlr:
            csv_wr = csv.DictWriter(wr_hdlr, delimiter=',', fieldnames=OFDATA)
            # write header in output file
            csv_wr.writeheader();
            for data in csv_rdr:
                DEBUG_PRINT("\nInput file content ==> " + str(data));
                # get status for each account ID
                resp = get_account_status(data['Account ID']);
                write_data_csv(csv_wr, resp, data['First Name']);

def write_data_csv(csv_wr, jsonresp, name):
    """
        Construct response to be written to output file
    """
    OFDATA = {'Account ID': jsonresp['account_id'],
              'First Name': name,
              'Created On': str(jsonresp['created_on']),
              'Status': str(jsonresp['status']),
              'Status Set': 'On' if str(jsonresp['status']) is not None else 'Off'};
    DEBUG_PRINT("Output to csv file ==>  " + str(OFDATA));
    csv_wr.writerow(OFDATA); 
   
    

def main (input_file, output_file):
    """
        Entry point
    """
    try:
        process_csv(input_file, output_file);
    except requests.exceptions.RequestException as e:
        DEBUG_PRINT("REST API exception \n %s" % (e));
    except IOError as e:
        DEBUG_PRINT("I/O error({0}): {1}".format(e.errno, e.strerror));
    except BaseException as e:
        DEBUG_PRINT("Generic exception occured %s" % e);
    
if __name__ == "__main__":
    DEBUG_PRINT("Length of arguments  %d" % (len(sys.argv)));
    DEBUG_PRINT("List of arguments    %s" % (str(sys.argv)));
    if len(sys.argv) != c.COMMAND_LEN:
        DEBUG_PRINT("Command Usage task.py <input file path> <output file path>");
        sys.exit(1);
    main(sys.argv[1], sys.argv[2]);
