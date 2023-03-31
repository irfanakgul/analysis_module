import pandas as pd
import pyodbc
import config as cf


def fn_tables():

    """[This function loads tables from the server.]

    Args:
        No Args

    Returns:
        [table1]: [df- this is first table that investigated]
        [table2]: [df- this is second table that investigated]
    """


    # Connected to database server
    conn = pyodbc.connect(cf.connection)
    df_fields = pd.read_excel(fr"{cf.input}\field_names.xlsx")

    # loading of bubble and grfd tables
    table1 = pd.read_sql(f'SELECT * FROM {cf.bubble}',conn)
    table2 = pd.read_sql(f'SELECT * FROM {cf.grfd}',conn)
    print(f"**** {cf.str_table1} and {cf.str_table2} HAVE LOADED **** ")

    #set measurement period ID
    if cf.adjust_mpi == True:
        table1 = table1[table1[cf.str_table1_mpi]==cf.mpi]
        table2 = table2[table2[cf.str_table2_mpi]==cf.mpi]
        print(f'$$$ MeasurementPeriodID has adjusted as "{cf.mpi}" $$$')
    else:
        print('$$$ Any MeasurementPeriodID have not adjusted!!! $$$ ')

       
    #make uppercase all columns. done for make equal column name. 
    table1.columns = map(str.upper, table1.columns)
    table2.columns = map(str.upper, table2.columns)

    
    return table1, table2
