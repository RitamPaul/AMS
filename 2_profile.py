import streamlit as st
from PIL import Image

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

ind = st.session_state['ind']

profilepic = Image.open('./resources/images/rp_circularlogo.jpg')
with st.columns([0.4,0.2,0.4], gap='small', vertical_alignment='center')[1]:
    st.image(image=profilepic)

st.text('\n')

# displaying name
col11, col12 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col11:
    st.write('**Name**')
with col12:
    st.text_input(
        label='name',
        value='your name',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying employee id
col21, col22 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col21:
    st.write('**Employee id**')
with col22:
    st.text_input(
        label='empid',
        value='your employee id',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying role
col31, col32 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col31:
    st.write('**Role**')
with col32:
    st.text_input(
        label='role',
        value='your registered role',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying username
col41, col42 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col41:
    st.write('**Username**')
with col42:
    st.text_input(
        label='uid',
        value='your username',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying password
col51, col52, col53 = st.columns([0.4,0.52,0.08], gap='small', vertical_alignment='center')
with col51:
    st.write('**Password**')
with col52:
    st.text_input(
        label='pwd',
        value='your password' if ('showpwd' in st.session_state) else ('*'*15),
        disabled=True,
        label_visibility='collapsed'
    )
with col53:
    if st.button(
        label=':material/visibility:' if ('showpwd' not in st.session_state) else (':material/visibility_off:'),
        type='primary',
        use_container_width=True
    ):
        if 'showpwd' not in st.session_state:
            st.session_state['showpwd'] = True
        else:
            del st.session_state['showpwd']
        st.rerun()

# displaying emailid
col61, col62 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col61:
    st.write('**Email id**')
with col62:
    st.text_input(
        label='email',
        value='your email',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying mobile
col71, col72 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col71:
    st.write('**Mobile**')
with col72:
    st.text_input(
        label='mobile',
        value='your mobile',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying designation
col81, col82 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col81:
    st.write('**Designation**')
with col82:
    st.text_input(
        label='desg',
        value='your designation',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying department
col91, col92 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col91:
    st.write('**Department**')
with col92:
    st.text_input(
        label='dept',
        value='your department',
        disabled=True,
        label_visibility='collapsed'
    )

# displaying address
col101, col102 = st.columns([0.4,0.6], gap='small', vertical_alignment='center')
with col101:
    st.write('**Home address**')
with col102:
    st.text_input(
        label='home address',
        value='your home address',
        disabled=True,
        label_visibility='collapsed'
    )