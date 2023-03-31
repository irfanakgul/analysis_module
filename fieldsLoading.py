import pandas as pd
import openpyxl
import config as cf

def fn_loadingFields():
    """
    This function will load fields/drivers which wants analyisis. Please fill input/fields.xlsx with correct column names
    .. in order to make analysis based on column name
    return: a df reading excel
    """

    df_fields = pd.read_excel(cf.input + r"\field_names.xlsx")
    return df_fields
