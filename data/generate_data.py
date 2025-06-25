import pandas as pd
import numpy as np 
import random

np.random.seed(42)

customers = [f"C{str(i).zfill(3)}" for i in range(1, 21)]
months = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05"]

data = []

for customer in customers:
    for month in months:
        usage_units = np.random.randint(50, 200)
        unit_price = round(np.random.uniform(1.0, 1.5), 2)
        expected = usage_units * unit_price

        error = np.random.choice([0,0,0,5,-5, 10, -10])
        billed_amout = round(expected + error, 2)

        data.append([customer, month, billed_amout, usage_units, unit_price])

df = pd.DataFrame(data, columns=["customer_id", "bill_month", "billed_amount", "usage_units", "unit_price"])
df.to_csv("data/synthetic_billing_data.csv", index=False)

print("Synthetic data generated.")
