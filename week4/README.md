# Logistics Delivery Performance Analysis and Late-Delivery Prediction

## Week 4 — Predictive Modeling and Optimization

Fully coded Week 4 implementation using the actual DataCo supply-chain dataset.

### Implemented

- Leakage-controlled feature selection
- Train/test split
- Missing-value preprocessing
- Numerical standardization
- Categorical one-hot encoding
- Class-balanced Logistic Regression
- Accuracy, precision, recall, F1 and ROC-AUC
- Confusion matrix
- Model coefficient interpretation
- Late-delivery probability scoring
- Risk-based intervention queue
- Optimization recommendations
- Automated tests
- Week 4 Word report

### Run

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

Run the complete pipeline:

```bash
python src/run_week4.py
```

Outputs include:

- `outputs/model_metrics.csv`
- `outputs/model_metrics.json`
- `outputs/confusion_matrix.csv`
- `outputs/model_coefficients.csv`
- `outputs/high_risk_intervention_queue.csv`
- `outputs/intervention_priority_summary.csv`
- `visualizations/confusion_matrix.png`
- `models/late_delivery_model.joblib`

Run tests:

```bash
pip install pytest
python -m pytest
```

### Leakage control

Actual shipping duration and delivery status are deliberately excluded from
the predictive feature set because they contain outcome information.

### Project progression

Week 1 → Strategic planning  
Week 2 → Cleaning and preprocessing  
Week 3 → EDA and visualization  
Week 4 → Predictive modeling and optimization
