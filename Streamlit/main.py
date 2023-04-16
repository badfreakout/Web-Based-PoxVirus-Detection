import os
import streamlit as st
import numpy as np
from PIL import  Image
# Custom imports 
from app import MultiPage

from pages import monkeypox

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("PoxVirus Detection with Order of Probabilities")
#display = Image.open('cover.webp')
#display = np.array(display)
#st.image(display)

st.text("PoxVirus : Chickenpox, Measles, Monkeypox, Healthy")

# Add all your application here
app.add_page("Monkeypox Or Not", monkeypox.app)

# The main app
app.run()   
