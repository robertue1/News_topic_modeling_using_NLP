import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd

from multiapp import MultiApp
from apps import main



app = MultiApp()



# Add all your application here
app.add_app("Main", main.app)
