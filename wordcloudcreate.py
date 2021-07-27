import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#Open file
df = pd.read_csv ('./cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()

#Joinings the dataframe into a long string
text = " ".join(twt for twt in df.cleantext)
print ("There are {} words in the cleaned tweets dataset.".format(len(text)))

#WordCloud
wordcloud = WordCloud(width=1200, height=800, random_state=22, max_font_size=150, relative_scaling=0.5, color_func=lambda *args, **kwargs: "white", colormap='Dark2').generate(text)

#Display the generated image:
plt.figure(figsize = (10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()