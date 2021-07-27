import pandas as  pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Open file
df = pd.read_csv ('./cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()

#Grouping and perform count over each group
dates_num =  df.groupby('dates')['dates'].count()
print(dates_num)

# Proportion of sentiments by day
df.groupby('dates')['svaluenltk'].value_counts(normalize=True).unstack()

# Proportion of sentiments by day
sent_by_day = df.groupby('dates')['svaluenltk'].value_counts(normalize=True).unstack()

# Plot a stacked line graph
p1 = sent_by_day.plot.area(stacked = True, figsize=(15,8),
                           color = ['red', 'goldenrod', 'green'], alpha = 0.7, fontsize=12)

p1.set_title('Tweet Sentiment Distribution Over Time', fontsize=12, pad=12)
p1.set_xlabel('Date', fontsize=12)
p1.set_ylabel('Sentiment (%)', fontsize=12, labelpad=12)
p1.legend(['Negative', 'Neutral', 'Positive'], facecolor='white', framealpha=1, fontsize=12)
plt.setp(p1.get_xticklabels(), fontsize=12)
plt.setp(p1.get_yticklabels(), fontsize=12);

plt.show()



