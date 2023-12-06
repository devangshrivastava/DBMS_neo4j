from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from nodes_models import *
from relation_models import *
from datetime import date

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

today_date = date.today()

with GraphDatabase.driver(uri, auth=(username, password)) as driver:
    # Start a session
    with driver.session() as session:
        customer_id = 5
        while(1==1):
            end = input("Do you want to add another customer? (y/n)")
            if end == "n": break
            name = input("Enter the name of the customer: ")
            ques2 = input("Do you want to add internal account or external? (i/e)")
            query = ""
            if(ques2 == "i"):
                accountNumber = input("Enter the account number: ")
                query = create_customer(name, customer_id,accountNumber)
            else:
                accountNumber = input("Enter the account number: ")
                country_name = input("Enter the country name: ")
                risk_score = input("Enter the risk score: ")
                iban_code = input("Enter the IBAN code: ")
                financial_inst_id = input("Enter the financial institution ID(int only): ")
                query = create_extrernal(accountNumber, iban_code, financial_inst_id, country_name, risk_score,name)
                
            print(f"customer {customer_id} created")
            session.run(query)
            customer_id += 1
        

        transaction_id = 9
        b = input("Do you want to add another transaction? (y/n)")
        while(b=='y'):
            ques1 = input("Do you want to add internal transaction or external? (i/e)")
            sender_id = input("Enter the sender's customer ID: ")
            receiver_id = input("Enter the receiver's customer ID: ")
            amount = input("Enter the amount of the transaction: ")
            if(ques1 == "i"): h = sends_internal(amount, today_date, transaction_id,  sender_id, receiver_id,)
            else: h = sends_external(amount, today_date, transaction_id,  sender_id, receiver_id,)
            session.run(h)
            print(f"transaction {transaction_id} created")
            transaction_id += 1
       
    