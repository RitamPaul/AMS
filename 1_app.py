import streamlit as st
import os

# page setup
st.set_page_config(
    page_title="Welcome",
    page_icon="👑",
    layout="centered",
    # initial_sidebar_state="collapsed",
)

if 'role' not in st.session_state:
    st.session_state['role'] = None

role = st.session_state['role']

def login():
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
    st.logo("resources/images/rp logo.jpg", icon_image="resources/images/rp logo.jpg")
    # # Login as Admin / User / New User
    # uid, pwd = "", ""
    # btnA, btnU, btnNU, submit = False, False, False, False
    # col1, col2, col3 = st.columns(3, vertical_alignment="center")
    # with col1:
    #     container1 = st.container(border=False)
    #     btnA = container1.button("Log in as ADMIN", type='primary', use_container_width=True)
    # with col2:
    #     container2 = st.container(border=False)
    #     btnU = container2.button("Log in as USER", type='primary', use_container_width=True)
    # with col3:
    #     container3 = st.container(border=False)
    #     btnNU = container3.button("Create account", type='primary', use_container_width=True)

    # if(btnA or btnU):
    #     uid = st.text_input(
    #         label="**Admin ID**"*btnA or "**User ID**"*btnU,
    #         placeholder="admin id"*btnA or "user id"*btnU,
    #         key="uidold"
    #     )
    #     pwd = st.text_input(label="**Password**", placeholder="password", key="pwdold", type="password")
    #     with st.columns([0.25,0.5,0.25])[1]:
    #         submit = st.button("submit", type='primary', use_container_width=True)

    # elif(btnNU):
    #     name = st.text_input(label="**Full name**", placeholder="full name", key="namenew")
    #     eid = st.text_input(label="**Unique employee ID**", placeholder="unique employee id", key="eidnew")
    #     uid = st.text_input(label="**Create your login ID**", placeholder="id", key="uidnew")
    #     pwd = st.text_input(label="**Create your Password**", placeholder="password", type="password", key="pwdnew")
    #     with st.columns([0.25,0.5,0.25])[1]:
    #         submit = st.button("Register", type='primary', use_container_width=True)
    
    # if(btnA):
    #     st.session_state['role'] = "admin"
    # elif(btnU):
    #     st.session_state['role'] = "user"
    # st.rerun()

    role = st.selectbox("**Choose your role 👇🏻**", options=['none', 'admin', 'user'])

    if st.button("Log in"):
        st.session_state['role'] = role
        st.rerun()

def logout():
    st.session_state['role'] = None
    st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
profile_page = st.Page("2_profile.py", title="Profile", icon=":material/person:", default = role in ['user','admin'])
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
else:
    pg = st.navigation([login_page])
pg.run()

# # Path for any image to display
# # absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(FILE_DIR, "resources")

# logo_path = os.path.join(dir_of_interest, "images", "rp logo.jpg")