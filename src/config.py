## Conifigures Constants - Helper File ##

"""
Configuration/constants module.

PURPOSE:
Stores constants and reference data used across the project.

WHY:
To separate configuration from logic so that the code is:
    - easier to read
    - easier to maintain
    - easier to update later
    - more modular

EXAMPLES:
Use this file to:
    - change the default number of generated rows
    - change the random seed amount
    - add/remove departments
    - add/remove equipment options
This file allows changes of the above without affecting the main logic file(s).

"""

# Default #records to generate (can be changed to 1000, 1500 (current), 2000, etc)
DEFAULT_RECORD_COUNT = 1500

# Random seed amount - used for reproducibility
# Why: using the same seed promotes consistency in results between runs
DEFAULT_SEED = 42

# Common, "Clean" Department Names - Canonical
# Every department in data should be one of the following names after cleaning in excel/power query
DEPARTMENTS_CANONICAL = [
    "Engineering",
    "Marketing",
    "Finance",
    "HR",
    "Operations",
    "IT"
]

# "Dirty" Department Names - Inconsistent department variants
# Why: To simulate real-world messy input for most accurate data intake simulation
# Promotes real practice on data cleaning
DEPT_VARIANTS = [
    "Engineering", "engineering", " Engineering ",
    "Marketing", "marketing", " Marketing ",
    "Finance", "finance", " Finance ",
    "HR", "hr", " Hr ",
    "Operations", "operations", " Operations ",
    "IT", "it", "I.T.", " I.T. ", "It"
]

# Equipment Data - Common, Clean Data on Equipment options that employees may request
EQUIPMENT_OPTIONS = [
    "Laptop",
    "Monitor",
    "Keyboard",
    "Security Badge",
    "Headset",
    "Docking Station"
]

# Boolean Data - Is training Required
TRAINING_OPTIONS = ["Yes", "No"]

# Output file name for the generated Excel dataset
DEFAULT_OUTPUT_FILE = "generated_hr_dataset.xlsx"

# Optional CSV output if we want to also export a CSV version
# DEFAULT_OUTPUT_CSV = "generated_hr_dataset.csv"
# Commented for now for simplicity during project's intial stages


