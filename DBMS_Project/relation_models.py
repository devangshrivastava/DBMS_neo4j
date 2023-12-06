from nodes_models import *

def sends_external(amount, date, transaction_ID, accountNumber_sender, accountNumber_receiver):
    return f"MATCH (sender:DepositAccount {{accountNumber: {accountNumber_sender}}}), (receiver:ExternalAccount {{accountNumber: {accountNumber_receiver}}}) CREATE (sender)-[:WITHDRAWALS]->(transaction:Transaction:Wire {{amount: {amount}, date: date('{date}'), transactionID: {transaction_ID}}})-[:RECEIVES_WIRE]->(receiver)"

def sends_internal(amount, date, transaction_ID, accountNumber_sender, accountNumber_receiver):
    transaction_ID2 = int(transaction_ID) + 1
    return f"MATCH (sender:DepositAccount {{accountNumber: {accountNumber_sender}}}), (receiver:DepositAccount {{accountNumber: {accountNumber_receiver}}}) CREATE (sender)-[:WITHDRAWALS]->(transaction:Transaction:ACH {{amount: {amount}, date: date('{date}'), transactionID: {transaction_ID}}})-[:INTERNAL_XFER]->(ctrTxn:Transaction:ACH {{amount: {amount}, date: date('{date}'), transactionID: {transaction_ID2}}})-[:DEPOSITS]->(receiver)"

def cash_deposit_query(amount, date, transaction_ID, accountNumber):
    return f"MATCH (receiver:DepositAccount {{accountNumber: {accountNumber}}}) CREATE (transaction:Transaction:Cash {{amount: {amount}, date: date('{date}'), transactionID: {transaction_ID}}})-[:DEPOSITS]->(receiver)"

def cash_withdraw_query(amount, date, transaction_ID, accountNumber):
    return f"MATCH (sender:DepositAccount {{accountNumber: {accountNumber}}}) CREATE (sender)-[:WITHDRAWALS]->(transaction:Transaction:Cash {{amount: {amount}, date: date('{date}'), transactionID: {transaction_ID}}})"

