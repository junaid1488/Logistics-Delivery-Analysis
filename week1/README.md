# Logistics Delivery Performance Analysis and Late-Delivery Prediction

## Week 1 — Strategic Planning and Data Exploration

This repository contains the fully coded Week 1 implementation for the logistics
data-science internship project.

### What is included

- Actual DataCo supply-chain CSV used by the project
- Dataset loading and validation
- Automated data-quality profiling
- Missing-value and duplicate analysis
- KPI calculation
- Strategic roadmap output
- Automated test
- Week 1 Word report

### Project KPIs

- On-Time Delivery Rate
- Late Delivery Rate
- Average Shipping Time
- Average Delivery Delay
- Late-Delivery Risk

### Run the project

Create and activate a virtual environment:

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

Run Week 1:

```bash
python run_week1.py
```

The script creates:

- `outputs/data_profile.csv`
- `outputs/week1_kpis.csv`
- `outputs/week1_strategy_output.md`

Run tests:

```bash
python -m pytest
```

### Important GitHub note

The raw CSV is included in this ZIP so the project runs immediately, but
`.gitignore` excludes `data/raw/*.csv`. For a public GitHub repository, do not
commit the raw dataset if its redistribution/license terms do not permit it.
Instead, use `data/README.md` and the public dataset source.

### Four-week project

Week 1 → Strategic planning  
Week 2 → Data cleaning and preprocessing  
Week 3 → EDA and visualization  
Week 4 → Predictive modeling and optimization
