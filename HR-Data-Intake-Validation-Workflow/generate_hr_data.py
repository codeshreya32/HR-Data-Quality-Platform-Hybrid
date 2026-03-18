## Main Script/Driver ##

"""

Main entry-point script for project.

Usability:
    -   Import modular components
    -   Generate base dataset
    -   Inject dirty-data intentionally into database
    -   Save result to output excel/csv file(s)
    -   Print summary for user review

All detailed work is delegated to other focused modules under src.

"""

from src.config import (
    DEFAULT_RECORD_COUNT,
    DEFAULT_SEED,
    DEFAULT_OUTPUT_FILE,
    #DEFAULT_OUTPUT_CSV  # optional in config.py
)

from src.data_generator import generate_base_records
from src.data_issues import apply_all_data_issues
from src.export_utils import save_to_excel, save_to_csv

def main():
    """
    Main workflow driver

    Performs the following:
        1.  Generate the base dataset
        2.  Inject intentional data-quality issues
        3.  Export to Excel
        4.  Export to CSV (optional)
        5.  Print summary

    """
    # STEP 1:   Generate initial "clean" synthetic dataset
    df = generate_base_records(
        n = DEFAULT_RECORD_COUNT,
        seed = DEFAULT_SEED
    )

    # STEP 2:   Intentionally "dirty" the data
    df = apply_all_data_issues(
        df,
        seed = DEFAULT_SEED
    )

    # STEP 3:   Save the final dataset to excel
    save_to_excel(df, DEFAULT_OUTPUT_FILE)

    # STEP 4:   (optional) Save the final dataset to csv
    # save_to_csv(df, DEFAULT_OUTPUT_CSV)

    # STEP 5:   Print summary + confirmation
    print(f"Successfully Generated {len(df)} Rows")
    print(f"Successfully Exported Data to Excel File: {DEFAULT_OUTPUT_FILE}")
    # (optional) print(f"Successfully Exported Data to CSV File: {DEFAULT_OUTPUT_CSV}")
    print("Columns: ")
    for i in df.columns:
        print(f" - {i}")

if __name__ == "__main__":
    main()
