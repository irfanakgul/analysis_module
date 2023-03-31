import pandas as pd
global path_graphs2



# paths
root = r"C:\Users\AkgulI\PycharmProjects\analysis_grfd"
input = root + "\input"
path_output = root + "\output2"
path_graphs = path_output + "\graphs"
path_graphs2 = root + r'\output2\graph'


# table names
bubble = r"[RA_ABB_Custom].[CreditCoreImpact].[RSME_Input_202204_Facility_Test_CRC] as B"
grfd = r"[RA_ABB_Custom].[GRFDImpactAssessments].[Input.Facility_B147] as G"

# server connections
connection = '''DRIVER={ODBC Driver 17 for SQL Server};Server=lbbbubble.eu.rabonet.com\ABB_PRD_01;
Database=RA_ABB_Custom;Trusted_connection=yes;'''

# empty df for analysis-1 
cols=['field','b_total','b_defaultFlag_1','b_defaultFlag_0','g_total','g_defaultFlag_1',\
          'g_defaultFlag_0','missing_count_def1','missing_count_def0','match_faciltyID',\
          'matching_default','unmatch_defaultFlag','missingDefault_perc']
df_output = pd.DataFrame(columns=cols)

#variables
str_table1 = 'BUBBLE'
str_table2 = 'GRFD'
str_facility_t1 = 'facilityId'.upper()
str_facility_t2 = 'REG_FCY_ID'.upper()
str_default_t1 = 'defaultFlag'.upper()
str_default_t2 = 'DFLT_F'.upper()

# indicate preference regarding graph drawn T-F
bool_drawFile = True

# Time Period setting
adjust_mpi = True
mpi = 202204
str_table1_mpi = 'MeasurementPeriodID'
str_table2_mpi = 'RPT_PRD'

