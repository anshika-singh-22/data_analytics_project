import pandas as pd
import numpy as np

# 1. Create a simple synthetic dataset (our "relevant dataset")
np.random.seed(42) # For reproducibility
data = {
    'Age': np.random.randint(20, 60, 100),
    'Income_k': np.random.normal(50, 15, 100).round(2), # Normal distribution around 50k
    'Purchased_Product': np.random.choice(['Yes', 'No'], 100, p=[0.4, 0.6]),
    'Missing_Data': np.random.choice([1, 2, np.nan], 100, p=[0.7, 0.2, 0.1]) # Introduce anomalies
}
df = pd.DataFrame(data)

# 2. Explore the data structure (df.info()) and types
print("--- Data Structure and Data Types (df.info()) ---")
df.info() 

# 3. Identify trends, patterns, and anomalies (df.describe())
print("\n--- Descriptive Statistics (df.describe()) ---")
print(df.describe())

# 4. Detect potential data issues (Missing values)
print("\n--- Missing Value Check ---")
print(df.isnull().sum()) # Shows how many NaNs are in each column

# 5. Simple Trend/Pattern: Check distribution of a categorical variable
print("\n--- Trend: Purchased Product Distribution ---")
print(df['Purchased_Product'].value_counts(normalize=True)) # Normalize=True for percentages