from fieldsLoading import fn_loadingFields
from loading import fn_tables
import config as cf
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import random as rn
import warnings
import seaborn as sns

# df_fields = fn_loadingFields()
pd.set_option('display.max_colwidth', None)
warnings.filterwarnings('ignore')



class Analysis():

    def __init__(self) -> None:
        self.df_table1, self.df_table2 = fn_tables()
        self.df_fields = fn_loadingFields()
        self.df_table1 = self.df_table1
        self.df_table2 = self.df_table2
        self.df_output = cf.df_output
        
       

    def fn_graph(self,df_col_a,df_col_1,colname,exp):
        """
        [fn_graph: draw a bar plot in order to show differencies between Table-1 and Table-2]

        Args:
            df_col_a (df): [ investigated driver/field in table-1]
            df_col_1 (df): [ investigated driver/field in table-2]
            col_name (str): [investigated column name as a string]
            exp (str) : [explanation for graph]

        Returns:
            None
        """

        print(f'>>>>>>>>> drawn {colname} bar plot <<<<<<<<<<<  ')

        len_a = len(df_col_a)
        len_b = len(df_col_1)


        # draw bar
        plt.bar([f'{cf.str_table1}', f'{cf.str_table2}'], [len_a,len_b], width =0.4, align='edge',alpha=0.5, color=['blue', 'green'])
        plt.title(f'"{exp}"')
        plt.xlabel('Tables')
        plt.ylabel(f'Total Number of "{colname}"')

        # make new folder if not exist
        os.chdir(rf'{cf.path_graphs2}')
        os.path.join(rf'{cf.path_graphs2}\{colname}')
        if not os.path.exists(rf'{cf.path_graphs2}\{colname}'):
            os.makedirs(colname)
        rond_name = str(rn.randint(100,999))
        plt.savefig(rf'{cf.path_graphs2}\{colname}\{colname}_{rond_name}.png')
        plt.close()

    def fn_distribution(self,df,col_a,col_1):
        """
        [fn_distribution: draw a box plot in order to show outliers in Table-1 and Table-2]

        Args:
            df (df): [ ivestigated and joined table-1 and table-2]
            col_a (str): [ investigated column name as string]
            col_1 (str): [investigated column name as a string]

        Returns:
            None
        
        
        """

        print(f'>>>>>>>>> drawn {col_a} distribution <<<<<<<<<<< ')
    
        if df[col_1].dtype != 'O':

            df_new = df[[col_a,col_1]]

            # df_new.plot.line(y=[col_a,col_1], figsize=(10,6))
            df_new.plot(kind='box', figsize=(9,6))

            # df_new.plot(kind='density')
            plt.title('distribution')
            plt.xlabel('Values')
            plt.ylabel('density')
            if not os.path.exists(rf'{cf.path_graphs2}\{col_a}'):
                os.makedirs(col_a)
            rond_name = str(rn.randint(100,999))
            plt.savefig(rf'{cf.path_graphs2}\{col_a}\Dist_{col_a}_{rond_name}.png')
        else:
            print(f'<<< Dtype of {col_a} is an object.Hence, cannot be calculated distribution >>> ')


    def fn_density(self,df,col_a,col_1):
        print(f'>>>>>>>>> drawn {col_a} Density <<<<<<<<<<< ')
        if df[col_1].dtype != 'O':
            df_new = df[[col_a,col_1]]
            sns.kdeplot(data=df_new)
            plt.title(f"Graph Density for;\n{col_a}")
            if not os.path.exists(rf'{cf.path_graphs2}\{col_a}'):
                os.makedirs(col_a)
            rond_name = str(rn.randint(100,999))
            plt.savefig(rf'{cf.path_graphs2}\{col_a}\Density_{col_a}_{rond_name}.png')
        else:
            print(f'<<< Dtype of {col_a} is an object.Hence, cannot be calculated Density >>> ')
            

    def fn_analyis_1(self,df_table1,df_table2,col):
        """
        [fn_analyis_1: this func. will make analysis based on total size of dataset separatly table-1 and table-2/
         like how many case are there in dataset and will give a rasult how similar and how differ from each other.]

        Args:
            self.df_table1 (df): [ ivestigated table-1 ]
            self.df_table2 (df): [ ivestigated table-2 ]
            col (str): [ investigated column name as string]

        Returns:
            df_output (df): result of analysis -1
        
        
        """

        print(f"****** Performing seperately analysis-1 ******")

        df_join = pd.merge(self.df_table1, self.df_table2, left_on=f'{cf.str_facility_t1}', right_on=f'{cf.str_facility_t2}')
        
        # transform to INT column if not
        if df_join[f'{cf.str_default_t2}'].dtype == 'O':
            df_join[f'{cf.str_default_t2}'] = df_join[f'{cf.str_default_t2}'].astype('int64')
        df_join['DEFAULT_MATCH'] = (df_join[f'{cf.str_default_t1}'] == df_join[f'{cf.str_default_t2}']).apply(lambda x: 1 if x else 0)

        if self.df_table2[f'{cf.str_default_t2}'].dtype == 'O':
            self.df_table2[f'{cf.str_default_t2}'] = self.df_table2[f'{cf.str_default_t2}'].astype('int64')

        if self.df_table1[f'{cf.str_default_t1}'].dtype == 'O':
            self.df_table1[f'{cf.str_default_t1}'] = self.df_table1[f'{cf.str_default_1}'].astype('int64')
        
        dic ={
        
        'field':col,
        'b_total':len(self.df_table1),
        'b_defaultFlag_1':len(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==1]),
        'b_defaultFlag_0':len(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==0]),
        'g_total':len(self.df_table2),
        'g_defaultFlag_1':len(self.df_table2[self.df_table2[f'{cf.str_default_t2}']==1]),
        'g_defaultFlag_0':len(self.df_table2[self.df_table2[f'{cf.str_default_t2}']==0]),
        'missing_count_def1':f"InDefault==1: {abs(len(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==1]) - self.df_table2[f'{cf.str_default_t2}'].value_counts()[1]) } and\
             %{round((100*abs(len(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==1]) - self.df_table2[f'{cf.str_default_t2}'].value_counts()[1]))/len(self.df_table1),2)} more case in {cf.str_table2}",
        'missing_count_def0': f"InDefault==0: {abs(len(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==0]) - self.df_table2[f'{cf.str_default_t2}'].value_counts()[0]) } and \
             %{round((100*abs(len(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==0]) - self.df_table2[f'{cf.str_default_t2}'].value_counts()[0]))/len(self.df_table1),2)} more case in {cf.str_table2}",
        'match_faciltyID': len(df_join),
        'matching_default':df_join['DEFAULT_MATCH'].value_counts()[1],
        'unmatch_defaultFlag':df_join['DEFAULT_MATCH'].value_counts()[0],
        'missingDefault_perc': f"% {round((100*df_join['DEFAULT_MATCH'].value_counts()[0])/len(df_join),2)} are unmatching based on default of total cases"
            
        }
        # test1 = self.df_table1[self.df_table1[f'{cf.str_default_t1}']==1][f'{cf.str_default_t1}']
        # test2 = self.df_table2[self.df_table2[f'{cf.str_default_t2}']==1][f'{cf.str_default_t2}']

        self.fn_graph(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==1][f'{cf.str_default_t1}'], self.df_table2[self.df_table2[f'{cf.str_default_t2}']==1][f'{cf.str_default_t2}'],col,'WHEN Default==1')
        self.fn_graph(self.df_table1[self.df_table1[f'{cf.str_default_t1}']==0][f'{cf.str_default_t1}'], self.df_table2[self.df_table2[f'{cf.str_default_t2}']==0][f'{cf.str_default_t2}'],col,'WHEN Default==0')
        
        df = pd.DataFrame(dic, index=[0])
        df_output = self.df_output.append(df)
        return df_output
        

    def fn_analysis_2(self, df_table1, df_table2,col_1,col_2):
        """
        [fn_analyis_2: this func. will make analysis based on null and not noll case  separatly table-1 and table-2./
        And it will show how many null in table 1 and table, and how many not null case there are in table-2 ]

        Args:
            self.df_table1 (df): [ ivestigated table-1 ]
            self.df_table2 (df): [ ivestigated table-2 ]
            col_1(str): [ investigated column name for table-1 as string]
            col_2(str): [ investigated column name for table-2 as string]


        Returns:
            df_output (df): result of analysis -2
        
        """

        print(f"******Performing NULL analysis-2 ******")

        self.df_table2 = self.df_table2.astype({f'{cf.str_default_t2}': 'int32'})
 
        t1_d1_notNull = self.df_table1[(self.df_table1[f'{cf.str_default_t1}']==1)][col_1].notnull()
        t1_d1_null = self.df_table1[(self.df_table1[f'{cf.str_default_t1}']==1)][col_1].isna()
        t1_d0_notNull = self.df_table1[(self.df_table1[f'{cf.str_default_t1}']==0)][col_1].notnull()
        t1_d0_Null = self.df_table1[(self.df_table1[f'{cf.str_default_t1}']==0)][col_1].isna()
        
        t2_d1_notNull = self.df_table2[(self.df_table2[f'{cf.str_default_t2}']==1)][col_2].notnull()
        t2_d1_Null = self.df_table2[(self.df_table2[f'{cf.str_default_t2}']==1)][col_2].isna()
        t2_d0_notNull = self.df_table2[(self.df_table2[f'{cf.str_default_t2}']==0)][col_2].notnull()
        t2_d0_Null = self.df_table2[(self.df_table2[f'{cf.str_default_t2}']==0)][col_2].isna()
        
        if cf.bool_drawFile==True:
            self.fn_graph(t1_d1_notNull[t1_d1_notNull==True],t2_d1_notNull[t2_d1_notNull==True],col_1,'Comparison of NOTNULL Cases WHEN Default==1')
            self.fn_graph(t1_d1_null[t1_d1_null==True],t2_d1_Null[t2_d1_Null==True],col_1,'Comparison of NULL Cases WHEN Default==1')
            self.fn_graph(t1_d0_notNull[t1_d0_notNull==True],t2_d0_notNull[t2_d0_notNull==True],col_1,'Comparison of NOTNULL Cases WHEN Default==0')
            self.fn_graph(t1_d0_Null[t1_d0_Null==True],t2_d0_Null[t2_d0_Null==True],col_1,'Comparison of NULL Cases WHEN Default==0')
        
        dic={
            'field':col_1,
            
            f'{cf.str_table1}_default_1_not_NULL':t1_d1_notNull.sum(),
            f'{cf.str_table2}_default_1_not_NULL':t2_d1_notNull.sum(),
            '% Deviations1':f'for default=1; there are {t2_d1_notNull.sum() - t1_d1_notNull.sum()} more Non-Null cases in {cf.str_table2} table. And these number consist of \
                %{float("{:.2f}".format(((t2_d1_notNull.sum() - t1_d1_notNull.sum())*100)/t1_d1_notNull.sum()))} total Non_null of {cf.str_table1}',
            
            'B_default_1_NULL':t1_d1_null.sum(),
            'G_default_1_NULL':t2_d1_Null.sum(),
            '% Deviations2':f'for default=1; there are {t2_d1_Null.sum() - t1_d1_null.sum()} more Null cases in {cf.str_table2} table. And these number consist of\
                 % {float("{:.2f}".format(((t2_d1_Null.sum() - t1_d1_null.sum())*100)/t1_d1_null.sum()))} total null of {cf.str_table1}',
            
            'B_default_0_not_NULL':t1_d0_notNull.sum(),
            'G_default_0_not_NULL':t2_d0_notNull.sum(),
            '% Deviations3':f'When default=0; there are {t2_d0_notNull.sum() - t1_d0_notNull.sum()} more Non-Null cases in {cf.str_table2} table. And these number consist of\
                %{float("{:.2f}".format(((t2_d0_notNull.sum() - t1_d0_notNull.sum())*100)/t1_d0_notNull.sum()))} total Non_null of {cf.str_table1}',
            
            'B_default_0_NULL':t1_d0_Null.sum(),
            'G_default_0_NULL':t2_d0_Null.sum(),
            '% Deviations4':f'When default=0; there are {t2_d0_Null.sum() - t1_d0_Null.sum()} more Null cases in {cf.str_table2} table. And these number consist of\
                 %{float("{:.2f}".format(((t2_d0_Null.sum() - t1_d0_Null.sum())*100)/t1_d0_Null.sum()))} total null of {cf.str_table1}'
        }
        
        df_output = pd.DataFrame(dic, index=[0])
        return df_output


    def fn_analysis_3(self,df_table1,df_table2,col_t1,col_t2):
        """
        [fn_analyis_3: this func. will make analysis based on similarity and differencies after joined table-1 and table-2 by default situation./
        And it will show them based on  matching /unmatching by default=1 and defaul-0  ]

        Args:
            self.df_table1 (df): [ ivestigated table-1 ]
            self.df_table2 (df): [ ivestigated table-2 ]
            col_t1(str): [ investigated column name for table-1 as string]
            col_t2(str): [ investigated column name for table-2 as string]


        Returns:
            df_based_on_dflt (df): result of analysis -3
        
        """
        

        print(f"****** Performing facility Match analysis-3 ******")
        
        # handle column names if they are same in two table.
        if col_t1 == col_t2:
            col_t1 = f"{col_t1}_x"
            col_t2 = f"{col_t2}_y"

        # merge two table based on facilityID
        df_join = pd.merge(self.df_table1, self.df_table2, left_on=f'{cf.str_facility_t1}', right_on=f'{cf.str_facility_t2}')
        if df_join[f'{cf.str_default_t2}'].dtype == 'O':
            df_join[f'{cf.str_default_t2}'] = df_join[f'{cf.str_default_t2}'].astype('int64')
        df_join['DEFAULT_MATCH'] = (df_join[f'{cf.str_default_t1}'] == df_join[f'{cf.str_default_t2}']).apply(lambda x: 1 if x else 0)
        df_short = df_join[[f"{cf.str_facility_t1}",f"{cf.str_facility_t2}",f"{cf.str_default_t1}",f"{cf.str_default_t2}",col_t1,col_t2]]
        
        # fill nan values with sample value to match columns
        df_short[col_t1] = df_short[col_t1].fillna(-999999)
        df_short[col_t2] = df_short[col_t2].fillna(-999999)
        
        # answers
        defaultFlagEqual_fieldEqual = df_short[(df_short[f'{cf.str_default_t1}']==df_short[f'{cf.str_default_t2}']) \
                                               &(df_short[col_t1]==df_short[col_t2]) ]
        
        defaultFlagEqual_fieldNotEqual = df_short[(df_short[f'{cf.str_default_t1}']==df_short[f'{cf.str_default_t2}']) \
                                               &(df_short[col_t1]!=df_short[col_t2]) ]
        
        defaultFlagNotEqual_fieldEqual = df_short[(df_short[f'{cf.str_default_t1}']!= df_short[f'{cf.str_default_t2}']) \
                                               &(df_short[col_t1] == df_short[col_t2]) ]
        
        defaultFlagNotEqual_fieldNotual = df_short[(df_short[f'{cf.str_default_t1}'] != df_short[f'{cf.str_default_t2}']) \
                                               &(df_short[col_t1]!=df_short[col_t2]) ]
        
        if cf.bool_drawFile==True:
            self.fn_graph(defaultFlagEqual_fieldEqual[col_t1],defaultFlagEqual_fieldEqual[col_t2], col_t1,f'by Facility / Default is matching \n/ {col_t1} is matching ')
            self.fn_graph(defaultFlagEqual_fieldNotEqual[col_t1],defaultFlagEqual_fieldNotEqual[col_t2], col_t1,f'by Facility / Default is matching \n/ {col_t1} is not matching ')
            self.fn_graph(defaultFlagNotEqual_fieldEqual[col_t1],defaultFlagNotEqual_fieldEqual[col_t2], col_t1,f'by Facility / Default is not matching\n / {col_t1} is matching ')
            self.fn_graph(defaultFlagNotEqual_fieldNotual[col_t1],defaultFlagNotEqual_fieldNotual[col_t2], col_t1,f'by Facility / Default is not matching\n / {col_t1} is not matching ')
            self.fn_distribution(df_join,col_t1,col_t2)
            # self.fn_density(df_join,col_t1,col_t2)



        # making a df of results
        dic = {
        'field':col_t1,
        'defaultFlagEqual_fieldEqual':len(defaultFlagEqual_fieldEqual),
        'defaultFlagEqual_fieldNotEqual':len(defaultFlagEqual_fieldNotEqual),
        'defaultFlagNotEqual_fieldEqual':len(defaultFlagNotEqual_fieldEqual),
        'defaultFlagNotEqual_fieldNotual':len(defaultFlagNotEqual_fieldNotual)  }
        df_based_on_dflt = pd.DataFrame(dic, index=[0])
        return df_based_on_dflt



    def fn_main_run(self):
        """
        [fn_main_run: this func. will run all analysis module and will write to excel file in output folder. ]

        Args:
            None


        Returns:
            None
        
        """


        print("### class, analysis -1 worked ### ")
        df_all_analysis_1 = pd.DataFrame()
        df_all_analysis_2 = pd.DataFrame()
        df_all_analysis_3 = pd.DataFrame()
        

        for idx,col in self.df_fields.iterrows():
            

            # print(f"############# Performing for : {col[f'{cf.str_table1}']} #############")
            
            #preparing columns from excel
            col_t2 = str(col.xls_table2.upper())
            col_t1 = str(col.xls_table1.upper())

            # run analysis -1
            df_analysis_1 = self.fn_analyis_1(self.df_table1,self.df_table2,col_t1)
            df_all_analysis_1 = df_all_analysis_1.append(df_analysis_1)

            # run analysis -2
            df_analysis_2 = self.fn_analysis_2(self.df_table1,self.df_table2,col_t1,col_t2)
            df_all_analysis_2 = df_all_analysis_2.append(df_analysis_2)

            # run analysis -3 test
            df_analysis_3 = self.fn_analysis_3(self.df_table1,self.df_table2,col_t1,col_t2)
            df_all_analysis_3 = df_all_analysis_3.append(df_analysis_3)


        # write to excel
        writer = pd.ExcelWriter(cf.path_output +r'\all_results.xlsx', engine='xlsxwriter')
        df_all_analysis_1.to_excel(writer, sheet_name='Separate Analysis')
        df_all_analysis_2.to_excel(writer, sheet_name='Null Analysis')
        df_all_analysis_3.to_excel(writer, sheet_name='Anlys.Based on Default')
        writer.close()

        print('<<<< clas 2 worked-----ALL ANALYSIS HAS DONE SUCCESFULY and WRITTEN TO OUTPUT FILE >>>>>>>>>>>')
            


# if __name__=="__main__":
#     myClass = Analysis()
#     myRes = myClass.fn_main_run()

# # exit()