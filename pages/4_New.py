import json
import time
import requests
import streamlit as st
import pandas as pd


st.header("Show Data Index Price")
df=pd.read_csv("C:\Users\wiriy\OneDrive\เดสก์ท็อป\เรียน Online\โฟลเดอร์ใหม่\project01\data\stock_index_price.csv")
st.write(df.head(10))


