import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Open file
df = pd.read_csv ('./cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()

#Sentiment Analysis
def fetch_sentiment_using_SIA(text):
    sid = SentimentIntensityAnalyzer()
    polarity = sid.polarity_scores(text)
    return 'neg' if polarity['neg'] > polarity['pos'] else 'pos'

sentiments_using_SIA = df.cleantext.apply(lambda text: fetch_sentiment_using_SIA(text))

sp = pd.DataFrame(sentiments_using_SIA.value_counts())

#Visualizing the results
label = 'Positive Words','Negative Words'
color = ['green', 'red']

print (sp)


plt.pie(sp, explode=None, labels=label, autopct='%1.1f%%', colors=color)

#draw center circle hole
cc = plt.Circle((0,0),0.75,fc='white')
fig = plt.gcf()
fig.gca().add_artist(cc)

#display
plt.tight_layout()
plt.title('Robinhood Tweets Polarity Chart')
plt.axis('equal')
plt.show()