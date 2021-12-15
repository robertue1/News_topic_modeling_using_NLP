import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd


#PART 1

st.write('''
# Understanding the Venezuelan Crisis
## Analysis of 20 years of news articles. 
''')

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
   .sidebar .sidebar-content {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
    </style>
    """,
    unsafe_allow_html=True
)
