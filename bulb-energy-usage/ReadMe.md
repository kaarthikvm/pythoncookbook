Design Considerations
======================
1) Code under development has to be used to generate bill for requested month

2) Considering practical scenario of generating bill using this code for current
   month, future meter reading are unknown

3) Desing details:
      i) For given month to calculate bill, take reading for requested
         month and previous month
      ii) Calculated the difference in unit consumed for calculating total
          amount based on energy consumption
      iii) calculate standing charge based on previous reading date and last
           updated current month reading date
      iv) Assumption that for each account "gas" and "electricity" may be present

      Eg JSON Reading used for testing for gas:
 
  {
  "member-123" : [ 
    {
    "account-abc" : [
      {
      "gas": [
        {
          "cumulative": 17580,
          "readingDate": "2017-03-28T00:00:00.000Z",
          "unit": "kWh"
        },
        {
          "cumulative": 17759,
          "readingDate": "2017-04-15T00:00:00.000Z",
          "unit": "kWh"
        }
       ],
      "electricity": [
        {
          "cumulative": 17580,
          "readingDate": "2017-03-28T00:00:00.000Z",
          "unit": "kWh"
        },
        {
          "cumulative": 17759,
          "readingDate": "2017-04-15T00:00:00.000Z",
          "unit": "kWh"
        },
      ................................

