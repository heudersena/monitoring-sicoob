import pyodbc

def connection(server_name, database_nama):   
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server="+server_name+";Database="+database_nama+";Trusted_Connection=yes;")
    
    return cnxn.cursor()