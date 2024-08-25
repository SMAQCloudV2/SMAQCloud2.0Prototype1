import streamlit as st
import requests as requests
import json
from streamlit_lottie import st_lottie
from PIL import Image

fish_lottie_url = "../Lottie Animations/fish_lottie.json"

with open(fish_lottie_url, "r",errors='ignore') as fish:
    fish_lottie = json.load(fish)

with st.container():
  column1, column2 = st.columns(2)

  with column1:
    st_lottie(fish_lottie,
          height = 300,
          )

  with column2:
   st.title("What is SMART AQUAPONICS?")
   st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna 
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
    ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    uis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur 
    sint occaecat cupidatat non proident, sunt in culpa qui
    officia deserunt mollit anim id est laborum.aaa
    """       
    )
