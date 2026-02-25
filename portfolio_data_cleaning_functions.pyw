import pandas as pd
import numpy as np 
import missingno as msno
import matplotlib.pyplot as plt

def seasonal_average_daily(sales, column):
    
    sales = sales.copy()
    sales = sales.sort_index()

    # weekday: Monday=0 ... Sunday=6
    weekday_mean = sales.groupby(sales.index.weekday)[column].transform("mean")

    # fill missing values
    sales[column] = sales[column].fillna(weekday_mean)

    return sales

def seasonal_average_hourly(sales, column):
    
    sales = sales.copy()
    sales = sales.sort_index()

    hour_mean = sales.groupby(sales.index.hour)[column].transform("mean")

    sales[column] = sales[column].fillna(hour_mean)

    return sales

    
def detect_and_replace_outliers(df, column, freq):
    """
    Detect and replace outliers using seasonal deviation.
    Also plots a boxplot BEFORE replacement to visualize outliers.
    """

    df = df.copy()
    df = df.sort_index()

    # --- choose seasonal grouping ---
    if freq == "M":
        seasonal_group = df.index.month
    elif freq == "W":
        seasonal_group = df.index.isocalendar().week
    elif freq == "D":
        seasonal_group = df.index.weekday
    elif freq == "H":
        seasonal_group = df.index.hour
    else:
        raise ValueError("Unsupported frequency")

    # seasonal mean & std
    seasonal_mean = df.groupby(seasonal_group)[column].transform("mean")
    seasonal_std = df.groupby(seasonal_group)[column].transform("std")

    # detect outliers (3-sigma rule)
    df["is_outlier"] = abs(df[column] - seasonal_mean) > 3 * seasonal_std

    # store seasonal group for plotting
    df["seasonal_group"] = seasonal_group

    # --- PLOT BEFORE REPLACEMENT ---
    plt.figure(figsize=(12, 6))

    # boxplot grouped by seasonal group
    df.boxplot(column=column, by="seasonal_group")
    plt.title(f"Boxplot of {column} by Seasonal Group ({freq})")
    plt.suptitle("")
    plt.xlabel("Seasonal Group")
    plt.ylabel(column)

    # overlay outliers
    outliers = df[df["is_outlier"]]
    plt.scatter(
        outliers["seasonal_group"],
        outliers[column],
        color="red",
        label="Detected Outliers",
        zorder=3
    )

    plt.legend()
    plt.show()

    # --- REPLACE OUTLIERS AFTER PLOTTING ---
    df.loc[df["is_outlier"], column] = seasonal_mean[df["is_outlier"]]

    return df
