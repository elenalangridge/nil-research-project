# NIL Research Project — Analysis Dataset Codebook

**Research question:** Do social media deals command higher average NIL compensation, conditional on school, sport, and year?

**Unit:** ECC3479 — Data and Evidence in Economics, Monash University  
**Group:** Elena Langridge, Teah Papageorgiou, Lily Proposch  
**Date:** May 2026

---

## Dataset: `nil_merged_analysis.csv`

### Overview
- **Unit of observation:** School × sport × year × deal-type group
- **N observations:** 358 groups (after dropping partial-year 2025)
- **Years:** 2021–2024
- **Schools:** 12 California public D-I universities
- **Sports:** 20 standardised sport categories
- **Data source:** Aggregated from `cleaned_nil.csv` via `code/02_aggregation_script.py`

### Variables

| Variable | Type | Description | Notes |
|----------|------|-------------|-------|
| `school` | String | University identifier | 12 unique values: calpolyslo, csulongbeach, sacramentostate1–4, ucberkeley, ucdavis, ucla, ucriverside, ucsandiego1, ucsantabarbara |
| `sport` | String | Sport category (standardised) | 20 sports: Baseball, Basketball, Beach Volleyball, Cross Country, Equestrian, Football, Gymnastics, Ice Hockey, Lacrosse, Rowing, Rugby, Soccer, Softball, Swimming & Diving, Tennis, Track and Field, Volleyball, Water Polo, Wrestling, Other |
| `year` | Integer | Calendar year of deal | 2021, 2022, 2023, 2024 (2025 excluded: N=13, partial-year reporting) |
| `is_social_media` | Binary | 1 if deal is social media; 0 otherwise | Derived from keyword matching on free-text `deal_description` in raw data. Special rule: UC San Diego (`ucsandiego1`) rows with blank notes coded as 1 (social media by assumption) |
| `avg_transaction_value` | Float | Mean NIL transaction value (USD) | Group-level average; n=358 groups, each may represent multiple individual deals. Includes $0.01 floor for missing/in-kind deals. Range: $0.01–$84,290.29; median: $178.72 |

### Descriptive Statistics

```
Total rows:                     358
Social media groups (is_social_media=1):  156 (43.6%)
Non-social media groups:        202 (56.4%)

Outcome: avg_transaction_value
  Mean:                         $2,184.62
  Median:                       $178.72
  SD:                           $5,423.42
  Min:                          $0.01
  Max:                          $84,290.29
  Skewness (raw):               6.749

Log-transformed: log(1 + avg_transaction_value)
  Mean:                         5.556
  Median:                       5.191
  SD:                           1.643
  Skewness:                     0.702 (near-normal)
```

### Data Quality Notes

1. **UC San Diego assumption rule:** UCSD rows with blank `Notes` fields are coded as `is_social_media=1` (social media by assumption). This is a conservative assumption applied during data cleaning; see `01_cleaning_script.py` for implementation.

2. **Measurement error in treatment:** `is_social_media` is derived from keyword matching on free-text `deal_description`. This introduces false positives and false negatives. See Section 7.2 (Threats to Validity) in `03_primary_analysis.ipynb` for discussion.

3. **Group-level aggregation:** The unit is a school-sport-year-deal-type *group average*, not individual deals. Small groups may be dominated by outliers; see Section 7.4 (Aggregation Artifact) for discussion.

4. **Missing year:** A small number of transactions had unparseable dates and were assigned a random year from {2021–2024}. This introduces noise into year fixed effects. See Section 7.5 (Date Imputation) for discussion.

---

## How to Reproduce This Dataset

From scratch:

1. Ensure raw files exist in `data/raw/` (included in repository)
2. Run `python code/01_cleaning_script.py`
   - Output: `data/clean/cleaned_nil.csv` (transaction-level, 2,347 rows)
3. Run `python code/02_aggregation_script.py`
   - Output: `data/clean/nil_merged_analysis.csv` (group-level, 371 rows initially; 358 after dropping 2025)

Or load directly from the repository:
```python
import pandas as pd
df = pd.read_csv("data/clean/nil_merged_analysis.csv")
df = df[df["year"] <= 2024]  # Drop 2025 partial-year observations (N=13)
```

---

## Analysis Files Using This Dataset

- **`new/03_primary_analysis.ipynb`** — Primary econometric analysis
  - Runs OLS regressions with fixed effects (year, school, sport)
  - Produces publication-quality tables and diagnostics
  - Includes robustness checks (exclude UC San Diego, winsorize, alternative specs)
  - Outputs: `new/results/{regression_table.png, coefficient_plot.png, residual_diagnostics.png}`

---

## References

- **CalMatters NIL repository:** https://github.com/calmatters/nil-disclosures
- **Data acquisition:** Individual university FOIA responses and public NIL registries
- **Codebook 1** (transaction-level data): `data/codebook 1 .md`
