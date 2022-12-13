#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd

# Allow user to upload a dataset
dataset = st.file_uploader("Upload a dataset in XLSX format", type="xlsx")

# Load the dataset into a DataFrame
if dataset is not None:
    data = pd.read_excel(dataset)

    # Calculate and display summary statistics and distribution graphs for each column
    st.header("Summary statistics")
    for column in data.columns:
        st.write(f"Column: {column}")
        st.write(data[column].describe())
        st.pyplot(data[column].hist())


# In[ ]:





# In[ ]:




