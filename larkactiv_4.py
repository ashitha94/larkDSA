#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:





# In[4]:


data=pd.read_excel("CustomerChurn.xlsx")
data


# # 1. Compare churn count with respect to gender.

# In[23]:


plt.figure(figsize=(8,6))
sns.countplot(data['gender'],hue=data['Churn'])
plt.title('Churn count Vs Gender', fontsize=17)


# # 2. Find out how many female senior citizens there in the dataset

# In[11]:


data1=data[(data['gender']=='Female') & (data['SeniorCitizen']==1)]
data1['gender'].count()


# In[20]:


plt.figure(figsize=(4,6))
sns.countplot(x=data1['gender'])
plt.title("Count of female senior citizens ")


# # 3.Compare 'tenure' with 'Total Charges'

# In[21]:


plt.figure(figsize=(8,6))
plt.scatter(data['tenure'] , data['TotalCharges'] , s=8 , c='r')
plt.title("Tenure VS Total charges")
plt.xlabel('Tenure')
plt.ylabel('Total Charges')


# # 4. Find out which contract is preferred by the senior citizen.

# In[22]:


snr_cit=data[data['SeniorCitizen']==1]
snr_cit


# In[39]:


plt.figure(figsize=(6,6))
sns.countplot(snr_cit['Contract'],hue=snr_cit['Contract'])
plt.title('Contract preferred by senior citizen',fontweight='bold', fontsize=17)


# # 5. Comment on your finds on Payment Method?

# In[55]:


plt.figure(figsize=(6,6))
sns.countplot(data['PaymentMethod'])
plt.title('Preferred payment method vs count', fontsize=18)
plt.xticks(rotation=30)
plt.grid()


# In[58]:


plt.figure(figsize=(6,6))
sns.countplot(data['PaymentMethod'],hue=data['gender'])
plt.title('Preferred payment method by gender ', fontsize=18)
plt.xticks(rotation=30)
plt.grid()


# In[51]:


youngster=data[data['SeniorCitizen']==0]
plt.figure(figsize=(6,6))
sns.countplot(youngster['PaymentMethod'],hue=youngster['PaymentMethod'])
plt.title('PaymentMethod preferred by youngster',fontweight='bold', fontsize=17)
plt.xticks(rotation=30)
plt.grid()

plt.figure(figsize=(6,6))
sns.countplot(snr_cit['PaymentMethod'],hue=snr_cit['PaymentMethod'])
plt.title('PaymentMethod preferred by senior citizen',fontweight='bold', fontsize=17)
plt.xticks(rotation=30)
plt.grid()


# In[57]:


plt.figure(figsize=(6,6))
sns.countplot(data1['PaymentMethod'])
plt.title('Preferred payment method of female senior citizen', fontsize=18)
plt.xticks(rotation=30)
plt.grid()

data2=data[(data['gender']=='Male') & (data['SeniorCitizen']==1)]
plt.figure(figsize=(6,6))
sns.countplot(data2['PaymentMethod'])
plt.title('Preferred payment method of male senior citizen', fontsize=18)
plt.xticks(rotation=30)
plt.grid()


# In[ ]:




