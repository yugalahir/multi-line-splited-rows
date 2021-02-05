# Developed by Yugal Kumar Ahir

from tabula import wrapper
import numpy as np
import json
import re
import os
import sys
import yaml
import traceback
import pdfplumber
import pandas as pd

#line_items this is your DataFrame
#multi_line_items rows of data frame on which you have merge - like Serial number, Index Number , unique identifer
def multi_line_ext(line_items, multi_line_items):
    try:
        line_items = line_items.stack().apply(pd.to_numeric, errors='ignore').fillna(0).unstack()
        sd = (line_items == 0).sum(axis=1) > len(line_items.columns) / 2
        df_merge = pd.DataFrame(sd, columns=['check'])
        df_merge = df_merge[df_merge['check'] == True]
        df_merge = df_merge.sort_index(ascending=False)
        print(df_merge, 'df_merged')

        for mi in multi_line_items:
            for vv in df_merge.index:
                if line_items.iloc[vv - 1][mi] != 0:
                    a = line_items.iloc[vv - 1][mi]
                    g = line_items.iloc[vv - 2][mi]
                    l = str(g) + ' ' + str(a)
                    l = l.replace('"', '')
                    line_items = line_items.replace(line_items.iloc[vv - 2][mi], l)

        for vv in df_merge.index:
            line_items = line_items.drop(vv)
        line_items = line_items.replace('\n', '', regex=True)
        line_items = line_items.replace('\|', '', regex=True)
        return line_items

    except Exception as e:
        return traceback.print_exc()