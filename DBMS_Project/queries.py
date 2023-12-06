from connection import *
def query1(): 
    a = '''

            // Main Query 1

            WITH date('2023-12-14') as endDate
            WITH endDate, endDate-duration({days:90}) as startDate
            MATCH p=(ctr:DepositAccount)-[:WITHDRAWALS]->(wt:Wire:Transaction)-[:RECEIVES_WIRE]
            ->(ext:ExternalAccount)-[:IBAN_ROUTING]->(iban:IBAN_Code)<-[:HAS_IBAN_CODE]-(fi:FinancialInstitution)-[:OPERATES_IN]->(cty:Country)
            WHERE wt.date >= startDate
                AND wt.date <= endDate
                AND cty.risk_Score > 0.6


            // Step 2 - find the accounts that had cash deposits that transferred to the account that did the wire transfer
            WITH ctr, wt, ext, iban, fi, cty

            MATCH g=(cu:AccountHolder)-[:HAS_ACCOUNT]->(src:DepositAccount)-[:WITHDRAWALS]->(srcTxn:ACH:Transaction)-[:INTERNAL_XFER]->(ctrTxn:ACH:Transaction)-[:DEPOSITS]->(ctr)<-[:HAS_ACCOUNT]-(cu2),
                (ctr)-[:WITHDRAWALS]-(wt)-[:RECEIVES_WIRE]-(ext)-[:IBAN_ROUTING]->(iban)<-[:HAS_IBAN_CODE]-(fi)-[:OPERATES_IN]->(cty), 
                (extName:External:AccountHolder)-[:HAS_ACCOUNT]->(ext)

            WHERE srcTxn.date <= wt.date
                AND duration.inDays(srcTxn.date, wt.date).days < 30

            RETURN cu.accountName, src.accountNumber, srcTxn.amount, srcTxn.transactionDate, ctr.accountNumber, cu2.accountName, wt.amount, wt.transactionDate,
            ext.accountNumber, extName.accountName, fi.bankName, cty.countryName 
            ORDER BY ctr.accountNumber, src.accountNumber;
''' 
    run_main_query1(a)
