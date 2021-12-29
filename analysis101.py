import pandas as pd
import numpy as np 
import streamlit as st
data = pd.read_csv('data/PakistanLargestEcommerceDataset.csv')
st.write("### PakistanLargestEcommerceDataset", data.head(5))
