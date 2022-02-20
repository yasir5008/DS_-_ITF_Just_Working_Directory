from numpy.random import sample
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from PIL import Image

st.title("This is a title")
st.text('This is some text.')
st.markdown('Streamlit is **_really_ cool**.:+1:')
st.markdown("# This is a markdown" )
st.markdown("## This is a markdown")
st.header("This is a header")
st.subheader("This is a subheader")

st.success("This is a success message")
st.info("This is a purely informational message")
st.error("This is an error")
st.help(range)
st.write("Hello, *World!* :sunglasses:")
img = Image.open("image.jpeg")
st.image(img,caption="cattie",width=300)
st.image(img,caption="cattie",use_column_width=True)