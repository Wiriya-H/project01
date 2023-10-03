import json
import time
import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

st.header("Show Data Index Price")
df=pd.read_csv(".\data\stock_index_price-2.csv")


