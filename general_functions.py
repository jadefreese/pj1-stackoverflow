import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from collections import defaultdict

def total_count(df, col1, col2, look_for):

    """
    FUNCTION: Create a data frame which includes unique values and the total 
              number of occurances in the input data frame

    INPUTS:
        df - dataframe to search
        col1 - column to look through
        col2 -column to count values from
        look_for - list of strings to search for in each row of col1

    OUTPUTS:
        new_df - dataframe of each item in look_for with a count of how often 
                 it appears and sorted by this count
    """

    new_df = defaultdict(int)
    for val in look_for:
        for idx in range(df.shape[0]):
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values(col2, ascending = False, inplace = True)
    return new_df

def bar_plotting(df, title='Title', plot=True):

    """
    FUNCTION: Create a bar plot of a given df which shows the percentage of 
              each category

    INPUTS:
        df - data frame to model
        title - string of the plot's title
        plot - boolean - if true, the function plots the data

    OUTPUTS:
        final_df - data frame with values from df and their percentage of 
                   the total repsonses
    """

    df.set_index(df.columns[0], inplace=True)
    if plot:
        (df/df.sum()).plot(kind = 'bar', legend = None)
        plt.ylabel('percentage')
        plt.title(title)
        plt.show()
        plt.savefig(title)
    final_df = df/df.sum()
    return final_df

def percentage_breakdown(df, unique_vals, ref_col, cat_breakdown):

    """
    FUNCTION: Create a new data frame with the percentage break down of 
              frequency of unique values by the chosen category

    INPUTS:
        df - data frame to model
        unique_vals - list of possible values to search for
        ref_col - string of the name of the column to search in the data frame
        cat_breakdown - string of the name of the column by which to breakdown
                        the percentages of the ref_col

    OUTPUTS:
        final_df - data frame with values from cat_breakdown broken down into 
                   percentages of ref_col
    """

    values = df[ref_col].value_counts().reset_index()
    values.rename(columns = {'index': ref_col, ref_col: cat_breakdown},
                  inplace = True)
    values_df = total_count(values, ref_col, cat_breakdown, unique_vals)

    values_df.set_index(ref_col, inplace=True)
    final_df = values_df/values_df.sum()
    return final_df

def get_max_cat(df):

    """
    FUNCTION: Return the top category of sorted input dataframe

    INPUTS:
        df - data frame containing the percentage breakdown of a category

    OUTPUTS:
        top_val - string containing the top category from the dataframe
    """

    df = df.transpose()
    top_val = df.columns[0]
    return top_val

def add_top_per_cat(df, max_vals):

    """
    FUNCTION: Add top values of each data frame of the input list to a new 
              dataframe of max categories

    INPUTS:
        df - data frame to add rows to
        max_vals - list of dataframes filtered by category

    OUTPUTS:
        df - input dataframe containing the appended max value per category
    """

    for cat_df in max_vals:
        df = df.append({df.columns[0]: cat_df.columns[0],
                       df.columns[1]: get_max_cat(cat_df)},
                       ignore_index = True)
    return df
