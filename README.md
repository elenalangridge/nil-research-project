#Data + GitHub repo

##a) Repository Structure
		- 	data/raw/: Contains the original, untouched CSV files for each university provided by CalMatters
		- 	data/clean/: Contains the processed datasets, including the intermediate standardised_nil.csv and the final analysis-ready nil_merged_analysis.csv, along with the data codebook
		- 	code/: Contains the Python scripts required to transform the raw data into a structured format for empirical analysis

##b) Manual Steps Outside of the Code
	- Data Acquisition: If the raw data is not pre-loaded, the individual university CSVs must be downloaded (e.g., ucla.csv, ucdavis.csv, fresnostate1.csv) from the CalMatters GitHub repository. 
	- Missing Records: Note that Cal State Northridge and San Jose State reported having no records of NIL deals and will not have 		corresponding data files for processing. 
	- Software Setup: Ensure Python is installed on your machine along with the pandas and numpy libraries to handle data manipulation and aggregation. 
	- Data Limitations: Be aware that the research utilizes the minimum guaranteed value for ambiguous "per month" or product-based "in-kind" deals to ensure a conservative and realistic estimation

##c) How to Run the Project from Scratch
	- To reproduce the analysis, follow these steps in order. These scripts ensure that varying levels of transparency across schools—ranging from payment-level details to annual team totals—are harmonised into a single dataset.
	###	1. Run the Cleaning Script
File: code/01_cleaning_script.py
Action: This script standardises inconsistent column headers across the 16 schools and searches transaction descriptions to identify the social media "treatment group".
	###	2. Run the Aggregation Script
File: code/02_aggregation_script.py
Action: This script aggregates individual payment records to the sport-team level per year (2021–2024)
- This step is vital for constructing the final outcome variable: the annual NIL sponsorship transaction value per sport

d) Order of Script Execution
- 01_cleaning_script.py: Must be run first to generate the standardised data
- 02_aggregation_script.py: Must be run second to produce the final dataset for empirical modelling
