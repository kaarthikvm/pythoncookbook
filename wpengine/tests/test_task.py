import unittest
import csv
import requests
from task.task import task_main as tm;
from task.task import get_account_status as gas


class TestSum(unittest.TestCase):

    def test_no_of_rows(self):
        """
           check input file total elements == output file total elements 
        """
        tm("../data/input.csv","../output.csv");
        # input file rows == output file rows
        rlen, wlen= 0,0; 
        with open("../data/input.csv","r") as rd,open("../output.csv","r") as wr:
             
            csv_rdr = csv.DictReader(rd, delimiter=',');
            for data in csv_rdr:
                rlen +=1;
            csv_wr = csv.DictReader(wr, delimiter=',');
            for data in csv_wr:
                wlen +=1;
        
        self.assertEqual(rlen,7)
        self.assertEqual(wlen,7)
        self.assertEqual(rlen,wlen)


    def test_ok_account_id(self):
        """
           check input file account id == output file account id 
        """
        tm("../data/input.csv","../output.csv");
        with open("../data/input.csv","r") as rd,open("../output.csv","r") as wr:
            csv_rdr = csv.DictReader(rd, delimiter=',');
            csv_wr =  csv.DictReader(wr, delimiter=',');
            
            self.assertEqual(0,cmp([ rdata['Account ID'] for rdata in csv_rdr],
                                   [ wdata['Account ID'] for wdata in csv_wr]));
           

    def test_ok_first_name(self):
        """
           check input file first name == output file first name id 
        """
        tm("../data/input.csv","../output.csv");
        with open("../data/input.csv","r") as rd,open("../output.csv","r") as wr:
            csv_rdr = csv.DictReader(rd, delimiter=',');
            csv_wr =  csv.DictReader(wr, delimiter=',');
            
            self.assertEqual(0,cmp([ rdata['First Name'] for rdata in csv_rdr],
                                   [ wdata['First Name'] for wdata in csv_wr]));
 

    def test_failure_rest_api(self):
        """
            check rest api is not working 
        """
        try:
            gas("123445");
        except requests.exceptions.RequestException as e:
            self.assertEqual(404,e.response.status_code);

       

if __name__ == '__main__':
    unittest.main()
