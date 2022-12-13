#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

# Allow user to upload a dataset
dataset = st.file_uploader("Upload a dataset in CSV format", type="csv")

# Load the dataset into a DataFrame
if dataset is not None:
    data = pd.read_csv(dataset)

    # Calculate and display summary statistics for the dataset
    st.header("Summary statistics")
    st.dataframe(data.describe())


# In[ ]:





# In[ ]:




