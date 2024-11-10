import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Read the Excel file, specifying thousands=','
df = pd.read_excel('newGr.xlsx', thousands=',')

# Select column 2 (assuming it contains labels) and columns 3, 4, 5
x = df.iloc[:, 1].astype(str)  # Convert to string
y = pd.to_numeric(df.iloc[:, 3], errors='coerce')
z = pd.to_numeric(df.iloc[:, 4], errors='coerce')
m = pd.to_numeric(df.iloc[:, 5], errors='coerce')

bar_width = 0.2  # Adjust bar width for increased space between bars

# Generate numerical indices for x-positions
x_indices = range(len(x))

# Plot the bar graphs separately but in the same figure
plt.figure(figsize=(12, 6))  # Adjust figure size as needed
plt.bar(x_indices, y, width=bar_width, label='Number of Arrivals, 2018', color='mediumblue')
plt.bar([index + bar_width * 1.2 for index in x_indices], z, width=bar_width, label='Number of Arrivals, 2019', color='red')  # Adjust the spacing
plt.bar([index + bar_width * 2.4 for index in x_indices], m, width=bar_width, label='Number of Arrivals, 2020', color='grey')  # Adjust the spacing

# Set x-tick labels
plt.xticks([index + bar_width * 1.2 for index in x_indices], x, rotation=90)  # Rotate x-labels for better readability

# Set y-axis limits
plt.ylim(30000, 20000000)  # Adjust the limits as needed

# Format y-axis labels in scientific notation
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))

plt.legend()
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
plt.savefig("2.png")