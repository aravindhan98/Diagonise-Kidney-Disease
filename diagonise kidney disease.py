
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from keras.layers import Dropout



# In[2]:


df=pd.read_csv('kindney_disease.csv')


# In[3]:


df = pd.read_csv('epidemic.csv')


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# In[8]:


for i in ['age','Bb','sg','al','su'];
    dif[i].fillna(df[i].mean(),inplace=true)


# In[9]:


sns.countplot(data=df,x='rbc')
 df['rbc'].fillna('normal',inplace=true)

