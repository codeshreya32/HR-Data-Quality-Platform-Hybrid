## Saves Data to Excel/CSV - Helper Script ##

"""
Export/output utility module.
    -   Handles writing datasets to output files such as Excel and CSV

WHY:
    -   Saving/exporting is a separate responsibility from data generation
    -   Separating export logic encourages:
        -   cleaner main file
        -   reusable output code
        -   seamless future updates/collaborations such as adding new formats etc
        -   overall modularization of code (best practice)

"""

import pandas as pd

def save_to_excel(df, output_path):
    """
    Saves a given pandas DataFrame to an Excel file.
        -   Uses pandas.DataFrame.to_excel()

    Paramaters:

        -   df (pandas.DataFrame):
                Dataset to save

        -   output_path (str):
                File path or file name for the excel output
                Specifies destination of the file

    NOTE:
        -   index=False prevents pandas from writing row numbers as an extra column           

    """

    df.to_excel(output_path, index=False)

def save_to_csv(df, output_path):
    """
    Save a given pandas DataFrame to a CSV file.
        -   Using pandas.DataFrame.to_csv()

    Parameters:
        -   df (pandas.DataFrame):
                Dataset to save

        -   output_path (str):
                File path or file name for the CSV output

    NOTE:
        index=False --> prevents pandas from writing row numbers as an extra column

    """
    
    df.to_csv(output_path, index=False)


