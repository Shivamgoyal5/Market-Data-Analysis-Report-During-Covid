import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# Load the Excel file into DataFrame
df = pd.read_excel('GR01.xlsx', skiprows=1)
df1 = pd.read_excel('GR03.xlsx', skiprows=1)

df = df.iloc[:-1]
df1 = df1.iloc[:-1]

# Extract numerical data from DataFrame columns
x = df.iloc[:, 3].values
y = df1.iloc[:, 3].values

x_log = np.log(x)
y_log = np.log(y)

# Calculate quantiles for the two datasets
quantiles_x = np.quantile(x_log, np.linspace(0.01, 0.99, 100))
quantiles_y = np.quantile(y_log, np.linspace(0.01, 0.99, 100))

# Sort the quantiles arrays
quantiles_x_sorted = np.sort(quantiles_x)
quantiles_y_sorted = np.sort(quantiles_y)

plt.scatter(quantiles_x_sorted, quantiles_y_sorted, color='blue', alpha=0.5)
plt.plot([np.min(quantiles_x_sorted), np.max(quantiles_x_sorted)], [np.min(quantiles_y_sorted), np.max(quantiles_y_sorted)], color='red', linestyle='--')  # Diagonal line for reference
plt.grid(True)
plt.savefig("Comparison_2018")
plt.show()  