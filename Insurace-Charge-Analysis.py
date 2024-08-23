#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


medical_dt=pd.read_csv('insurance.csv')


# In[3]:


medical_dt


# In[4]:


medical_dt.info()


# In[5]:


medical_dt.describe()


# In[6]:


get_ipython().system('pip install plotly matplotlib seaborn --quiet')


# In[7]:


import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


sns.scatterplot(data=medical_dt,x="bmi",y="charges")


# In[9]:


sns.scatterplot(data=medical_dt,x="bmi",y="charges",hue="region",style="region", size="region",
    sizes=(20, 200), legend="full")


# In[10]:


sns.relplot(data=medical_dt,x="bmi",y="charges",col="smoker",style="region",
    kind="scatter",)


# In[11]:


plt.title("Distribution of BMI ")
plt.hist(medical_dt.bmi);


# In[12]:


plt.hist(medical_dt.bmi, bins=5);


# In[13]:


plt.hist(medical_dt.bmi, bins=np.arange(20, 50, 10));


# In[14]:


medical_dt.age.describe()


# In[15]:


fig = px.histogram(medical_dt, 
                   x='age', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.2)
fig.show()


# In[16]:


fig = px.histogram(medical_dt, 
                   x='bmi', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.2)
fig.show()


# Visualize the distribution of medical charges in connection with other factors like "sex" and "region"

# In[17]:


fig = px.histogram(medical_dt, 
                   x='charges', 
                   marginal='box',
                   color='smoker',
                   color_discrete_sequence=['green', 'grey'], 
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.2)
fig.show()


# In[18]:


fig = px.histogram(medical_dt, 
                   x='charges', 
                   marginal='box',
                   color='sex',
                   color_discrete_sequence=['green', 'grey'], 
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.2)
fig.show()


# In[19]:


fig = px.histogram(medical_dt, 
                   x='charges', 
                   marginal='box',
                   color='region',
                   color_discrete_sequence=['green', 'grey','orange','blue'], 
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.2)
fig.show()


# Smoker
# 
# Let's visualize the distribution of the "smoker" column (containing values "yes" and "no") using a histogram.

# In[20]:


medical_dt.smoker.value_counts()


# In[21]:


px.histogram(medical_dt, x='smoker', color='sex', title='Smoker')


# In[22]:


px.histogram(medical_dt, x='smoker', color='region', title='Smoker')


# In[23]:


px.histogram(medical_dt, x='region', color='children', title='region')


# In[25]:


fig=px.scatter(medical_dt,
               x='age',
               y='charges',
               color='smoker',
               opacity=0.8,
                hover_data=['sex','region'], 
                 title='Age vs. Charges')
fig.update_traces(marker_size=5)
fig.show()
               


# We can make the following observations from the above chart:
# 
# * The general trend seems to be that medical charges increase with age, as we might expect. However, there is significant variation at every age, and it's clear that age alone cannot be used to accurately determine medical charges.
# 
# 
# * We can see three "clusters" of points, each of which seems to form a line with an increasing slope:
# 
#      1. The first and the largest cluster consists primary of presumably "healthy non-smokers" who have relatively low medical charges compared to others
#      
#      2. The second cluster contains a mix of smokers and non-smokers. It's possible that these are actually two distinct but overlapping clusters: "non-smokers with medical issues" and "smokers without major medical issues".
#      
#      3. The final cluster consists exclusively of smokers, presumably smokers with major medical issues that are possibly related to or worsened chart?
# >
# > ???

# In[29]:


fig=px.scatter(medical_dt,x='bmi',y='charges',color='smoker',opacity=0.8,
               hover_data=['sex','region'], title='BMI VS Charges')
fig.update_traces(marker_size=5)
fig.show()


# In[31]:


px.violin(medical_dt,x='children',y='charges')


# In[32]:


px.violin(medical_dt,x='sex',y='charges')


# ### Correlation
# 
# As you can tell from the analysis, the values in some columns are more closely related to the values in "charges" compared to other columns. E.g. "age" and "charges" seem to grow together, whereas "bmi" and "charges" don't.
# 
# This relationship is often expressed numerically using a measure called the _correlation coefficient_, which can be computed using the `.corr` method of a Pandas series.

# In[33]:


medical_dt.charges.corr(medical_dt.age)


# In[38]:


smoker_values={'no':0,'yes':1}
smoker_numeric=medical_dt.smoker.map(smoker_values)
medical_dt.charges.corr(smoker_numeric)


# In[ ]:




