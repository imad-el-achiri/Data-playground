import inspect
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plost


def dfPrinter(*args, **kwargs) -> None:
    """
    prints/shows a dataframe/data/dataset
    Args:
      This function does not take any parameters, call it with none
    """

    calling_frame = inspect.stack()[1].frame
    calling_globals = calling_frame.f_globals
    df = calling_globals["df"]
    st.write(df)

def scatterPlot(column1: str, column2: str) -> None:
    """
    prints a scatterplot of two dataframe columns
    Args:
      column1 (str): The first column
      column2 (str): the second column
    """
    calling_frame = inspect.stack()[1].frame
    calling_globals = calling_frame.f_globals
    df = calling_globals["df"]
    st.scatter_chart(data=df, x=column1, y=column2, x_label=column1, y_label=column2)

def summarize(column: str) -> None:
    """
    Calculates a summary of statistics about the column from the dataframe
    Args:
      column (str): The column to do a statistical summary about
    """
    calling_frame = inspect.stack()[1].frame
    calling_globals = calling_frame.f_globals
    df = calling_globals["df"]
    st.write(df[[column]].describe())

def histogram(column: str) -> None:
    """
    draws/plots a histogram/barplot/ditribution plot about the column from the dataframe
    Args:
      column (str): The column to do plot the histogram for
    """
    calling_frame = inspect.stack()[1].frame
    calling_globals = calling_frame.f_globals
    df = calling_globals["df"]

    plost.hist(
    data=df,
    x=column,
    aggregate='count')

    #fig, ax = plt.subplots()
    #ax.hist(df[column], bins=20)

    #st.pyplot(fig)