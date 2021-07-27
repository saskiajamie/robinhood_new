import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Boxplot Tweet length

#Open file
df = pd.read_csv ('./0_results_robinhood.csv', index_col=None, header=0)
df.append(df)
df.head()

# adding a column to represent the length of the tweet
df['prelen'] = df['text'].str.len()
df['cleanlen'] = df['cleantext'].str.len()

#Create column and boxplot with text length before and after cleaning
fig, ax = plt.subplots(figsize=(5, 5))
plt.boxplot(df.prelen)
plt.show()

fig, ax = plt.subplots(figsize=(5, 5))
plt.boxplot(df.cleanlen)
plt.show()
