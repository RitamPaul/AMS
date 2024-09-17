import streamlit as st

ind = st.session_state['ind']

if 'notconfirmed' in st.session_state:
    st.error('ERROR : Typing mistake during confirmation',  icon='🔴')
    del st.session_state['notconfirmed']

login_page = st.Page("app.py", title="Log in", icon=":material/login:")

st.markdown(
    '''<p style="
    color:blue;
    text-align:center;
    letter-spacing:7px;
    font-size:50px;
    font-weight:bolder;
    font-family:verdana;
    ">
    ACCOUNT DELETION
    </p>''',
    unsafe_allow_html = True
)

st.subheader("\n")
st.write("**⚠️Note : Keep in mind that your account will be permanently deleted and your data can never be retrieved**")
st.subheader("\n")

col1, col2 = st.columns([0.7,0.3], gap='small', vertical_alignment='center')

with col1:
    st.subheader("**Type 'CONTINUE' here to confirm your action 👉**")

with col2:
    st.text_input(
        label='',
        value=None,
        key=f'entry-{ind}',
        placeholder='write in block letters',
        label_visibility='collapsed'
    )

entry = st.session_state[f'entry-{ind}']
del st.session_state[f'entry-{ind}']

st.subheader("\n")
st.subheader("\n")
with st.columns([0.3,0.4,0.3], gap='small', vertical_alignment='center')[1]:
    if st.button("submit", type='primary', use_container_width=True):
        if entry!='CONTINUE':
            st.session_state['notconfirmed'] = True
            st.rerun()

        # removing from database
        mycon = st.session_state['dblink']
        cursor = mycon.cursor(buffered=True)
        username = st.session_state['username']
        query=f"select empid from employee where uid='{username}'"
        cursor.execute(query)

        data = cursor.fetchone()
        empid = data[0]
        
        query=f"delete from employee where empid='{empid}'"
        cursor.execute(query)
        mycon.commit()

        # going back to login page after clearing cache
        st.session_state['dblink'].close()
        st.session_state.clear()
        pg = st.navigation([login_page])
        pg.run()
        st.session_state.clear()
        st.rerun()