import streamlit as st
import os

if 'role' not in st.session_state:
    st.session_state['role'] = None

if(st.session_state['role'] == None):
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

    if('registered' in st.session_state):
        st.success("Congratulations! your account is successfully created", icon="✅")

    if 'btn' not in st.session_state:
        st.session_state['btn'] = None
    btn = st.session_state['btn']

    # Login as Admin / User / New User
    col1, col2, col3 = st.columns(3, vertical_alignment="center")
    with col1:
        if st.button("Log in as ADMIN", type='primary', use_container_width=True):
            st.session_state['btn'] = 1
            st.rerun()
    with col2:
        if st.button("Log in as USER", type='primary', use_container_width=True):
            st.session_state['btn'] = 2
            st.rerun()
    with col3:
        if st.button("Create account", type='primary', use_container_width=True):
            st.session_state['btn'] = 3
            st.rerun()

    if((btn==1) or (btn==2)):
        st.text_input(
            label="**Admin ID**" if (btn==1) else ("**User ID**"),
            key='id',
            value=None if (('id' not in st.session_state) or (st.session_state['id']==None)) else (st.session_state['id']),
            placeholder='enter your id' if (('id' not in st.session_state) or (st.session_state['id']==None)) else (None)
        )
        st.text_input(
            label="**Password**",
            type="password",
            key='pwd',
            value=None if (('pwd' not in st.session_state) or (st.session_state['pwd']==None)) else (st.session_state['pwd']),
            placeholder='enter your password' if (('pwd' not in st.session_state) or (st.session_state['pwd']==None)) else (None)
        )
        with st.columns([0.25,0.5,0.25])[1]:
            if st.button("submit", type='primary', use_container_width=True):
                st.session_state['role'] = 'admin' if (btn==1) else ('user')
                st.rerun()
    elif(btn==3):
        st.text_input(label="**Full name**", key='name', placeholder="enter your full name")
        st.text_input(label="**Unique employee ID**", key='eid', placeholder="enter your unique employee id")
        st.selectbox(label="**Choose your role**", options=['Admin','User'], key='reg_role', index=None, placeholder='choose an option')
        st.text_input(label="**Create your login ID**", key='uid', placeholder="id")
        st.text_input(label="**Create your Password**", key='pwd', placeholder="password", type="password")
        with st.columns([0.25,0.5,0.25])[1]:
            if st.button("submit", type='primary', use_container_width=True):
                st.session_state.clear()
                st.session_state['registered'] = True
                st.rerun()

def logout():
    st.session_state.clear()
    pg = st.navigation([login_page])
    pg.run()
    st.rerun()

login_page = st.Page("app.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
profile_page = st.Page("2_profile.py", title="Profile", icon=":material/person:", default = st.session_state['role'] in ['user','admin'])
settings_page = st.Page("3_settings.py", title="Settings", icon=":material/settings:")
allocatetask_page = st.Page("1 Admin/allocatetask.py", title="Allocate task", icon="🛠️")
viewtasks_page = st.Page("1 Admin/viewtasks.py", title="View task activity", icon="📈")
commontask_page = st.Page("2 User/commontask.py", title="Common task", icon=":material/groups:")
onlyformetask_page = st.Page("2 User/onlyformetask.py", title="Only for me task", icon=":material/accessibility:")
raiseissue_page = st.Page("2 User/raiseissue.py", title="Raise issue", icon=":material/info:")

sidebar_list = {}
if(st.session_state['role'] == 'admin'):
    sidebar_list['Account'] = [profile_page, settings_page, logout_page]
    sidebar_list['Work'] = [allocatetask_page, viewtasks_page]
if(st.session_state['role'] == 'user'):
    sidebar_list['Account'] = [profile_page, settings_page, logout_page]
    sidebar_list['Work'] = [commontask_page, onlyformetask_page, raiseissue_page]

if(len(sidebar_list) > 0):
    pg = st.navigation(sidebar_list)
    pg.run()

# # Path for any image to display
# # absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(FILE_DIR, "resources")

# logo_path = os.path.join(dir_of_interest, "images", "rp logo.jpg")