import pandas as pd
from pandas import Dataframe, Series

class ColFeatures(object):
    """Functions for catergorizing csv files"""
    
    def __init__(self, df):
        """df is a pandas dataframe"""
        self.df = df

    
    def get_col_names(self):
        """Returns a list assuming it receives a pandas dataframe"""
        col_name_list = list(self.df.columns.values)
        return col_name_list

    def get_feature_histo(var_col_list, var_df):
        """takes two variables, a list of column names and a dataframe"""
        col_name_frequency_dict = {}

        for item in var_col_list:
            ##value counts for column names
            vc_f_item = var_df[item].value_counts()
            
            ## Populating a dict based on the column names, and a dict
            length_entities_item = len(vc_f_item)  
            col_name_frequency_dict[item] = length_entities_item

        series_column_entities_frequency_ = pd.Series(col_name_frequency_dict)

        return series_column_entities_frequency_

    def get_query_feature_num_cols(series_histo):
        """  The number of columns which have less then the raw input """
        values = int(raw_input("How many columns have less then this number of entities:"))
        ##  This is a boolean mask looking for values less then the number
        col_query = (series_histo < values).sum()
        return col_query
