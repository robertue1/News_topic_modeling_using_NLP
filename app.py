import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd





st.write('''
# Understanding the Venezuelan Crisis
## Analysis of 20 years of news articles. 
''')

st.markdown(
    """
 <style>
.stApp {
  background-image: url("https://images.unsplash.com/photo-1621622633934-b910be06148d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3538&q=80,%s");
  background-size: cover;
}
</style>
    """,
    unsafe_allow_html=True
)

st.write(''' 
       #### Choose one of the following times frames to see the main topics in the news
''')



period  = st.selectbox(
     'Choose one of the following time frames',
     ('1999-2004', '2004-2009', '2009-2013', '2013-2017'))

st.write('You selected:', period)



