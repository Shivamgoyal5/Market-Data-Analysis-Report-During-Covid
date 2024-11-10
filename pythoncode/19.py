import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
df = pd.read_excel('GR04.xlsx',skiprows=1)

x = df.iloc[:, 1] 
y = df.iloc[:, 9]  

plt.figure(figsize=(12,8))

# Plotting
plt.plot(x, y)
plt.xlabel('Country')
plt.ylabel('Expenditures for Passenger transport items, 2019')
plt.grid(True)  # Add grid

plt.savefig('Expenditures for Passenger transport items, 2019 .png')