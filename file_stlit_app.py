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
  col1,col2=st.columns([5,5])
  with col1:
      uploaded_file = st.file_uploader("Choose a file:")
  type_of_file=uploaded_file.name.split['.'][-1]
  if uploaded_file is not None and type_of_file='csv':
        # displaying the contents of the CSV file
        dataframe = pd.read_csv(uploaded_file,nrows=10)
        #data=uploaded_file.read()
        #st.write(data)
        st.dataframe(dataframe)
  with col2:
    btn1=st.button("Encrypt and Upload File",key="Key1")
    st.write("")
    btn2=st.button("Upload File",key="Key2")
