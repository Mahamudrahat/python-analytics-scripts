#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd


# In[70]:


titanic=pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Titanic.csv')


# In[71]:


titanic.head(1000)


# In[72]:


titanic.tail()


# In[73]:


data={"Name":["Rahim","karim"],
      "Age":[23,24],
      "Salary":[4000,80000]}
df=pd.DataFrame(data)
print(df)


# In[74]:


titanic.info()


# In[75]:


titanic.describe()


# In[76]:


titanic.isnull().sum()


# In[77]:


titanic["pclass"].duplicated().sum()


# In[78]:


titanic['age'].mean()


# In[79]:


import numpy as np


# In[80]:


titanic['age']=titanic['age'].replace(np.nan,29.88)


# In[81]:


titanic['fare'].mean()
titanic['fare']=titanic['fare'].replace(np.nan,33)


# In[82]:


titanic.isnull().sum()


# In[83]:


len(titanic[titanic['cabin'].notnull()])


# In[84]:


len(titanic)


# In[85]:


most_frequent_cabin = titanic['cabin'].mode()[0]


# In[86]:


most_frequent_cabin


# In[87]:


# Count the occurrences of each unique value in the 'cabin' column
cabin_counts = titanic['cabin'].value_counts(dropna=False)

# Display the result
print(cabin_counts)


# In[88]:


titanic['cabin']=titanic['cabin'].replace(np.nan,'Unknown')


# In[89]:


titanic.isnull().sum()


# In[90]:


[titanic['cabin'][0]


# In[91]:


most_frequent_cabin


# In[151]:


titanic[titanic['cabin']=='Unknown']


# In[97]:


titanic[titanic['embarked'].isnull()]


# In[100]:


frequent_embarked=titanic['embarked'].mode()[0]
print(frequent_embarked)


# In[103]:


# Count the occurrences of each unique value in the 'cabin' column
cabin_counts = titanic['embarked'].value_counts(dropna=False)

# Display the result
print(cabin_counts)


# In[102]:


titanic['embarked'].fillna('S',inplace=True)


# In[152]:


# Count the occurrences of each unique value in the 'cabin' column
cabin_counts = titanic['boat'].value_counts(dropna=False)

# Display the result
print(cabin_counts)


# In[109]:


titanic['boat']=titanic['boat'].replace(np.nan,'Unknown')


# In[157]:


# Retrieve only the duplicate rows
titanic[titanic['body'].notnull()]

# Display the duplicate rows
titanic[titanic[titanic['body'].notnull()].duplicated()]


# In[141]:


existing_body_values=set(titanic['body'].dropna().astype(int))
print(len(existing_body_values))


# In[143]:


def generate_unique_value():
    while True:
        random_value=np.random.randint(1,1360)
        if random_value not in existing_body_values:
            existing_body_values.add(random_value)
            return random_value
# Step 3: Replace NaN values with the generated unique values
titanic['body'] = titanic['body'].apply(lambda x: generate_unique_value() if np.isnan(x) else x)   


# In[144]:


titanic['body']


# In[146]:


titanic[titanic['body'].duplicated()]


# In[149]:


titanic.isnull().sum()


# In[148]:


titanic['home.dest']=titanic['home.dest'].replace(np.nan,'Unknown')


# In[ ]:




