import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd


page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


#PART 1

st.write('''
# Welcome To Streamlit!
In this streamlit app we will cover:

- Markdown
- Importing Data
- Displaying DataFrames
- Graphing
- Interactivity with Buttons
- Mapping
- Making Predictions with User Input
''')
