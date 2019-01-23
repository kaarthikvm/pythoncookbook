from datetime import datetime as dt
from load_readings import get_readings
import tariff

############################################
#
# During production use python logging
# framework to choose between various
# log levels like DEBUG,DETAIL,INFO
# For this current exercise, below logging
# is used for debugging. Disable print if required
# by commenting it
#############################################
def debug_print( *args ):
    """ print details for debugging """
    print("****************************\n");
    for info in args:
        print(info);
        print("\n#######################\n");

def fetch_member_details(member_id = None):
    """
        Get all information associated with member_id
        like account-id, reading for gas and electricity
    """
    json = get_readings();
    return json[member_id]

def fetch_meter_reading(account_id=None, m=None, y=None):
    """
        Get the registered meter reading value (gas & electricity) for 
        given month & year
    """
    member_usage_table = {"electricity":fetch_reading_bill_type("electricity", account_id, m, y),
                          "gas":fetch_reading_bill_type('gas', account_id, m, y)};
    debug_print( member_usage_table );
    member_bill_table = {"electricity":tariff_calculation("electricity",
                                                           member_usage_table["electricity"][0],
                                                           member_usage_table["electricity"][1],
                                                           member_usage_table["electricity"][2]),
                          "gas":tariff_calculation("gas",
                                                    member_usage_table["gas"][0],
                                                    member_usage_table["gas"][1],
                                                    member_usage_table["gas"][2])
                         };
    debug_print( member_bill_table );
    return member_bill_table;

def fetch_reading_bill_type(bill_type = None, member_electric_details = None, m=None, y=None):
    """ fetch reading for electricity & gas """
    details = member_electric_details.get(bill_type, []);
    prev_reading, curr_reading = 0, 0;
    prev_date, curr_date=dt(y,m,1), dt(y,m,1); # default value is current date and month request for billing
    
    for i in range(len(details)):
        # extract month & year information from readings
        # check for match to given month and year.
        # fetch previous and current registered reading
        fmt = "%Y-%m-%dT%H:%M:%S.%fZ"; 
        if ((dt.strptime(details[i]["readingDate"],fmt).month == m) and
            (dt.strptime(details[i]["readingDate"],fmt).year == y)):
               # print("matched \n");  # debug point
               curr_reading = details[i]["cumulative"];
               curr_date = dt.strptime(details[i]["readingDate"],fmt);
               if i!=0:
                   prev_reading = details[i-1]["cumulative"];
                   prev_date = dt.strptime(details[i-1]["readingDate"],fmt);
               else: 
                   prev_date = dt(y,m,1); # it is assumed that for first paymnet of initial connection
                                          # day 1 of that month can be considered as start value

    delta = curr_date - prev_date;
    debug_print("prev reading %d"%prev_reading,
                "curr reading %d"%curr_reading,
                "unit consumed %d"%(curr_reading - prev_reading),   
                "delta days %s" %str(delta));
    return [prev_reading, curr_reading, delta.days];     

def tariff_calculation( bill_type=None, prev_reading=0, curr_reading=0, delta_days=0):
    """
        calculate total cost consumer has to pay & no of units consumer
    """
    # calculate total charge for consumed units kWh
    total_unit_charge = tariff.BULB_TARIFF[bill_type]["unit_rate"] * (curr_reading - prev_reading);
    # calculate standing charge for used days
    total_standing_charge = tariff.BULB_TARIFF[bill_type]["standing_charge"] * delta_days;
    debug_print("total unit charge (pence) %.2f" % total_unit_charge,
                "total standing charge (pence) %.2f" % total_standing_charge);
    return [float("%.2f"%((total_unit_charge + total_standing_charge)/100)), # total cost to pay
            int(curr_reading - prev_reading)] # no of units consumed 

def calculate_bill_no_of_account(mdetails=None, account_id=None, bill_type=None, m=None, y=None):
    """
       list of dictionary containing amount,kwh for all/single account id
    """
    il=[];
    ol=[];
    for acc in mdetails: # list of dictionary
        for k,v in acc.items(): # fetch each account information
            debug_print("  fetch reading for account name    %s" %k); 
            il.append(fetch_individual_account_info(k, v[0], bill_type, m, y));
    print(il);
    ol = filter_based_on_account_id(il, account_id);
    print(ol);
    return ol; 


def filter_based_on_account_id(ilist=[], account_id=None):
    """
       filter list based on account_id = ALL / single id
    """
    idetail = [];
    if (account_id != 'ALL'):
        # filter the list for particular account_id
        for i in ilist:
            if account_id == i["account_id"]:
                idetail.append(i);
                return idetail;
    else:
        return ilist;

def fetch_individual_account_info(account_id=None, account_info=None, bill_type=None, m=None, y=None):
    """
        get individual account information from list of json
        DISCLAIMER: Currently either gas/electricity is calculated.
                    Once confirmed from BULB architect team on usage, BOTH gas
                    and electricity combination has to be tweaked bit.
    """ 
    bill = fetch_meter_reading(account_info, m, y);
    ind = dict();  # dictionary containing individual account info
    ind["account_id"]=account_id;
    ind["bill_type"]=bill_type;
    if bill_type == "electricity":
        ind["amount"]=bill["electricity"][0];
        ind["kwh"]=bill["electricity"][1];
    # below else part for Gas is tested locally and it is working as expected
    # API "calculate_bill" has to be modified to incorporate billing for gas
    # eg: calculate_bill(member_id=None, account_id=None, bill_date=None, bill_type='electricity') 
    elif bill_type == "gas": 
        ind["amount"]=bill["gas"][0];
        ind["kwh"]=bill["gas"][1];
    return ind;

def calculate_bill(member_id=None, account_id=None, bill_date=None):
    amount=0.;
    kwh=0;
    bill_type = 'electricity'; # PLEASE NOTE THAT this has been hardcoded as of now.
                               # BUT if we change API calculate_bill, this can be removed
                               # explained in else part of code  
    try:
        debug_print("Calculation for bill date  %s ---- %s" % (member_id, str(bill_date)));
        dtobj = dt.strptime(bill_date,"%Y-%m-%d");
        mdetails = fetch_member_details(member_id);
        debug_print(" Count - no of account registered %d" % len(mdetails));
        amount_kwh_list = calculate_bill_no_of_account(mdetails, account_id, bill_type, dtobj.month, dtobj.year);
        debug_print("List of amount & kwh details with account information == %s" %str(amount_kwh_list));
        if amount_kwh_list is not None:
            amount = amount_kwh_list[0]["amount"]; # Hard code. Please see DISCLAIMER below
            kwh = amount_kwh_list[0]["kwh"]; # Hard coded. Please see DISCLAIMER below
            #DISCLAIMER: Need to discuss with bulb architect team. 
            #            As per "main.py", for given member_id,
            #            "account_id" can be ALL or individual account
            #            For all, list contains bill details of each
            #            account. In that case, "calculate_and_print_bill API
            #            has to be changed to accomodate this list.
            #            Currently that API has been coded for single account_id
            #            (returning single amount & kwh value)
            #            Check with architect team whether sum of all has to be
            #            given. Not sure how json reading/real use case looks like  
    except KeyError as error:
        print("Non existence of Key - Exception occured %s" % error);
    except TypeError as error:
        print("Exception occured %s" % error);
    return amount, kwh
def calculate_and_print_bill(member_id, account, bill_date):
    """Calculate the bill and then print it to screen.
    Account is an optional argument - I could bill for one account or many.
    There's no need to refactor this function."""
    member_id = member_id or 'member-123'
    bill_date = bill_date or '2017-08-31'
    account = account or 'ALL'
    amount, kwh = calculate_bill(member_id, account, bill_date)
    print('Hello {member}!'.format(member=member_id))
    print('Your bill for {account} on {date} is £{amount}'.format(
        account=account,
        date=bill_date,
        amount=amount))
    print('based on {kwh}kWh of usage in the last month'.format(kwh=kwh))
