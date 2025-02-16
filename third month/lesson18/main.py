import numpy as np
import pandas, matplotlib.pyplot as plt, seaborn

df = seaborn.load_dataset('tips')

plt.figure(figsize=(8, 6))
plt.hist(df['time'], color='darkgreen', edgecolor='black')

plt.title('Гистограмма распределения признака "total_bill"')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')

plt.show()