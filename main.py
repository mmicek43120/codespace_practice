import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load a dataset
data = load_iris()
df = pd.DataFrame(data=data.data, columns=data.feature_names)

# Basic data exploration
print(df.head())

# Simple plot
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width')
plt.show()
