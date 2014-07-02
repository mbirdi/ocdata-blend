import pandas as pd
import numpy as np

##data = pd.read_csv('../data/canada_example.csv')

class ColFeatures(object):
    '''Functions for catergorizing csv files'''
    
    def __init__(self, df):
        # df is a dataframe:
        self.df = df

    
    def get_col_names(self):
        ##df must be a dataframe
        ##df = pd.DataFrame()
        col_name_list = list(self.df.columns.values)
        ##  try and put a raw input to get less then number of values
        return col_name_list

     
    def get_num_col(col_name_list):
        ##df = pd.DataFrame()
        num_col = len(col_name_list)
        return num_col

    def get_feature_histo(var_col_list, var_df):
        ## takes two variables, a list of column names and a dataframe
        col_name_frequency_dict = {}

        for item in var_col_list:
            vc_f_item = var_df[item].value_counts()  ##value counts for item
            ##print vc_f_item
            length_entities_item = len(vc_f_item)  ## the length of the value counts or the number of entities for an item
            ##print length_entities_item
            col_name_frequency_dict[item] = length_entities_item

        series_Column_Entities_Frequency_ = pd.Series(col_name_frequency_dict)

        return series_Column_Entities_Frequency_

    def query_feature_num(series_histo):
        ##  Raw input for the columns of interest
        values = int(raw_input("How many columns have less then this number of entities:"))
        ##  This is a boolean mask looking for values less then the number
        col_query = (series_histo < values).sum()
        return col_query
