import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(x='total_bill', y='tip', data=df[df['sex'] == 'Male'], hue='smoker')
plt.title('Взаимосвязь total_bill и tip для Male')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

plt.subplot(1, 2, 2)
sns.scatterplot(x='total_bill', y='tip', data=df[df['sex'] == 'Female'], hue='smoker')
plt.title('Взаимосвязь total_bill и tip для Female')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

plt.tight_layout()
plt.show()
