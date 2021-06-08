#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd


# In[19]:


pew = pd.read_csv('C:\\Users\\bly\\Desktop\\pew.csv')


# In[20]:


pew.head()


# In[21]:


pew.info()


# In[22]:


pew.columns


# In[23]:


pew.describe()


# In[30]:


long_pew = pd.melt(
    pew,
    id_vars='religion', 
    var_name = 'income', 
    value_name = 'count')


# In[33]:


long_pew.head()


# In[34]:


billboard = pd.read_csv('C:\\Users\\bly\\Desktop\\data\\billboard.csv')


# In[36]:


billboard


# In[41]:


long_billboard = pd.melt(
    billboard,
    id_vars=['year','artist','track','time','date.entered'],
    var_name='week',
    value_name='rating')


# In[42]:


long_billboard


# In[49]:


ebola = pd.read_csv('C:\\Users\\bly\\Desktop\\data\\country_timeseries.csv')


# In[50]:


ebola


# In[52]:


long_ebola = pd.melt(ebola,
                     id_vars=['Date', 'Day'],
                     value_name='Count'
                    )
long_ebola


# In[54]:


variable_split = long_ebola['variable'].str.split('_')
variable_split


# In[57]:


long_ebola['Status'] = variable_split.str[0]
long_ebola['Country'] = variable_split.str[1]


# In[58]:


long_ebola


# In[61]:


del long_ebola['variable']


# In[62]:


long_ebola


# In[64]:


weather = pd.read_csv('C:\\Users\\bly\\Desktop\\data\\weather.csv')


# In[65]:


weather


# In[68]:


long_weather = pd.melt( 
                       weather,
                       id_vars=['id','year','month','element'],
                       var_name='day',
                       value_name='temp'
                      )


# In[69]:


long_weather


# In[90]:


pivot_weather = pd.pivot_table(
                         long_weather,
                         index=['id','year','month','day'],
                         columns='element',
                         values='temp'      
                        )


# In[93]:


pivot_weather.reset_index()


# In[95]:


long_billboard


# In[99]:


long_billboard[long_billboard['track']=='Loser']


# In[101]:


billboard_songs = long_billboard[['year','artist','track','time']]
billboard_songs


# In[102]:


billboard_songs = billboard_songs.drop_duplicates()
billboard_songs


# In[105]:


billboard_songs['id'] = range(len(billboard_songs))


# In[106]:


billboard_songs


# In[107]:


billboard_ratings = long_billboard.merge(
    billboard_songs,
    on=['year','artist','track','time']
)
billboard_ratings


# In[108]:


billboard_ratings = billboard_ratings[['id','date.entered','week','rating']]
billboard_ratings


# In[109]:


billboard_songs


# In[ ]:




