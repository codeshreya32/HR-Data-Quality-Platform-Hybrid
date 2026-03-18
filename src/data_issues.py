## Inject Missing/Duplicate/Messy Data to Mitigate Data Issues - Helper Script ##

"""
Intentional data-quality issue injection module

PURPOSE:
    -   Introduces realistic "dirty data" into the generated dataset.

USABILITY:
    -   Realism
        -   HR/admin/data-entry workflows, raw data is often imperfect
        -   Makes project realistic and to justify later cleaning/validation steps in Excel and Power Query
        -   Issues such as the following are intentionally injected
            -   extra spaces in names
            -   missing departments
            -   missing employee IDs
            -   duplicate employee IDs
    -   Keeps issue injection separate from base record generation
        -   generation logic remains clean
        -   dirty-data logic is centralized
        -   each issue is explained clearly and modified independently

"""

import random
import pandas as pd

def add_spacing_issues_to_names(df, prob_extra_spaces=0.02, seed=42):
    """
    Add extra leading/trailing spaces to some employee names for realistic "typos" in raw data intake practices
    
    Purpose:
        -   Simulates messy manual data entry such as:
                'John Doe'  --> '  John Doe '
    
    Parameters:
        -   df (pandas.DataFrame):
                The dataset to modify
    
        -   prob_extra_spaces (float):
                Probability that each row's name gets extra spaces

        -   seed (int):
                Random seed for reproducibility

    Returns:

        pandas.DataFrame
            Modified DataFrame
    
    """
    
    random.seed(seed)

    # Create copy to work on to avoid unexpected modifications to original DataFrame
    df = df.copy()

    for i in df.index:
        if random.random() < prob_extra_spaces:
            original_name = str(df.loc[i, "Employee Name"])
            df.loc[i, "Employee Name"] = f"  {original_name} "

            #Record issue in flag column
            curr_flag = str(df.loc[i, "Data Issue Flag"])

            if curr_flag:
                df.loc[i, "Data Issue Flag"] = curr_flag + "; Extra Name Spaces"
            else:
                df.loc[i, "Data Issue Flag"] = "Extra Name Spaces"

    return df

def add_missing_departments(df, missing_fraction=0.015, seed=42):
    """
    Set a small percentage of department values to missing.
        -   simulates incomplete form submissions or incomplete data-entry rows

    Paramaters:
        
        -   df (pandas.DataFrame):
                Dataset to modify

        -   missing_fraction (float):
                Fraction of rows to affect
                Default 0.015 = 1.5%

        -   seed (int):
                Random seed

    Returns:
        pandas.DataFrame
    
    """
    
    random.seed(seed+1)
    df = df.copy()

    n = len(df)
    missing_count = max(1, int(n*missing_fraction))

    selected_inds = random.sample(list(df.index), missing_count)

    for i in selected_inds:
        df.loc[i, "Department"] = None

        curr_flag = str(df.loc[i, "Data Issue Flag"])

        if curr_flag:
            df.loc[i, "Data Issue Flag"] = curr_flag + "; Missing Department"
        else:
            df.loc[i, "Data Issue Flag"] = "Missing Department"

    return df

def add_missing_employee_ids(df, missing_fraction=0.015, seed=42):
    """
    Set a small percentage of Employee ID values to missing
        -   Simulates row(s) with missing key identifiers

    Parameters:

        -   df (pandas.DataFrame):
                Dataset to modify

        -   missing_fraction (float):
                Fraction of rows to affect

        -   seed (int):
                Random seed

    Returns:
        pandas.DataFrame

    """

    random.seed(seed+2)
    df = df.copy()

    n = len(df)
    missing_count = max(1, int(n*missing_fraction))

    selected_inds = random.sample(list(df.index), missing_count)

    for i in selected_inds:
        df.loc[i, "Employee ID"] = None

        curr_flag = str(df.loc[i, "Data Issue Flag"])

        if curr_flag:
            df.loc[i, "Data Issue Flag"] = curr_flag + "; Missing Employee ID"
        else:
            df.loc[i, "Data Issue Flag"] = "Missing Employee ID"

    return df

def add_duplicate_employee_ids(df, duplicate_fraction=0.015, seed=42):
    """
    Introduce duplicate Employee IDs by coping some IDs from dataset's source rows into target rows.
        -   Simulates duplicate key problems
        -   Such as common in administrative data

    Parameters:

        -   df (pandas.DataFrame):
                Dataset to modify

        -   duplicate_fraction (float):
                Fraction of rows that should receive duplicated IDs

        -   seed (int):
                Random seed

    Returns:
        pandas.DataFrame

    """

    random.seed(seed+3)
    df = df.copy()

    n = len(df)
    duplicate_count = max(1, int(n*duplicate_fraction))

    # Valid (source) rows are those that currently have a non-missing ID
    # Make note of which these rows are in the dataset
    valid_id_inds = [
        i for i in df.index
        if pd.notna(df.loc[i, "Employee ID"])
    ]

    # Handle Edge Cases
    # There are too many IDs that are missing 
    if len(valid_id_inds) < 2:
        return df
    
    target_inds = random.sample(
        valid_id_inds,
        min(duplicate_count, len(valid_id_inds))
    )

    source_inds = random.sample(
        valid_id_inds,
        min(duplicate_count, len(valid_id_inds))
    )

    for target_idx, source_idx in zip(target_inds, source_inds):
        df.loc[target_idx, "Employee ID"] = df.loc[source_idx, "Employee ID"]

        curr_flag = str(df.loc[target_idx, "Data Issue Flag"])

        if curr_flag:
            df.loc[target_idx, "Data Issue Flag"] = curr_flag + "; Duplicate Employee ID"
        else:
            df.loc[target_idx, "Data Issue Flag"] = "Duplicate Employee ID"

    return df

def apply_all_data_issues(df, seed=42):
    """
    Apply all intentional dirty-data transformations in sequence.
        -   Mimics a single pipeline wrapper so main() can stay clean

    Returns:
        pandas.DataFrame

    """
    
    # Order Used:
    #   1.  Add name spacing issues
    df = add_spacing_issues_to_names(df, prob_extra_spaces=0.02, seed=seed)
    #   2.  Add missing departments
    df = add_missing_departments(df, missing_fraction=0.015, seed=seed)
    #   3.  Add missing employee IDs
    df = add_missing_employee_ids(df, missing_fraction=0.015, seed=seed)
    #   4.  Add duplicate employee IDs
    df = add_duplicate_employee_ids(df, duplicate_fraction=0.015, seed=seed)

    return df
    