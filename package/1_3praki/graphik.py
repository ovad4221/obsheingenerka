import pandas as pd
import matplotlib.pyplot as plt

# ggg
df = pd.read_csv('values.csv', quotechar=';')
print(df.head())

plt.figure()
plt.ylabel('voltage')
plt.xlabel('digit')
plt.plot(df['n'], df['v'])
plt.show()
