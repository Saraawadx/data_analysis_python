#!/usr/bin/env python
# coding: utf-8

# In[11]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ad1d7e12-04bb-41de-8d80-358f67a61020',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[30]:


import pandas as pd

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[13]:


df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')

df


# In[34]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'ad1d7e12-04bb-41de-8d80-358f67a61020',
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df

    if not os.path.isfile(r'C:\Users\s.abdelraheem\Desktop\Data Science\API.csv'):
        df.to_csv(r'C:\Users\s.abdelraheem\Desktop\Data Science\API.csv', header='column_names')
    else:
        df.to_csv(r'C:\Users\s.abdelraheem\Desktop\Data Science\API.csv',mode='a', header=False)


# In[35]:


import os
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API runner completed successfully!')
    sleep(60) #sleep for 1 minute
exit()


# In[36]:


df3 = pd.read_csv(r'C:\Users\s.abdelraheem\Desktop\Data Science\API.csv')
df3


# In[42]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[43]:


df3


# In[44]:


df4 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df4


# In[45]:


df5 = df4.stack()
df5


# In[46]:


type(df5)


# In[47]:


df6 = df5.to_frame(name='values')
df6


# In[48]:


type(df6)


# In[50]:


index = pd.Index(range(90))

df7 = df6.reset_index()
df7


# In[51]:


df8 = df7.rename(columns={'level_1': 'percent_change'})
df8


# In[54]:


df8['percent_change'] = df8['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df8


# In[55]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[72]:


sns.catplot(x='percent_change', y='values', hue='name', data=df8, kind='point', aspect = 2)


# In[66]:


df10 = df3[['name','quote.USD.price','timestamp']]
df10 = df10.query("name == 'Bitcoin'")
df10


# In[71]:


sns.set_theme(style="darkgrid")

sns.lineplot(x='timestamp', y='quote.USD.price', data = df10)


# In[ ]:




