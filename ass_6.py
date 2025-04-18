# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RcDD4xcSm4bKc8PElVurV4DY7swA0B_G
"""

#q1
import numpy as np
import matplotlib.pyplot as plt
M = float (input ("Enter value for M: "))
x = np.linspace(-10, 10, 100)
y1 = M*x*x
y2 = M * np.sin(x)
plt.plot(x, y1, 'p--', label='y = M*x^2')
plt.plot(x, y2, 'b-', label='y = M*sin(x)')
plt. legend()
plt.grid()
plt.title( 'Mathematical Functions')
plt.show()

#q2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Subject': ['Math', 'Science', 'English', 'History', 'Computer Science'],
        'Score': [85, 90, 78, 88, 95]}

df = pd.DataFrame(data)

sns.barplot(x='Subject', y='Score', hue='Subject', data=df, palette='pastel', legend=False)
for i, score in enumerate(df['Score']):
    plt.text(i, score + 1, str(score))


plt.title("Scores by Subject")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.grid(True)
plt.show()

#q3
import numpy as np
import matplotlib.pyplot as plt
roll_number = 102317059
np.random.seed(roll_number)


values = np.random.randn(50)


fig, axes = plt.subplots(1, 2, figsize=(10, 5))


axes[0].plot(np.cumsum(values),linestyle='-', color='b')
axes[0].set_title("Cumulative Sum Line Plot")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Cumulative Sum")
axes[0].grid(True)


axes[1].scatter(range(50), values, color='r', alpha=0.6)
axes[1].set_title("Scatter Plot with Random Noise")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Random Value")
axes[1].grid(True)

plt.show()

#q4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_url = "https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv"
df = pd.read_csv(data_url)

sns.set_style("whitegrid")

# 1. Line plot for Total Profit
plt.figure(figsize=(10, 5))
sns.lineplot(x=df['month_number'], y=df['total_profit'],color='b')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

# 2. Multiline plot for all product sales
plt.figure(figsize=(10, 6))
for column in df.columns[1:6]:
    sns.lineplot(x=df['month_number'], y=df[column], label=column)
plt.title("Product Sales per Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# 3. Bar chart for all features
plt.figure(figsize=(12, 6))
for column in df.columns[1:]:
    plt.bar(df['month_number'], df[column], label=column, alpha=0.7)
plt.title("Bar Chart for All Features")
plt.xlabel("Month")
plt.ylabel("Values")
plt.legend(title="Features")
plt.grid(True)
plt.show()