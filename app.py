import streamlit as st
import os

for attrib in ['role','username','password']:       # NONE type initialisation
    if attrib not in st.session_state:
        st.session_state[attrib] = None
if 'ind' not in st.session_state:                   # BOOL type initialisation
    st.session_state['ind'] = True
if 'department' not in st.session_state:            # LIST type initialisation
    st.session_state['department'] = ['Airport Operations', 'Air Traffic Control (ATC)', 'Security', 'Customs & Immigrations', 'Ground Handling Services', 'Terminal Management', 'Passenger Services', 'Engineering & Maintenance', 'Cargo Operations', 'Airlines Offices', 'Fire & Rescue Service', 'Medical Service', 'Finance & Accounts', 'Human Resources', 'Parking & Ground Transportation']
    st.session_state['department'].sort()
ind = st.session_state['ind']

# login page
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

    # greetings for successfully registered
    if('registered' in st.session_state):
        st.success("Congratulations! your account is successfully created", icon="✅")
        st.balloons()
        del st.session_state['registered']

    if 'btn' not in st.session_state:
        st.session_state['btn'] = None
    btn = st.session_state['btn']

    # Login as Admin / User / New User
    col1, col2, col3 = st.columns(3, vertical_alignment="center")
    with col1:
        if st.button("Log in as ADMIN", type='primary', use_container_width=True):
            st.session_state['btn'] = 1
            st.session_state['ind'] = not st.session_state['ind']
            st.rerun()
    with col2:
        if st.button("Log in as USER", type='primary', use_container_width=True):
            st.session_state['btn'] = 2
            st.session_state['ind'] = not st.session_state['ind']
            st.rerun()
    with col3:
        if st.button("Create account", type='primary', use_container_width=True):
            st.session_state['btn'] = 3
            st.session_state['ind'] = not st.session_state['ind']
            st.rerun()

    if((btn==1) or (btn==2)):
        st.text_input(
            label="**Admin ID**" if (btn==1) else ("**User ID**"),
            key=f'id-{ind}',
            value=None,
            placeholder='enter your username'
        )
        st.text_input(
            label="**Password**",
            type="password",
            key=f'pwd-{ind}',
            value=None,
            placeholder='enter your password'
        )
        with st.columns([0.25,0.5,0.25])[1]:
            if st.button("submit", type='primary', use_container_width=True):
                uid = st.session_state['username'] = st.session_state[f'id-{ind}']
                pwd = st.session_state['password'] = st.session_state[f'pwd-{ind}']
                del st.session_state[f'id-{ind}']
                del st.session_state[f'pwd-{ind}']
                del st.session_state['btn']
                
                # checking in database

                st.session_state['role'] = 'admin' if (btn==1) else ('user')
                st.rerun()
    
    elif(btn==3):
        st.text_input(
            label="**Full name**",
            key=f'name-{ind}',
            value=None,
            placeholder="enter your full name"
        )
        st.text_input(
            label="**Unique employee ID**",
            key=f'eid-{ind}',
            value=None,
            placeholder="enter your unique employee id"
        )
        st.radio(
            label="**Choose your role**",
            options=['Admin','User'],
            key=f'reg_role-{ind}',
            index=None,
            horizontal=True
        )
        st.text_input(
            label="**Email id**",
            key=f'email-{ind}',
            value=None,
            placeholder="enter your email id"
        )
        st.text_input(
            label="**Mobile**",
            key=f'mobile-{ind}',
            value=None,
            placeholder="enter your contact number"
        )
        st.text_input(
            label="**Address**",
            key=f'address-{ind}',
            value=None,
            placeholder="enter your location address"
        )
        st.selectbox(
            label="**Department**",
            key=f'dept-{ind}',
            options=st.session_state['department'],
            index=None,
            placeholder="enter your department"
        )
        st.text_input(
            label="**Designation**",
            key=f'desg-{ind}',
            value=None,
            placeholder="enter your designation"
        )
        st.text_input(
            label="**Create your login ID**",
            key=f'uid-{ind}',
            value=None,
            placeholder="username"
        )
        st.text_input(
            label="**Create your Password**",
            key=f'pwd-{ind}',
            value=None,
            placeholder="password",
            type="password"
        )
        with st.columns([0.25,0.5,0.25])[1]:
            if st.button("submit", type='primary', use_container_width=True):
                # insert into database
                name        = st.session_state[f'name-{ind}']
                eid         = st.session_state[f'eid-{ind}']
                reg_role    = st.session_state[f'reg_role-{ind}']
                email       = st.session_state[f'email-{ind}']
                mobile      = st.session_state[f'mobile-{ind}']
                address     = st.session_state[f'address-{ind}']
                dept        = st.session_state[f'dept-{ind}']
                desg        = st.session_state[f'desg-{ind}']
                uid         = st.session_state[f'uid-{ind}']
                pwd         = st.session_state[f'pwd-{ind}']

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
deleteaccount_page = st.Page("4_deleteaccount.py", title="Delete account", icon=":material/delete:")

allocatetask_page = st.Page("1 Admin/allocatetask.py", title="Allocate task", icon="🛠️")
assetapproval_page = st.Page("1 Admin/assetapproval.py", title="Approve asset requests", icon="🫱🏻‍🫲🏻")

assetrequest_page = st.Page("2 User/assetrequest.py", title="Asset request", icon=":material/storefront:")
onlyformetask_page = st.Page("2 User/onlyformetask.py", title="Only for me task", icon=":material/accessibility:")
raiseissue_page = st.Page("2 User/raiseissue.py", title="Raise issue", icon=":material/info:")

sidebar_list = {}
if(st.session_state['role'] == 'admin'):
    sidebar_list['Account'] = [profile_page, settings_page, deleteaccount_page, logout_page]
    sidebar_list['Admin privileges'] = [assetrequest_page, raiseissue_page]
    sidebar_list['Work'] = [allocatetask_page, assetapproval_page]
elif(st.session_state['role'] == 'user'):
    sidebar_list['Account'] = [profile_page, settings_page, deleteaccount_page, logout_page]
    sidebar_list['Work'] = [assetrequest_page, onlyformetask_page, raiseissue_page]

if(len(sidebar_list) > 0):
    pg = st.navigation(sidebar_list)
    pg.run()

# # Path for any image to display
# # absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(FILE_DIR, "resources")

# logo_path = os.path.join(dir_of_interest, "images", "rp logo.jpg")