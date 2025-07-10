#!/usr/bin/env python
# coding: utf-8

# # Web Scraping - USA top Revenue Companies

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[7]:


soup.find_all('table')[0]


# In[8]:


table = soup.find_all('table')[0]


# In[17]:


world_titles = table.find_all('th')


# In[19]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[21]:


import pandas as pd


# In[23]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[24]:


column_data = table.find_all('tr')


# In[29]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[30]:


df


# In[32]:


df.to_csv(r'C:\Users\s.abdelraheem\Desktop\New folder (2)\Web Scraping\US Copanies.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




