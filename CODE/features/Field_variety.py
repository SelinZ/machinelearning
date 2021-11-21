#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import pandas as pd


# In[5]:


#import json

#with open(r"C:\Users\SelinZ\OneDrive\Desktop\ML\train-1.json") as f:
#    traind = json.load(f)

#df = pd.DataFrame.from_dict(traind)


# In[7]:


#fields = df['fields_of_study'] 
#print(fields.isnull().sum())
#fields_filled = fields.fillna('A')
#print(fields_filled.isnull().sum())


# In[11]:


#The number of different fields that a certain article is about > 1 or 2 or 3 

def field_variety(df):
    """
    Computes the number of different fields that each paper is about by taking the number of fields in 'fields_of_study'
    Input:
        - df['fields_of_study']:    dataframe (dataset); 'fields_of_study' column                   [pandas dataframe]
    Output:
        - Field variety:           vector of field_variety for each paper of the given dataset      [pandas series]
                                    with field_variety                                                   [int]
    """
    import pandas as pd

   # Field_variety = pd.Series([len(i) for i in fields_filled])            # Variety of fields
    Field_variety = pd.Series([len(i) for i in df['fields_of_study']])      # Variety of fields

    return(Field_variety)                                                  #Output


# In[10]:


#field_variety(df).value_counts()
#1    9224
#2     423
#3      11
#dtype: int64

