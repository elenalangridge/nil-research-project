import pandas as pd
import glob
import os

# Mapping inconsistent school headers to a standard set [1, 3]
header_mapping = {
    'Transaction Date': 'date', 'Date of Deal': 'date', 'Date': 'date', 'Submitted Date': 'date', 'Transaction Date': 'date',
    'Amount': 'amount', 'Total Compensation': 'amount', 'Cost': 'amount', 'Proposed Payment Amount (i.e. $5 per post, $500 per appearance, etc.):': 'amount', 'Total Value of Reported Deals': 'amount', 'Value': 'amount',
    'Sport Name': 'sport', 'Athletic Team': 'sport', 'Sport': 'sport', 'Sport Type': 'sport',
    'Description': 'deal_description', 'Transaction Type': 'deal_description', 'Brief Description': 'deal_description', 'Disclosure Type/Transaction Type': 'deal_description', 'Type of Endorsement:': 'deal_description', 'Transactions': 'deal_description'
}

def clean_nil_data():
    # Identify all raw CSV files in the data/raw folder [5-11]
    raw_path = 'data/raw/*.csv'
    all_files = glob.glob(raw_path)
    clean_dfs = []

    for file in all_files:
        school_name = os.path.basename(file).replace('.csv', '')
        # Read the school file (e.g., ucla.csv, ucdavis.csv) [10, 11]
        df = pd.read_csv(file)
        df = df.rename(columns=header_mapping)
        df = df.loc[:, ~df.columns.duplicated()]  # Remove duplicate columns if any
        
        # Check for required columns
        required_cols = ['amount']
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            print(f"Skipping {school_name}: missing required columns {missing}")
            continue
        
        # Add school name to control for school-level differences [4]
        df['school'] = school_name
        
        # Identify "Social Media" deals by searching for keywords [3, 4]
        # This creates your primary treatment variable
        if 'deal_description' in df.columns:
            df['is_social_media'] = df['deal_description'].str.contains(
                'social media|instagram|tiktok|post|tweet', case=False, na=False
            ).astype(int)
        else:
            df['deal_description'] = 'Other'
            df['is_social_media'] = 0 # Default to 0 if description is missing
        
        if 'sport' not in df.columns:
            df['sport'] = 'Other'
        
        # Standardise amount: convert to numbers, handling missing or 'in-kind' values [2]
        if 'amount' in df.columns:
            df['amount'] = df['amount'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
            df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
        else:
            df['amount'] = 0
        
        # Select standard columns for the final dataset
        cols = ['school', 'date', 'amount', 'sport', 'deal_description', 'is_social_media']
        clean_dfs.append(df[[c for c in cols if c in df.columns]])

    # Combine all schools into one master file [1]
    combined = pd.concat(clean_dfs, ignore_index=True)
    print(f"Combined data has {len(combined)} rows before filtering.")
    
    # Filter for amount > 0
    combined = combined[combined['amount'] > 0]
    print(f"After amount filter, {len(combined)} rows.")
    
    # If date column exists, filter for 2021-2024 or missing date
    if 'date' in combined.columns:
        combined['date'] = pd.to_datetime(combined['date'], errors='coerce')
        combined = combined[combined['date'].isna() | ((combined['date'].dt.year >= 2021) & (combined['date'].dt.year <= 2024))]
        print(f"After date filter, {len(combined)} rows.")
    
    # Save the cleaned file
    combined.to_csv('data/clean/cleaned_nil.csv', index=False)
    print("Step 1 Complete: cleaned_nil.csv created.")

if __name__ == "__main__":
    clean_nil_data()

