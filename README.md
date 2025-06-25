# Bill Reconciliation Dashboard

This project analyzes synthetic billing data to detect discrepancies between expected and billed amounts.

## Features
- Calculates discrepancies based on unit price × usage
- Detects billing mismatches > 0.01
- Interactive charts using Plotly
- Summary table of issues by month
- Heatmap showing affected customers

## Tech Stack
- Python, pandas
- Jupyter Notebook
- Plotly
- Synthetic dataset generator

## Output
- CSV output of analysis

## Run Locally
```bash
pip install pandas plotly
python data/generate_data.py
jupyter notebook notebook/bill_reconciliation.ipynb
