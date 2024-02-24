#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports (no need to add anything here)

# Define the configuration for the MSSQL database
mssql = {'host': 'dbhost',  # the hostname of the MSSQL server
         'user': 'dbuser',  # the username to connect to the MSSQL server
         'passwd': 'dbPwd',  # the password for the above user
         'db': 'db'}  # the name of the database to connect to

# Define the configuration for the PostgreSQL database
postgresql = {'host': '0.0.0.0',  # the hostname of the PostgreSQL server
         'user': 'postgres',  # the username to connect to the PostgreSQL server
         'passwd': 'magical_password',  # the password for the above user
         'db': 'db'}  # the name of the database to connect to

# Create the connection string for the MSSQL database using the pyodbc library
mssqlConfig = "mssql+pyodbc://{}:{}@{}:1433/{}?driver=SQL+Server+Native+Client+10.0".format(mssql['user'], mssql['passwd'], mssql['host'], mssql['db'])

# Create the connection string for the PostgreSQL database using the psycopg2 library
postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])

