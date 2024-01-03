import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Read the data from epa-sea-level.csv
df = pd.read_csv('epa-sea-level.csv')

# Create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Calculate the slope and y-intercept of the line of best fit
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Calculate the y value for the year 2050
y_2050 = slope * 2050 + intercept

# Plot the line of best fit over the top of the scatter plot
plt.plot(df['Year'], slope * df['Year'] + intercept, color='red')

# Create a new line of best fit just using the data from year 2000 through the most recent year in the dataset
df_new = df[df['Year'] >= 2000]
slope_new, intercept_new, r_value_new, p_value_new, std_err_new = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])

# Calculate the y value for the year 2050 using the new line of best fit
y_2050_new = slope_new * 2050 + intercept_new

# Plot the new line of best fit
plt.plot(df['Year'], slope_new * df['Year'] + intercept_new, color='green')

# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Display the plot
plt.show()

# Print the predictions for the sea level rise in 2050
print('Predicted sea level rise in 2050:', y_2050)
print('Predicted sea level rise in 2050, using the line of best fit from 2000:', y_2050_new)