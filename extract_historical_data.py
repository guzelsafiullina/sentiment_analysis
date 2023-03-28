#!/usr/bin/env python
# coding: utf-8

# In[39]:


#pip install requests
#
#
# In[40]:
#
#
#pip install termcolor

import pandas as pd
import requests
from termcolor import colored as cl


api_key = '642330f961ef29.57304407'
url = 'https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}&limit={n_news}&offset={offset}&from={start_date}&to={end_date}'


def get_customized_news(stock, start_date, end_date, n_news, api_key, offset = 0):
    url = f'https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}&limit={n_news}&offset={offset}&from={start_date}&to={end_date}'
    news_json = requests.get(url).json()
    
    news = []
    
    for i in range(len(news_json)):
        title = news_json[-i]['title']
        news.append(title)
        print(cl('{}. '.format(i+1), attrs = ['bold']), '{}'.format(title))
    
    return news, news_json

news, news_json = get_customized_news('AAPL', '2023-02-27', '2023-02-28', 15, api_key, 0)


news_df = pd.DataFrame.from_records(news_json)

date = '28.03.2023'
news_df.to_csv(f"""{date}_news.csv""")


