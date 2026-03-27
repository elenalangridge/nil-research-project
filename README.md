# NIL Research Project

This repository contains the data and code for analysing Name, Image, and Likeness (NIL) deals at California public Division I universities from 2021-2024. The project examines the impact of social media deals on average transaction values, controlling for school and sport.

## Repository Structure

- `README.md`: This file provides a project overview and instructions.
- `code/`: Contains Python scripts for data processing.
  - `01_cleaning_script.py`: Standardises and cleans raw CSV files from multiple universities.
  - `02_aggregation_script.py`: Aggregates cleaned data to team-level averages for analysis.
- `data/`: Contains all data files.
  - `raw/`: Original CSV files from each university (e.g., ucla.csv, ucberkeley.csv, etc.).
  - `clean/`: Processed datasets.
    - `cleaned_nil.csv`: Intermediate cleaned dataset with standardised columns.
    - `nil_merged_analysis.csv`: Final aggregated dataset for regression analysis.

## How to Run the Project from Scratch

### Prerequisites
- Python 3.8 or higher installed on your system.
- Git (optional, for cloning the repository).

### Setup Steps
1. **Clone or Download the Repository**:
   - If using Git: `git clone [repository URL]`
   - Or download the ZIP file and extract it.

2. **Set Up Virtual Environment** (Recommended):
   - Navigate to the project directory.
   - Create a virtual environment: `python -m venv .venv`
   - Activate it: `source .venv/bin/activate` (on macOS/Linux) or `.venv\Scripts\activate` (on Windows).

3. **Install Dependencies**:
   - Install required packages: `pip install pandas numpy`

4. **Run the Scripts in Order**:
   - First, run the cleaning script: `python code/01_cleaning_script.py`
     - This processes raw CSV files, standardises columns, handles missing data, and identifies social media deals.
   - Second, run the aggregation script: `python code/02_aggregation_script.py`
     - This aggregates the cleaned data to school-sport-year level averages.

### Manual Steps Outside of the Code
- **Data Acquisition**: The raw data files are included in `data/raw/`. If you need to update or acquire new data, download CSV files from the CalMatters GitHub repository or relevant sources. Note that some schools (e.g., Cal State Northridge, San Jose State) reported no NIL deals and are not included.
- **Data Validation**: Manually review the cleaned data for any anomalies, as the scripts apply conservative estimates for ambiguous deals (e.g., minimum values for "per month" or in-kind deals).
- **Software Setup**: Ensure your system has Python and the required libraries. If using a different environment manager (e.g., conda), adjust the setup accordingly.
- **Output Verification**: After running scripts, check `data/clean/` for the generated files and verify row counts match expectations.

### Order of Script Execution
1. `01_cleaning_script.py`: Run first to clean and standardise raw data.
2. `02_aggregation_script.py`: Run second to aggregate data for analysis.

After running both scripts, the `nil_merged_analysis.csv` file will be ready for statistical modelling (e.g., regression analysis on the effect of social media deals on NIL values).
