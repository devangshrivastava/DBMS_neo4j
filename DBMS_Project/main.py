from functions import *
from queries import *
import pandas as pd


while(1==1):
    end = input("Do you want to add another customer? (y/n)")
    if end == "n": break
    customer()

while(1==1):
    end = input("Do you want to add another transaction? (y/n)")
    if end == "n": break
    transaction()


while(1==1):
    end = input("Do you want to add another cash deposit or withdraw? (y/n)")
    if end == "n": break
    ques = input("Do you want to add cash deposit or withdraw? (d/w)")
    if(ques != "d" and ques != "w"): print("Invalid input")
    elif(ques == "d"): cash_deposit()
    else: cash_withdraw()

while(1==1):
    end = input("Do you want to check balance? (y/n)")
    if end == "n": break
    accountNumber = input("Enter the account number: ")
    check_bank_balance(accountNumber)
    

ques = input("Do you want to run a query1? (y/n)")
if(ques == "y"):
    query1()