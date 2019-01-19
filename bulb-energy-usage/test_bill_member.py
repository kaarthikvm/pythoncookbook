import datetime
import unittest

from bill_member import calculate_bill


class TestBillMember(unittest.TestCase):


    def test_calculate_bill_for_march_2017(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-03-31')
        self.assertEqual(amount, 2107.27)
        self.assertEqual(kwh, 17580)

    
    def test_calculate_bill_for_april_2017(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-04-30')
        self.assertEqual(amount, 25.81)
        self.assertEqual(kwh, 179)

    def test_calculate_bill_for_august_2017(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-08-31')
        self.assertEqual(amount, 27.57)
        self.assertEqual(kwh, 167)
        pass

    def test_calculate_bill_for_september_2017(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-09-30')
        self.assertEqual(amount, 9.86)
        self.assertEqual(kwh, 62)
 
    def test_calculate_bill_for_october_2017(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-10-10')
        self.assertEqual(amount, 38.19)
        self.assertEqual(kwh, 223)
 
    def test_calculate_bill_for_april_2018(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2018-04-30')
        self.assertEqual(amount, 50.01)
        self.assertEqual(kwh, 324)

    # failure test case - meter reading not present
    def test_calculate_bill_for_march_2019(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2019-03-31')
        self.assertEqual(amount, 0.0)
        self.assertEqual(kwh, 0)

   # failure test case - key/value error
    def test_calculate_bill_for_march_2017(self):
        amount, kwh = calculate_bill(member_id='member-1234',
                                     account_id='ALL',
                                     bill_date='2017-03-31')
        self.assertEqual(amount, 0.0)
        self.assertEqual(kwh, 0)
        pass;


 
    # since calculate_bill API has to be modified to incorporate
    # gas billing, following test case related to gas billing
    # is tested locally and it is working as expected
    # COMMENTED OUT below code for submission
    #def test_calculate_gas_bill_for_april_2017(self):
    #    amount, kwh = calculate_bill(member_id='member-123',
    #                                 account_id='ALL',
    #                                 bill_date='2017-04-30',
    #                                 bill_type= 'gas')
    #    self.assertEqual(amount, 11.22)
    #    self.assertEqual(kwh, 179)

    
if __name__ == '__main__':
    unittest.main()
