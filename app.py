import streamlit as st
import os

st.markdown(
    '''<p style="
    color:blue;
    text-align:center;
    letter-spacing:10px;
    font-size:60px;
    font-weight:bolder;
    font-family:verdana;
    ">
    WELCOME    
    </p>''',
    unsafe_allow_html = True
)

# Login as Admin / User / New User
uid, pwd = "", ""
btn1, btn2, btn3, submit = False, False, False, False
col1, col2, col3 = st.columns(3, vertical_alignment="center")
with col1:
    container1 = st.container(border=False)
    btn1 = container1.button("Log in as ADMIN", type='primary', use_container_width=True)
with col2:
    container2 = st.container(border=False)
    btn2 = container2.button("Log in as USER", type='primary', use_container_width=True)
with col3:
    container3 = st.container(border=False)
    btn3 = container3.button("Create account", type='primary', use_container_width=True)

while(not submit):
    if(btn1 or btn2):
        uid = st.text_input(
            label="**Admin ID**"*btn1 or "**User ID**"*btn2,
            placeholder="admin id"*btn1 or "user id"*btn2
        )
        pwd = st.text_input(label="**Password**", placeholder="password", type="password")
        with st.columns([0.25,0.5,0.25])[1]:
            submit = st.button("submit", type='primary', use_container_width=True)

    elif(btn3):
        name = st.text_input(label="**Full name**", placeholder="full name")
        eid = st.text_input(label="**Unique employee ID**", placeholder="unique employee id")
        uid = st.text_input(label="**Create your login ID**", placeholder="id")
        pwd = st.text_input(label="**Create your Password**", placeholder="password", type="password")
        with st.columns([0.25,0.5,0.25])[1]:
            submit = st.button("submit", type='primary', use_container_width=True)


# # Path for any image to display
# # absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(FILE_DIR, "resources")

# logo_path = os.path.join(dir_of_interest, "images", "rp logo.jpg")