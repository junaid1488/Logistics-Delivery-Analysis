# Logistics Delivery Performance Analysis and Late-Delivery Prediction

## Week 2 — Data Collection, Cleaning and Preprocessing

This repository contains the fully coded Week 2 implementation using the actual
DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS dataset.

## What is implemented

- Raw dataset loading
- Automated data-quality profiling
- Missing-value analysis
- Exact duplicate detection/removal
- Removal of completely missing and highly incomplete fields
- Small-group missing-value imputation
- Date conversion
- Delivery-delay feature creation
- IQR-based outlier screening
- Model-ready preprocessing pipeline
- Numeric standardization
- Categorical one-hot encoding
- Train/test split
- Automated tests
- Week 2 Word report

## Run

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Run the complete Week 2 pipeline:

```bash
python src/run_week2.py
```

Run tests:

```bash
pip install pytest
python -m pytest
```

## Outputs

The pipeline creates:

- `outputs/data_quality_report.csv`
- `outputs/iqr_outlier_report.csv`
- `outputs/missing_values_after_cleaning.csv`
- `outputs/DataCoSupplyChain_Cleaned.csv`

## Leakage control

For the future prediction task, realized delivery information such as actual
shipping duration and delivery status must not be used as predictive features.

## Dataset

The raw CSV is included in this ZIP for reproducibility. Before pushing to a
public GitHub repository, check the dataset's license/redistribution terms.
If redistribution is not permitted, remove the CSV and keep the data README
with instructions for obtaining it from the public source.
