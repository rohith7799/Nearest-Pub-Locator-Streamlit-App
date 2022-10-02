import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from ctypes import alignment
from turtle import color
from PIL import Image

column1, column2 = st.columns(2)
with column1:
    st.title("Welcome to Beer Garden United Kingdom")

with column2:
    img = Image.open("pubimg.jpg")
    st.image(img)

st.subheader("Money can't buy happiness but it can buy Beer. Cheers!!")

st.markdown("Check out the Top Locations with more than 400 Pubs")

col = ['fsa_id', 'pubname', 'pubaddress', 'pubpostcode', 'easting', 'northing', 'lat', 'lon', 'local_authority']

df = pd.read_csv('open_pubs.csv', names = col)
df['lat'] = df['lat'].replace('\\N', np.nan)
df['lon'] = df['lon'].replace('\\N', np.nan)
df = df.dropna()

## top 20 local_authority with high pub counts > 400
a = pd.DataFrame(df['local_authority'].value_counts())
a.reset_index(inplace = True)
column = ['local_authority', 'pub_count']
a.columns = column
pub400 = a[a['pub_count'] > 400]
plt.figure(figsize = (20,6))
st.bar_chart(data = pub400, x = 'local_authority', y = 'pub_count' )
