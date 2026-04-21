# Data Codebook

This codebook documents the final dataset variables produced by the pipeline for the NIL analysis.

## File: data/clean/cleaned_nil.csv (transaction-level)

- `school` (string)
  - Source university name (from raw file base name or explicit row-level column if available).

- `date` (integer)
  - Year of transaction, derived from date columns (e.g., `Transaction Date`, `Submitted Date`) or randomly assigned among {2021, 2022, 2023, 2024} when missing.

- `amount` (numeric)
  - NIL deal amount, cleansed from strings with `$` and `,` removed, converted to numeric. Non-parsable or blank values default to 0.
  - Rows with `amount <= 0` are dropped in cleaning.

- `sport` (string)
  - Standardized D1 sport label after mapping many variants and abbreviations.
  - Example values: `Basketball`, `Soccer`, `Volleyball`, `Water Polo`, `Track and Field`, `Football`, `Golf`, `Rowing`, `Gymnastics`, `Cross Country`, `Softball`, `Beach Volleyball`, `Other`.

- `deal_description` (string)
  - Deal type/description.  Missing/blank values are set to `Other`.
  - For UC San Diego row-level input, blank `Notes` is mapped to `Social Media` by rule.

- `is_social_media` (integer, 0/1)
  - 1 if `deal_description` contains social media keywords (`social media`, `instagram`, `tiktok`, `post`, `tweet`), else 0.

## File: data/clean/nil_merged_analysis.csv (aggregated analysis-level)

- `school` (string)
  - University identifier.

- `year` (integer)
  - Transaction year group (2021–2024).

- `sport` (string)
  - Standardized sport group.

- `is_social_media` (integer, 0/1)
  - Treatment indicator for social media deals.

- `avg_transaction_value` (numeric)
  - Mean NIL value (`amount`) for the grouped observation.

## Notes and transformation logic

- Raw data is read from `data/raw/` CSV files (e.g., `ucla.csv`, `ucberkeley.csv`, etc.).
- Excluded: `fresnostate1`, `sandiegostate1` (manual exclusion rule), plus raw files without mappable `amount` (e.g., `ucirvine1`/`ucirvine2`, `sandiegostate2`, etc.).
- Column mapping key in `code/01_cleaning_script.py` includes: `Amount`, `Total Compensation`, `Cost`, `Total NIL`, etc.
- Sport normalisation map in cleaning script includes and standardises abbreviations like `MWP` -> `Water Polo`, `MBB` -> `Basketball`, `WVB` -> `Volleyball`, etc.
- Year fallback: if no date is parsed, fill with a random year from 2021 to 2024.
- Aggregation script groups by (`school`, `year`, `sport`, `is_social_media`) and calculates mean/size.

## Reproducibility

1. Run `python code/01_cleaning_script.py`.
2. Run `python code/02_aggregation_script.py`.
3. Verify outputs in `data/clean/`:
   - `cleaned_nil.csv`
   - `nil_merged_analysis.csv`
