# Week 4 Methodology

## Prediction target
`Late_delivery_risk` is treated as a binary classification target.

## Leakage control
The feature set intentionally excludes realized delivery variables such as:
- `Days for shipping (real)`
- `Delivery Status`

These variables are known after or during the outcome and could leak future
information into a pre-delivery prediction.

## Model
Logistic Regression with balanced class weights is used as an interpretable
baseline. Numeric variables are median-imputed and standardized. Categorical
variables are imputed and one-hot encoded.

## Validation
An 80/20 stratified train-test split with random_state=42 is used for the
baseline experiment. A production system should additionally use time-aware
validation.

## Optimization
Predicted probabilities are converted into Standard, High, and Critical
intervention tiers. This is a decision-support framework; thresholds should
ultimately be tuned using the real cost of false positives and missed delays.
