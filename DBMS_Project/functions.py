from nodes_models import *
from relation_models import *
from connection import *
from neo4j.exceptions import ConstraintError
from datetime import date


today_date = str(date.today())

def customer():
    customer_id = input("Enter the customer ID: ")
    name = input("Enter the name of the customer: ")
    ques2 = input("Do you want to add internal account or external? (i/e)")
    accountID = input("Enter the account ID: ")
    accountNumber = input("Enter the account number: ")
    query = ""
    balance = 1000
    if(ques2 == "i"):
        query = create_customer(name,accountNumber,accountID,balance) # create_customer(name, accountNumber, accountID)
    else:
        country_name = input("Enter the country name: ")
        risk_score = input("Enter the risk score: ")
        iban_code = input("Enter the IBAN code: ")
        financial_inst_id = input("Enter the financial institution ID(int only): ")

        query = create_extrernal(accountNumber, iban_code, financial_inst_id, country_name, risk_score,name,accountID)
        # create_extrernal(accountNumber, iban_code, financial_inst_id, country_name, risk_score, name, accountID):
    try:
        run_query(query)
        print(f"customer {customer_id} created")

    except ConstraintError:
        print("Account number already exists")    
        
def transaction():
    ques1 = input("Do you want to add internal transaction or external? (i/e)")
    sender_id = input("Enter the sender's account Number: ")
    receiver_id = input("Enter the receiver's account Number: ")
    amount = input("Enter the amount of the transaction: ")
    transaction_id = input("Enter the transaction ID: ")
    query = ""
    if(ques1 == "i"): query = sends_internal(amount, today_date, transaction_id,  sender_id, receiver_id,)
    else: query = sends_external(amount, today_date, transaction_id,  sender_id, receiver_id,)
    # sends_external(amount, date, transaction_ID, accountNumber_sender, accountNumber_receiver)
    # sends_internal(amount, date, transaction_ID, accountNumber_sender, accountNumber_receiver)

    try:
        run_query(query)
        print(f"transaction {transaction_id} created")

    except ConstraintError:
        print("Account number already exists")   

    print(query)
   
    
def cash_deposit():
    cash = input("Enter the amount of cash deposited: ")
    accountNumber = input("Enter the account number: ")
    transaction_id = input("Enter the transaction ID: ")
    query = cash_deposit_query(cash, today_date, transaction_id, accountNumber)
    run_query(query)
    print(f"cash_transaction {transaction_id} created")

def cash_withdraw():
    cash = input("Enter the amount of cash withdraw: ")
    accountNumber = input("Enter the account number: ")
    transaction_id = input("Enter the transaction ID: ")
    query = cash_deposit_query(cash, today_date, transaction_id, accountNumber)
    run_query(query)
    print(f"cash_transaction {transaction_id} created")

    

