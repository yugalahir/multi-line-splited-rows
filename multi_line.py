'''
Developed by Yugal Kumar Ahir.
Purpose - Merging the multiple line description of the product into its parent row.
Usage Import the below libraries and then add the multi_line_ext(line_items, multi_line_items) into your class.
'''
from tabula import wrapper
import numpy as np
import re
import traceback
import pdfplumber
import pandas as pd
'''
Function name multi_line_ext(line_items, multi_line_items)
Parameters
1 line_items this holds the main dataframe 
2 multi_line_items has sub dataframe column on which we have to merge the rows e.g Serial number, Index Number , unique identifer
'''
class Docworx():
        line_items = [] #initial value of line_items list to empty
        def multi_line_ext(line_items, multi_line_items):
            try:
                line_items = line_items.stack().apply(pd.to_numeric, errors='ignore').fillna(0).unstack()  #cleaning the dataframe
                sd = (line_items == 0).sum(axis=1) > len(line_items.columns) / 2    #getting the average of (sum of empty data of row divied by total number of columns)
                df_merge = pd.DataFrame(sd, columns=['check']) 
                df_merge = df_merge[df_merge['check'] == True]
                df_merge = df_merge.sort_index(ascending=False)
                #Running loop on the columns 
                for mi in multi_line_items: 
                    for mi_sub_df in df_merge.index:
                        if line_items.iloc[mi_sub_df - 1][mi] != 0:
                            first_line = line_items.iloc[mi_sub_df - 1][mi] #getting first parent rows
                            next_line = line_items.iloc[mi_sub_df - 2][mi] #getting child rows
                            temp_holder = str(next_line) + ' ' + str(first_line)
                            temp_holder = temp_holder.replace('"', '') #removing "
                            line_items = line_items.replace(line_items.iloc[mi_sub_df - 2][mi], temp_holder)

                for temp_cleaner in df_merge.index:
                    line_items = line_items.drop(temp_cleaner)  #removing the irrelevant data
                line_items = line_items.replace('\n', '', regex=True) #removing spaces
                line_items = line_items.replace('\|', '', regex=True) #removing pine line
                return line_items

            except Exception as e:
                #logging of errors
                return traceback.print_exc()
#End of class
