from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from nodes_models import *
from relation_models import *
from datetime import date

uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

today_date = date.today()

def run_query(query): 
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        # Start a session
        with driver.session() as session:
            a = session.run(query)
            print("Query executed")
            

def fetch_query(query): 
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        # Start a session
        with driver.session() as session:
            result = session.run(query)
            account_properties = dict(result.single()["account"].items())
            
            # Print the dictionary            
            print("Query executed")

            return account_properties
            