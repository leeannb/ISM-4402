#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[3]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades','BS','MS','PhD'])
df


# In[4]:


df.count()


# In[5]:


df.mean()


# In[6]:


df.std()


# In[7]:


df.min()


# In[8]:


df.max()


# In[9]:


df.quantile(.25)


# In[10]:


df.quantile(.5)


# In[11]:


df.quantile(.75)


# In[ ]:




