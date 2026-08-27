# Logistics Delivery Performance Analysis and Late-Delivery Prediction

## Week 3 — Advanced EDA and Visualization

Fully coded Week 3 project using the actual DataCo supply-chain dataset.

### Implemented

- Dataset loading
- Date preparation
- Delivery-delay feature creation
- Late-risk feature creation
- Descriptive statistics
- Correlation analysis
- Late-delivery comparison by shipping mode
- Late-delivery comparison by market
- Shipping-time distribution
- Top product-category sales analysis
- Correlation-matrix visualization
- Automated insight generation
- Automated test
- Week 3 Word report

### Run

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the complete pipeline:

```bash
python src/run_week3.py
```

Generated files:

- `outputs/descriptive_statistics.csv`
- `outputs/correlation_matrix.csv`
- `outputs/eda_insights.md`
- `visualizations/*.png`

Run tests:

```bash
pip install pytest
python -m pytest
```

### Important

The raw CSV is included in this ZIP for local reproducibility. Before publishing
the repository publicly, check the dataset's license and remove the CSV if its
redistribution is not permitted.

### Project progression

Week 1 → Strategic planning  
Week 2 → Cleaning and preprocessing  
Week 3 → EDA and visualization  
Week 4 → Predictive modeling and optimization
