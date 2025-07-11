"""
Module that cointains main data preprocessing functions
"""
import pandas as pd
import numpy as np
import io

def load_data(csv_text):
    """
    Function that returns a Pandas DataFrame
    Object generated from the csv data
    """
    csv_buffer = io.StringIO(csv_text)
    df = pd.read_csv(csv_buffer)
    return df

def remove_nulls(df, opt):
    """
    Function that remove nulls from the dataframe object.
    axis = 0 to remove rows
    axis = 1 to remove columns
    """
    if opt == "rm-0": 
        df.dropna(axis=0, inplace=True)
    elif opt == "rm-0":
        df.dropna(axis=1, inplace=True)

def replace_nulls(df, replace_by):
    """Function that replace all the null values in the
        data frame object.
    """
    if replace_by == "rp-mean": # replace nulls with mean in numerical columns
        df.fillna(df.mean(numeric_only=True), inplace=True)
    elif replace_by == "rp-mode": # replace nulls with mode in numerical columns
        df.fillna(df.mode(numeric_only=True), inplace=True) 
    elif replace_by == "rp-mode": # replace nulls with mode in all columns
        df.fillna(df.mode(), inplace=True)
    elif replace_by == "mean_mode": # replace nulls with mean in numerical columns and mode in others
        df.fillna(df.mean(numeric_only=True), inplace=True)
        df.fillna(df.mode(), inplace=True)
    elif replace_by == "pr-f": # fill values by propagating the last valid observation.
        df.ffill(inplace=True)
    elif replace_by == "pr-b": # fill values by using the next valid observation to fill the gap.
        df.bfill(inplace=True)
        

    

    

