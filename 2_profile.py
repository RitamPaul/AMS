import streamlit as st
from PIL import Image
import PIL

st.markdown(
    '''<p style="
    color:blue;
    text-align:center;
    letter-spacing:10px;
    font-size:50px;
    font-weight:bolder;
    font-family:verdana;
    ">
    PROFILE
    </p>''',
    unsafe_allow_html = True
)

profilepic = Image.open('./resources/images/rp_circularlogo.jpg')
with st.columns([0.4,0.2,0.4], gap='small', vertical_alignment='center')[1]:
    st.image(image=profilepic)

