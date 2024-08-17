import streamlit as st

st.html(
    '''<p style="
    color:blue;
    text-align:center;
    letter-spacing:10px;
    font-size:50px;
    font-weight:bolder;
    font-family:verdana;
    ">
    ALLOCATE TASKS
    </p>'''
)

st.session_state

if 'imagenum' not in st.session_state:
    st.session_state['imagenum'] = 1

st.file_uploader(
    label='**Task image** (if any)',
    key=f'taskimageadmin-{st.session_state['imagenum']}',
    accept_multiple_files=True,
)
imagecount = len(st.session_state[f'taskimageadmin-{st.session_state['imagenum']}']) if (st.session_state[f'taskimageadmin-{st.session_state['imagenum']}']!=None) else 0
with st.popover(
    label='**Open this to see task images**' if imagecount>0 else '**No image uploaded**',
    disabled=imagecount==0,
    use_container_width=True
):
    if st.selectbox(
        label='**Choose the uploaded picture to display**',
        key='taskimageviewer',
        options=[f"image-{i+1}" for i in range(imagecount)],
        placeholder='choose image number',
        disabled=imagecount == 0
    ):
        string_sb = st.session_state['taskimageviewer']
        imagenum = string_sb.split('-')[1]
        st.image(st.session_state[f'taskimageadmin-{st.session_state['imagenum']}'][int(imagenum) - 1])
topictags = st.multiselect(
    label="**Task tag**",
    options=['computer','network devices','wires/cables','bug fix'],
    key='topictagadmin',
    placeholder='choose the topic tags'
)
st.text_input(
    label='**Task details**',
    key='taskdetailsadmin',
    placeholder='details of the task'
)
st.text_input(
    label='**Location**',
    key='issuelocationadmin',
    placeholder='building no. / floor no. / room no.'
)
st.multiselect(
    label='**Specific employee to alocate task** (if any)',
    key='specificemployee',
    options=[""],
    placeholder='employee names will go here'
)
st.slider(
    label='**Completion percentage (%)**',
    key='taskcomplete',
    value=0,
    min_value=0,
    max_value=100,
    step=1
)

with st.columns([0.25,0.5,0.25])[1]:
    if st.button(
        label="submit",
        type='primary',
        use_container_width=True
    ):
        # list_attrib = ['taskimageadmin','taskimageviewer','topictagadmin','taskdetailsadmin','issuelocationadmin','specificemployee','taskcomplete']
        # # only erase now
        # for attrib in list_attrib:
        #     st.session_state.attrib = None
        # st.session_state.taskimageadmin = None
        st.session_state['imagenum'] += 1
        st.rerun()
