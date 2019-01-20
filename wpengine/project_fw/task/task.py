#!/usr/bin/python
import sys
import csv
import constant as c
import requests

def debug_print ( args ):
    #print "#################################\n";
    print args;
    #print "\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n";

def get_account_status ( account_id ):
    debug_print(c.URI + account_id);
    resp = requests.get(c.URI + account_id);
    resp.raise_for_status(); # raises exception for other than 200 status code
    debug_print("API response ==> " + str(resp.json())); 

def read_csv ( fileName ):
    with open( fileName, 'rb') as rd_hdlr:
        #csv_rdr = csv.reader(rd_hdlr, delimiter=',');
        csv_rdr = csv.DictReader(rd_hdlr);#, delimiter=',');
        count = 0;
        for row in csv_rdr:
            #debug_print(row);
            #if count == 0:
                # column header
            #    count += 1;
            #    continue; 
            get_account_status(row['Account ID']);


def write_csv ( fileName ):
    pass

def main (input_file, output_file):
    try:
        read_csv(input_file);
        write_csv(output_file); 
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
