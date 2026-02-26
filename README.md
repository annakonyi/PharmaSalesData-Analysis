# PharmaSalesData-Analysis
The goal

**This project demonstrates a complete end-to-end data analytics workflow, starting from raw data preparation in Python to interactive business intelligence reporting in Power BI.**
**The goal was to transform pharmaceutical sales data into actionable insights that support performance monitoring, trend analysis, and data-driven decision-making.**

The dataset is based on a pharmaceutical sales dataset from Kaggle.


## Tech Stack
### Languages & Tools
    Python (Pandas, NumPy)
    Jupyter Notebook
    Power BI
    DAX & Power Query
    SQL concepts & data modeling
## Libraries
    missingno
    matplotlib
    pandas
    numpy


This project consists of two main stages. First, the data was cleaned and prepared in a Jupyter Notebook using Python. In the second stage, the processed CSV files were integrated into Power BI to create interactive visualizations. This README provides a detailed, step-by-step overview of the entire workflow and methodology.

## 0. Download Pharma Sales Data from Kaggle

## 1. Jupyter Notebook
Using Anaconda Navigator, a Jupyter Notebook environment was launched to perform data preparation and analysis using Python.

  ### 1.1 Read CSV Files
    1.1.1 Import Libraries
          pandas
          numpy
          missingno
          matplotlib.pyplot

 ###  1.2. Create Defined Functions
  Custom reusable cleaning functions were created in:
      portfolio_data_cleaning_functions.py

  ### 1.3. Data Quality Checks
    1.3.1. Checking Missing Values
      The datasets were analyzed to identify missing values. When zero values appeared frequently, they were treated as incorrectly recorded missing values and handled using seasonal imputation. If no zero values       were present, missing values were replaced with zero under the assumption that no sales occurred during that period.
      Since zero sales naturally occur in the dataset, missing values were primarily treated as data gaps and imputed using seasonal patterns.

    1.3.2. Imputation
      Seasonal imputation methods were applied to preserve time-series consistency.

    1.3.3. Check Duplicates
      Duplicate records were identified and removed where necessary.

    1.3.4. Check Data Types
      Columns were validated and converted to appropriate data types to ensure analytical consistency.

    1.3.5. Outlier Detection
      In time-series analysis, outliers are not defined solely by extreme numeric values but by observations that deviate significantly from local trends or seasonal patterns.
      Therefore, both statistical thresholds (such as quantiles and percentile limits) and temporal behavior were considered. Observations outside expected seasonal behavior may indicate data quality issues,            recording errors, or unusual business events.

      1.3.5.1 Visualizations were created to support outlier identification and validation.

###  1.4. Save Cleaned Data
Cleaned dataframes were exported as CSV files for further analysis.

## 2. Power BI
   
 ### 2.1. Data Integration
  CSV files were imported as data sources. In addition to sales datasets, a date table (serving as the central element of the star schema) and a mapping table containing country and product codes were also          included.

 ### 2.2. Data Model Connections
    The data model connections can be viewed in DataConnections.png.

    The model represents a structured Power BI schema designed to support multi-granularity sales analysis across daily, weekly, monthly, and hourly datasets. Central dimension tables ensure consistent filtering and unified reporting across all fact tables. The relational structure improves data integrity, performance, and scalability while enabling efficient KPI calculations and time-based comparisons.

###  2.3. Power BI Dashboard
  
    2.3.1.Purpose of the Visualization
    The goal of the dashboard is to transform cleaned sales data into actionable business insights by enabling users to monitor performance, identify trends, and compare results across time, geography, and            product categories. The visualization supports data-driven decision-making through intuitive and interactive reporting.

    2.3.2. Filters
  
      Interactive slicers allow analysis by:
      Date
      Country
      Product category

    2.3.3. KPIs

      Executive summary metrics including:
      Total Sales
      Month-to-Date performance
      Growth rates
      Target comparison

      The KPI panel delivers an executive-level overview of performance, including total sales, month-to-date results, growth percentages, and target comparisons. This section enables decision-makers to quickly         understand current performance and key changes.

    2.3.4. SUM Value
      The SUM Value section highlights aggregated sales performance through comparative visualizations by country and product. These insights help identify leading markets, product contributions, and performance        gaps, supporting strategic and operational decisions.

    2.3.5. Timetrends
      The Timetrends section presents time-series analysis to reveal sales evolution, seasonal patterns, and performance fluctuations. Historical trend visualization helps users understand business dynamics and         supports forecasting and planning activities.
 

## Conclusion

This project demonstrates the complete data analytics workflow, from raw data preparation and quality validation in Python to advanced business visualization in Power BI. By combining data engineering practices with analytical storytelling, the solution showcases how structured data models and interactive dashboards can transform raw data into meaningful business insights that support informed decision-making.
