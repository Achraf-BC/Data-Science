# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:06:47 2019

@author: ACHRAF CHERGUI
"""
import pandas as pd
def parse_data(df,use_columns,target):
    if target not in df.columns:
        raise ValueError("target column should belong to df")
    X = df[use_columns]
    y = df[target]
    return X,y
    

def fill_na(df):
    continuous_columns = df.select_dtypes(include=["number"])
    categorical_columns = df.select_dtypes(include=["object"])
    for x in continuous_columns : 
        df[x] = df[x].fillna(df[x].mean())
    for x in categorical_columns : 
        df[x] = df[x].fillna(df[x].mode())
    return df


import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

import numpy as np


def plot_hist(df, feature, target, bins=20):
    yes = df[df[target] == 1]
    no = df[df[target] == 0]
    x1 = np.array(no[feature].dropna())
    x2 = np.array(yes[feature].dropna())
    plt.hist([x1, x2], label=df[target].unique(), bins=bins, color=['r', 'b'])
    plt.legend(loc="upper left")
    plt.title('distribution relative de %s' %feature)
    plt.show()
