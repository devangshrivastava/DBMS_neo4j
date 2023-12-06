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
            session.run(query)
            print("Query executed")
       
    