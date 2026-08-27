# Week 2 Methodology

## Missing values
- Product Description: remove because it is completely missing.
- Order Zipcode: exclude from the core analytical dataset because missingness is extremely high.
- Customer Lname: replace missing values with `Unknown`.
- Customer Zipcode: median imputation for the small missing group.

## Duplicates
Exact duplicate rows are detected and removed if present.

## Outliers
IQR bounds are calculated for numeric fields. Potential outliers are reported
rather than blindly deleted because extreme logistics/sales values can be
legitimate observations.

## Normalization
StandardScaler is applied in the model-ready pipeline to numerical variables.
Categorical variables are one-hot encoded.

## Reproducibility
All transformations are implemented in Python and can be rerun from the raw
dataset.
