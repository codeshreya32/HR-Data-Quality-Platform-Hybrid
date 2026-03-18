## Clean Record Generation - Helper Script ##

"""

Base Synthetic Data Generation Script for HR Data Intake Validation Workflow

PURPOSE:
Generates "clean base data" as a combed through dataset before introducing intentional data-quality issues.

RESPONSIBILITY:
    -   Generate realistic employee rows
    -   Create names, IDs, dates, emails, phone numbers
    -   Assign departments, training flags, & equipment
            -   Update this file for 

NOTE:
    - Focus is on generating a valid dataset structure
    - Intentional injection of dirty-data is handled separately in data_issues.py

SEPARATION OF DIRTY-DATA AND CLEAN-DATA GENERATION:
    - Keeps responsibilities clear and code maintainable
    - Encourages modularity of code -- responsible design
    - this file: creates valid records
    - data_issues.py: intentionally introduces errors and inconsistencies for realistic simulation
            
"""

import random
from datetime import date, timedelta, datetime

import pandas as pd
from faker import Faker

from src.config import DEPT_VARIANTS, EQUIPMENT_OPTIONS, TRAINING_OPTIONS

# Following creates a Faker instance
# used to generate realistic fake data (with introduced inconsistencies and errors)
fake = Faker()

def random_start_date(within_days_back=365, within_days_forward=60):
    """
    Generate a realistic employee start date
    
    Returns a date between:
        - 365 days in the past (within_days_back, first arg)
        - 60 days in the future (within_days_forward, second arg)

    within_days_back --> range of time before current day where some employees have started working
    within_days_forward --> range of time after current day where some employees are scheduled to start working

    Usability:
        - Simulates realistic HR onboarding environment
        - ^ Where some employees have recently started and some are scheduled to start soon

    Method:
        1.  Get today's date
        2.  Compute min and max date bounds
        3.  Randomly choose one day in that interval

    Returns:
    datetime.date

    """
    
    today = date.today()
    min_day = today - timedelta(days=within_days_back)
    max_day = today + timedelta(days=within_days_forward)
    delta_days = (max_day - min_day).days

    return min_day + timedelta(days=random.randint(0, delta_days))

def generate_base_records(n=1500, seed=42):
    """
    Generates base HR dataset with realistic synthetic values.
    
    Purpose:
        -   Create n employee records with realistic fields
        -   Not yet introducing intentionally missing or duplicating values

    Parameters:
    n (int):
        first argument --> number of records to generate

    seed (int):
        second argument --> random seed for reproducibility

    Returns:
    pandas.DataFrame

    """
    
    # Set reproducible seeds
    random.seed(seed) # for random
    Faker.seed(seed) # for Faker

    # Build list of unique employee IDs (no repeats)
    # Use IDs within a certain range for realism (e.g. 100000, 100001, 100002, etc)
    base_ids = list(range(100000, 100000+n))

    # Shuffle the IDs so they do not appear in perfect ascending order
    # This reflects situations such as firing/resigning and another employee being added in
    # Which would result in them having the same employee ID but added "later" or "afterwards"
    random.shuffle(base_ids)

    # This list will hold one dictionary per employee row
    rows = []

    for i in range(n):
        # Generate a fake employee name
        employee_name = fake.name()

        # Assign a unique employee ID from the shuffled list
        employee_id = base_ids[i]

        # Pick a department from the intentionally messy list
        # Though this list includes formatting variations, it will still be part of the "base generated data"
        # This is because it still simulates reailstic raw data intake before cleaning of said data is performed
        department = random.choice(DEPT_VARIANTS)

        # Generate a realistic start date
        start_date = random_start_date()

        # Randomly choose between 1 and 3 pieces of equipment
        equipment_count = random.randint(1, 3)

        # random.sample selects unique items without replacement
        # Sort is performed for consistent presentation
        # Joined then into a single text string
        equipment_required = "; ".join(
            sorted(random.sample(EQUIPMENT_OPTIONS, equipment_count))
        )

        # Generate manager name
        manager_name = fake.name()

        # Randomly decide if training is required (yes/no)
        training_required = random.choice(TRAINING_OPTIONS)

        # Generate realistic contact details
        email = fake.email()
        phone = fake.phone_number()

        # Simulate a submission timestamp from sometime in the last 45 days
        submission_timestamp = datetime.now() - timedelta(
            days=random.randint(0, 45),
            minutes=random.randint(0, 1440)
        )

        # Construct one row as a dictionary
        row = {
            "Employee Name": employee_name,
            "Employee ID": employee_id,
            "Department": department,
            "Start Date": start_date,
            "Equipment Required": equipment_required,
            "Manager Name": manager_name,
            "Training Required": training_required,
            "Email": email,
            "Phone": phone,
            "Submission Timestamp": submission_timestamp,

            # Following addition of column tracks which data-quality issue(s) (if any) exist in the row
            # Empty for now (because only clean data), but will be filled later in data_issues.py
            "Data Issue Flag": ""
        }

        rows.append(row)

    #Convert list of row dictionaries into a pandas DataFrame
    df = pd.DataFrame(rows)

    return df


