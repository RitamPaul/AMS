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
btnA, btnU, btnNU, submit = False, False, False, False
col1, col2, col3 = st.columns(3, vertical_alignment="center")
with col1:
    container1 = st.container(border=False)
    btnA = container1.button("Log in as ADMIN", type='primary', use_container_width=True)
with col2:
    container2 = st.container(border=False)
    btnU = container2.button("Log in as USER", type='primary', use_container_width=True)
with col3:
    container3 = st.container(border=False)
    btnNU = container3.button("Create account", type='primary', use_container_width=True)

if(btnA or btnU):
    uid = st.text_input(
        label="**Admin ID**"*btnA or "**User ID**"*btnU,
        placeholder="admin id"*btnA or "user id"*btnU,
        key="uidold"
    )
    pwd = st.text_input(label="**Password**", placeholder="password", key="pwdold", type="password")
    with st.columns([0.25,0.5,0.25])[1]:
        submit = st.button("submit", type='primary', use_container_width=True)

elif(btnNU):
    name = st.text_input(label="**Full name**", placeholder="full name", key="namenew")
    eid = st.text_input(label="**Unique employee ID**", placeholder="unique employee id", key="eidnew")
    uid = st.text_input(label="**Create your login ID**", placeholder="id", key="uidnew")
    pwd = st.text_input(label="**Create your Password**", placeholder="password", type="password", key="pwdnew")
    with st.columns([0.25,0.5,0.25])[1]:
        submit = st.button("Register", type='primary', use_container_width=True)


# # Path for any image to display
# # absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(FILE_DIR, "resources")

# logo_path = os.path.join(dir_of_interest, "images", "rp logo.jpg")