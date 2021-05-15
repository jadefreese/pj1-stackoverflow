import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from collections import defaultdict

'''
FUNCTION: Create a data frame which includes unique values and the total number of occurances in the input data frame

INPUTS:
    df - dataframe to search
    col1 - column to look through
    col2 -column to count values from
    look_for - list of strings to search for in each row of col1

OUTPUTS:
    new_df - dataframe of each item in look_for with a count of how often it appears and sorted by this count

'''
def total_count(df, col1, col2, look_for):
    new_df = defaultdict(int)
    for val in look_for:
        for idx in range(df.shape[0]):
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])   
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df

'''
FUNCTION: 
'''
def bar_plotting(df,title='Title',plot=True):
    df.set_index(df.columns[0], inplace=True)
    if plot:
        (df/df.sum()).plot(kind='bar',legend=None)
        plt.title(title)
        plt.show()
    final_df = df/df.sum()
    return final_df

'''
'''
def clean_age(df, lang_used, title='Title', plot=True):
    lang = df['LanguageWorkedWith'].value_counts().reset_index()
    lang.rename(columns={'index':'language','LanguageWorkedWith':'count'}, inplace = True)
    lang_df = total_count(lang,'language','count',lang_used)

    lang_df.set_index('language', inplace=True)
    final_df = lang_df/lang_df.sum()
    return final_df
