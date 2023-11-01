import streamlit as st
import pandas as pd
import math
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
from snowflake.snowpark import Session
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from snowflake.snowpark.functions import avg, sum, col, lit
import streamlit as st
import pandas as pd
from io import StringIO
import csv
#session=Session.builder.configs(connection_parameters).create()
selected_opt  = option_menu(None, ["Sender","Receiver"],  
default_index=0, orientation="horizontal",icons=None,
                menu_icon=None,
                styles={              
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                # "icon": {"color": "orange", "font-size": "25px"},
                "icon":{"display":"none"},
                "nav": {"background-color":"#f2f5f9"},
                "nav-link": {"font-size": "10px",
                "font-weight":"bold",
                "color":"#1d1160",
                "border-right":"2px solid #4B0082",
                "border-left":"1.5px solid #4B0082",
                "border-top":"1.5px solid #4B0082",
                "border-bottom":"1.5px solid #4B0082",
                "padding":"10px",
                "text-transform": "uppercase",
                "border-radius":"1px",
                "margin":"1px",
                "--hover-color": "#e1e1e1"},
                "nav-link-selected": {"background-color":"#1d1160", "color":"#ffffff"},
                })
if selected_opt=='Sender':
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # displaying the contents of the CSV file
        #dataframe = pd.read_csv(uploaded_file,encoding='unicode_escape')
        st.write("Sucessfully Loaded File")
