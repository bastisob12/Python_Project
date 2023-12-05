#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


diwali_data_sales=pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Project_DataAnalyst\Python project\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv')


# In[ ]:


print(diwali_data_sales)


# diwali_data_sales.shape

# In[ ]:


diwali_data_sales.info()


# diwali_data_sales.head(50)

# diwali_data_sales.tail(50)

# diwali_data_sales.drop(["Status","unnamed1"],axis=1)

# 

# diwali_data_sales.isnull().sum()

# diwali_data_sales.describe()

# diwali_data_sales.sort_values(by=["Amount"])

# diwali_data_sales.columns 

# diwali_data_sales.rename(columns={'Marital_Status':'Shadi'})

# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


ax=sns.countplot(x="Gender",data=diwali_data_sales)


# In[ ]:


ax=sns.countplot(x="Gender",data=diwali_data_sales)
for bars in ax.containers:
    ax.bar_label(bars)


# In[92]:


sns.barplot(x='Gender',y='Amount',data=diwali_data_sales )


# In[105]:


diwali_data_sales_v1=diwali_data_sales.groupby(['Zone'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[101]:


diwali_data_sales_v1


# In[108]:


ax=sns.countplot(x='Age Group',hue='Gender',data= diwali_data_sales )


# In[ ]:





# # STATE
# 

# In[112]:


#TOTAL NUMBER OF ORDERS FROM 10 STATES
diwali_data_sales_v2=diwali_data_sales.groupby(['State'],as_index= False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)


# In[113]:


diwali_data_sales_v2


# In[122]:


sns.set(rc={'figure.figsize':(19,5)})
ax=sns.barplot(x='State',y='Orders',data= diwali_data_sales_v2)


# In[125]:


sns.set(rc={'figure.figsize':(20,10)})
ax=sns.countplot(x='Occupation',data= diwali_data_sales)


# In[ ]:sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

# In[]:sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)

#In: sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')




