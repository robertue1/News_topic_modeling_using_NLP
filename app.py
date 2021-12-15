import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd



from multipage import save, MultiPage, start_app, clear_cache

start_app() #Clears the cache when the app is started

app = MultiPage()
app.start_button = "Let's go!"
# app.navbar_name = "Navigation"
# app.next_page_button = "Next Page"
# app.previous_page_button = "Previous Page"


def startpage():
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

    link = "[Let's begin the journey](http://github.com)"
    st.markdown(link, unsafe_allow_html=True)


