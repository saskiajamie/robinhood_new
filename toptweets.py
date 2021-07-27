import pandas as  pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Open file
df = pd.read_csv ('./cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()


# Create dataframe of top twenty tweets per day by likes
top_20_by_day = []
for i in df.groupby('dates')['likes'].nlargest(20).index:
    top_20_by_day.append(i[1])
    
top_20_by_day = df.loc[top_20_by_day]
top_20_by_day.shape


# Proportion of sentiments of top twenty tweets by day
sent_top_20_by_day = top_20_by_day.groupby('dates')['svaluenltk'].value_counts(normalize=True).unstack()

# Plot a stacked line graph
p1 = sent_top_20_by_day.plot.area(stacked = True, figsize=(15,8),
                           color = ['red', 'goldenrod', 'green'], alpha = .70, fontsize=12)

p1.set_title('Sentiment of Daily Top Twenty Tweets', fontsize=12, pad=10)
p1.set_xlabel('Date', fontsize=12)
p1.set_ylabel('Sentiment (%)', fontsize=12, labelpad=10)
plt.setp(p1.get_xticklabels(), fontsize=12)
plt.setp(p1.get_yticklabels(), fontsize=12)
p1.legend(['Negative', 'Neutral', 'Positive'], facecolor='white', framealpha=1, fontsize=12)

plt.show()

# Create dataframes for positive, neutral and negative sentiment
positive_df = df[df['svaluenltk'] == 'positive']
neutral_df = df[df['svaluenltk'] == 'neutral']
negative_df = df[df['svaluenltk'] == 'negative']

positive_df.shape, neutral_df.shape, negative_df.shape

df['svaluenltk'].value_counts()

#Negative sentiments per day in bar chart
p2 = negative_df['dates'].value_counts().plot(kind='bar', figsize=(10,6), alpha = .70, fontsize=12)

p2.set_title('Num of Negative Tweets per day', fontsize=12, pad=10)
p2.set_xlabel('Date', fontsize=12, labelpad=10)
p2.set_ylabel('Sentiment', fontsize=12, labelpad=10)

plt.show()

#Negative sentiments per day in bar chart
p2 = positive_df['dates'].value_counts().plot(kind='bar', figsize=(10,6), alpha = .70, fontsize=12)

p2.set_title('Num of Positive Tweets per day', fontsize=12, pad=10)
p2.set_xlabel('Date', fontsize=12, labelpad=10)
p2.set_ylabel('Sentiment', fontsize=12, labelpad=10)

plt.show()

#Negative sentiments per day in bar chart
p2 = neutral_df['dates'].value_counts().plot(kind='bar', figsize=(10,6), alpha = .70, fontsize=12)

p2.set_title('Num of Neutral Tweets per day', fontsize=12, pad=10)
p2.set_xlabel('Date', fontsize=12, labelpad=10)
p2.set_ylabel('Sentiment', fontsize=12, labelpad=10)

plt.show()

negative_df['dates'].value_counts()
neutral_df['dates'].value_counts()
positive_df['dates'].value_counts()

