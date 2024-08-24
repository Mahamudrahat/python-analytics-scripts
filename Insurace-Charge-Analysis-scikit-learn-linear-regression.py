#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
import numpy as np


# In[124]:


medical_dt=pd.read_csv('insurance.csv')


# In[125]:


medical_dt


# In[126]:


medical_dt.info()


# In[127]:


medical_dt.describe()


# In[128]:


get_ipython().system('pip install plotly matplotlib seaborn --quiet')


# In[129]:


import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[130]:


sns.scatterplot(data=medical_dt,x="bmi",y="charges")


# In[131]:


sns.scatterplot(data=medical_dt,x="bmi",y="charges",hue="region",style="region", size="region",
    sizes=(20, 200), legend="full")


# In[132]:


sns.relplot(data=medical_dt,x="bmi",y="charges",col="smoker",style="region",
    kind="scatter",)


# In[133]:


plt.title("Distribution of BMI ")
plt.hist(medical_dt.bmi);


# In[134]:


plt.hist(medical_dt.bmi, bins=5);


# In[135]:


plt.hist(medical_dt.bmi, bins=np.arange(20, 50, 10));


# In[136]:


medical_dt.age.describe()


# In[137]:


fig = px.histogram(medical_dt, 
                   x='age', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.2)
fig.show()


# In[138]:


fig = px.histogram(medical_dt, 
                   x='bmi', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.2)
fig.show()


# Visualize the distribution of medical charges in connection with other factors like "sex" and "region"

# In[139]:


fig = px.histogram(medical_dt, 
                   x='charges', 
                   marginal='box',
                   color='smoker',
                   color_discrete_sequence=['green', 'grey'], 
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.2)
fig.show()


# In[140]:


fig = px.histogram(medical_dt, 
                   x='charges', 
                   marginal='box',
                   color='sex',
                   color_discrete_sequence=['green', 'grey'], 
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.2)
fig.show()


# In[141]:


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

# In[142]:


medical_dt.smoker.value_counts()


# In[143]:


px.histogram(medical_dt, x='smoker', color='sex', title='Smoker')


# In[144]:


px.histogram(medical_dt, x='smoker', color='region', title='Smoker')


# In[145]:


px.histogram(medical_dt, x='region', color='children', title='region')


# In[146]:


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

# In[147]:


fig=px.scatter(medical_dt,x='bmi',y='charges',color='smoker',opacity=0.8,
               hover_data=['sex','region'], title='BMI VS Charges')
fig.update_traces(marker_size=5)
fig.show()


# In[148]:


px.violin(medical_dt,x='children',y='charges')


# In[149]:


px.violin(medical_dt,x='sex',y='charges')


# ### Correlation
# 
# As you can tell from the analysis, the values in some columns are more closely related to the values in "charges" compared to other columns. E.g. "age" and "charges" seem to grow together, whereas "bmi" and "charges" don't.
# 
# This relationship is often expressed numerically using a measure called the _correlation coefficient_, which can be computed using the `.corr` method of a Pandas series.

# In[150]:


medical_dt.charges.corr(medical_dt.age)


# In[151]:


smoker_values={'no':0,'yes':1}
smoker_numeric=medical_dt.smoker.map(smoker_values)
medical_dt.charges.corr(smoker_numeric)


# In[152]:


numeric_df = medical_dt.select_dtypes(include=['number'])
numeric_df.corr()


# In[153]:


sns.heatmap(numeric_df.corr(),cmap='Reds',annot=True)
plt.title('Correlation Matrix')


# ## Linear Regression using a Single Feature
# 
# We now know that the "smoker" and "age" columns have the strongest correlation with "charges". Let's try to find a way of estimating the value of "charges" using the value of "age" for non-smokers. First, let's create a data frame containing just the data for non-smokers..

# In[154]:


non_smoker_df=medical_dt[medical_dt.smoker=='no']


# In[155]:


plt.title('Age vs, Charges')
sns.scatterplot(data=non_smoker_df,x='age',y='charges',alpha=0.7,s=15)


# Apart from a few exceptions, the points seem to form a line. We'll try and "fit" a line using this points, and use the line to predict charges for a given age. A line on the X&Y coordinates has the following formula:
# 
# $y = wx + b$
# 
# The line is characterized two numbers: $w$ (called "slope") and $b$ (called "intercept"). 
# 
# ### Model
# 
# In the above case, the x axis shows "age" and the y axis shows "charges". Thus, we're assuming the following relationship between the two:
# 
# $charges = w \times age + b$
# 
# We'll try determine $w$ and $b$ for the line that best fits the data. 
# 
# * This technique is called _linear regression_, and we call the above equation a _linear regression model_, because it models the relationship between "age" and "charges" as a straight line. 
# 
# * The numbers $w$ and $b$ are called the _parameters_ or _weights_ of the model.
# 
# * The values in the "age" column of the dataset are called the _inputs_ to the model and the values in the charges column are called "targets". 
# 
# Let define a helper function `estimate_charges`, to compute $charges$, given $age$, $w$ and $b$.

# In[156]:


def estimate_charges(age,w,b):
    return w*age+b


# The `estimate_charges` function is our very first _model_.
# 
# Let's _guess_ the values for $w$ and $b$ and use them to estimate the value for charges.

# In[157]:


w=50
b=100
ages=non_smoker_df.age
estimated_charges=estimate_charges(ages,w,b)


# In[158]:


target = non_smoker_df.charges

plt.plot(ages, estimated_charges, 'r', alpha=0.9);
plt.scatter(ages, target, s=8,alpha=0.8);
plt.xlabel('Age');
plt.ylabel('Charges')
plt.legend(['Estimate', 'Actual']);


# In[166]:


def try_parameters(w,b):
    ages=non_smoker_df.age
    target=non_smoker_df.charges
    estimated_charges=estimate_charges(age,w,b)


# In[167]:


print(estimated_charges)


# In[168]:


plt.plot(ages,estimated_charges,'r',alpha=0.9);


# In[169]:


plt.plot(ages,estimated_charges,'r',alpha=0.9);
plt.scatter(ages, target, s=8,alpha=0.8);
plt.xlabel('Age');
plt.ylabel('Charges')
plt.legend(['Estimate', 'Actual']);


# In[171]:


def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges
    
    estimated_charges = estimate_charges(ages, w, b)
    
    plt.plot(ages, estimated_charges, 'r', alpha=0.9);
    plt.scatter(ages, target, s=8,alpha=0.8);
    plt.xlabel('Age');
    plt.ylabel('Charges')
    plt.legend(['Estimate', 'Actual']);


# In[172]:


try_parameters(60, 200)


# As we change the values, of $w$ and $b$ manually, trying to move the line visually closer to the points, we are _learning_ the approximate relationship between "age" and "charges". 
# 
# Wouldn't it be nice if a computer could try several different values of `w` and `b` and _learn_ the relationship between "age" and "charges"? To do this, we need to solve a couple of problems:
# 
# 1. We need a way to measure numerically how well the line fits the points.
# 
# 2. Once the "measure of fit" has been computed, we need a way to modify `w` and `b` to improve the the fit.
# 
# If we can solve the above problems, it should be possible for a computer to determine `w` and `b` for the best fit line, starting from a random guess.

# ### Loss/Cost Function
# 
# We can compare our model's predictions with the actual targets using the following method:
# 
# * Calculate the difference between the targets and predictions (the differenced is called the "residual")
# * Square all elements of the difference matrix to remove negative values.
# * Calculate the average of the elements in the resulting matrix.
# * Take the square root of the result
# 
# The result is a single number, known as the **root mean squared error** (RMSE). The above description can be stated mathematically as follows: 
# 
# <img src="https://i.imgur.com/WCanPkA.png" width="360">
# 
# Geometrically, the residuals can be visualized as follows:
# 
# <img src="https://i.imgur.com/ll3NL80.png" width="420">
# 
# Let's define a function to compute the RMSE.

# In[173]:


def rmse(targets,predictions):
    return np.sqrt(np.mean(np.square(targets-predictions)))


# In[174]:


w=50
b=100


# In[175]:


targets = non_smoker_df['charges']
predicted = estimate_charges(non_smoker_df.age, w, b)


# In[176]:


rmse(targets,predicted)


# In[177]:


get_ipython().system('pip install scikit-learn --quiet')


# In[178]:


from sklearn.linear_model import LinearRegression


# In[179]:


model=LinearRegression()


# In[180]:


help(model.fit)


# In[181]:


inputs=non_smoker_df[['age']]


# In[184]:


print(inputs.shape)


# In[185]:


inputs = non_smoker_df[['age']]
targets = non_smoker_df.charges
print('inputs.shape :', inputs.shape)
print('targes.shape :', targets.shape)


# In[186]:


model.fit(inputs,targets)


# In[187]:


predictions=model.predict(inputs)


# In[188]:


predictions


# In[191]:


model.predict(np.array([[34]]))


# In[192]:


model.predict(np.array([[23], 
                        [37], 
                        [61]]))


# In[193]:


rmse(targets, predictions)


# In[194]:


# w
model.coef_


# In[195]:


# b
model.intercept_


# In[196]:


try_parameters(model.coef_, model.intercept_)


# In[197]:


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[198]:


try_parameters(model.coef_, model.intercept_)


# In[ ]:




