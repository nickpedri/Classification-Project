from env import get_connection
import pandas as pd
import os


def titanic_data():
    filename = 'titanic.csv'
    if os.path.isfile(filename):  # checks if file exists
        return pd.read_csv(filename)  # if file exists, function will read and return csv file
    else:
        db_url = get_connection('titanic_db')
        query = '''
                SELECT * FROM passengers
                '''
        titanic = pd.read_sql(query, db_url)
        titanic.to_csv('titanic.csv', index=False)
        return titanic


'''This function will retrieve titanic data. It will first check if there is a local .csv file and if there is,
the function will open read and return the contents of that .csv file. If there is no file, the function will create
a SQL query and pull the information from the CodeUp database and then save a local .csv file.'''


def iris_data():
    filename = 'iris.csv'
    if os.path.isfile(filename):  # checks if file exists
        return pd.read_csv(filename)  # if file exists, function will read and return csv file
    else:
        db_url = get_connection('iris_db')
        query = '''SELECT * FROM species as S JOIN measurements as M USING(species_id)'''
        iris = pd.read_sql(query, db_url)
        iris.to_csv(filename, index=False)
        return iris


'''This function will retrieve iris data. It will first check if there is a local .csv file and if there is,
the function will open read and return the contents of that .csv file. If there is no file, the function will create
a SQL query and pull the information from the CodeUp database and then save a local .csv file.'''


def telco_data():
    filename = 'telco.csv'
    if os.path.isfile(filename):  # checks if file exists
        return pd.read_csv(filename)  # if file exists, function will read and return csv file
    else:
        db_url = get_connection('telco_churn')
        query = '''SELECT * FROM customers AS cd
        LEFT JOIN contract_types as ct USING(contract_type_id)
        LEFT JOIN internet_service_types as ist USING(internet_service_type_id)
        LEFT JOIN payment_types as pt USING(payment_type_id)
        WHERE total_charges != '' '''
        telco = pd.read_sql(query, db_url)
        telco.to_csv(filename, index=False)
        return telco


'''This function will retrieve telco data. It will first check if there is a local .csv file and if there is,
the function will open read and return the contents of that .csv file. If there is no file, the function will create
a SQL query and pull the information from the CodeUp database and then save a local .csv file.
*NOTE* The SQL query in this function joins a few tables and it also gets rid of 11 rows that have a missing 
total charge.'''


def sql_query(db='None', query='None'):
    if db == 'None':
        print('Database not specified.')
    elif query == 'None':
        print('No query!')
    else:
        db_url = get_connection(db)
        df = pd.read_sql(query, db_url)
        return df


'''This is a function to easily and quickly create a SQL query in python without having to perform multiple steps. This
function takes in two arguments: db which is the database that you wish to connect/use, and query which is the
query that you would like to run.'''


def show_tables(db='None'):
    if db == 'None':
        print('Database not specified')
    else:
        db_url = get_connection(db)
        query = 'SHOW TABLES'
        tables = pd.read_sql(query, db_url)
        return tables


'''This is a simple function that takes a database argument and returns all of the tables within the database.'''
