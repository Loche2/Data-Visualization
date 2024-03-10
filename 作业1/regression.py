import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Create a color map
colors = ['b', 'g', 'r', 'c']

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Calculate and plot the least squares regression line for each dataset
for i, color in zip(['I', 'II', 'III', 'IV'], colors):
    dataset = df[df['dataset'] == i]
    x = dataset['x']
    y = dataset['y']
    slope, intercept = np.polyfit(x, y, 1)
    ax.plot(x, y, 'o', color=color, label=f'Dataset {i}')
    ax.plot(x, slope*x + intercept, color=color, label=f'Regression line {i}: y = {slope:.2f}x + {intercept:.2f}')
    print(f'Regression line for Dataset {i}: y = {slope:.2f}x + {intercept:.2f}')

# Set title and labels
ax.set_title('Anscombe\'s quartet with regression lines')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Show legend
ax.legend()

# Show the plot
plt.show()