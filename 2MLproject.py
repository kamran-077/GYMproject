#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#1.load
df = pd.read_csv('gym_members_exercise_tracking.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


#now will perform EDA
df.info()


# In[6]:


#1Gender
#2 workout Type
df['Gender'].unique()


# In[7]:


df['Workout_Type'].unique()


# In[8]:


#2 to check null values
df.isnull().sum()


# In[9]:


#checking target columns (calories_burned) for skewness
sns.histplot(df['Calories_Burned'],kde=True)


# In[10]:


df['Calories_Burned'].skew()


# In[11]:


#coorelation and heatmap btw numerical feature
corr = df.corr(numeric_only=True)


# In[12]:


plt.figure(figsize=(10,10))
sns.heatmap(corr,annot=True)


# In[13]:


# Gender , workout_type encode
df['Gender'] = df['Gender'].map({'Male':0,'Female':1})
df.head()


# In[14]:


#Workout_type onehot encode
df = pd.get_dummies(df,columns=['Workout_Type'])
df.head()


# In[15]:


#split x and y variables
x = df.drop('Calories_Burned',axis=1)
y = df['Calories_Burned']


# In[16]:


#Train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[17]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)   # to prevent from data leakage


# In[18]:


#Build linear regression model
from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()
linear_model.fit(x_train,y_train)


# In[19]:


y_pred = linear_model.predict(x_test)


# In[20]:


from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score


# In[21]:


#test accuracy
print(r2_score(y_test,y_pred))


# In[22]:


# Train accuracy
r2_score(y_train,linear_model.predict(x_train))


# In[23]:


mean = mean_absolute_error(y_test,y_pred)
print(mean)


# In[24]:


import joblib
joblib.dump(linear_model,'linear_model.pkl')

