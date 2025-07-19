# Importations  
import streamlit as st
import cv2
import cvzone
import time
import mediapipe as mp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Haram Blur", page_icon="🙈",layout="centered")

st.title("Haram Blur ❤️")
st.sidebar.success("Try Our App !!.")


st.markdown("""
            ##### Here is My 2 Options To Try in My App :
            1. Using Image as an Input 
            2. Using Real Time Camera as an Input   
            """)