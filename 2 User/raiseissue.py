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
    RAISE ISSUE
    </p>'''
)

ind = st.session_state['ind']

# issue image uploader
st.file_uploader(
    label='**Issue image(s)** (if any)',
    key=f'issueimages-{ind}',
    accept_multiple_files=True,
)

imagecount = 0
if(st.session_state[f'issueimages-{ind}'] != None):
    imagecount = len(st.session_state[f'issueimages-{ind}'])

# popover to display task images
# since it's a container, no need of key
with st.popover(
    label='**Open this to see issue image(s)**' if imagecount>0 else '**No image(s) uploaded**',
    disabled=imagecount==0,
    use_container_width=True
):
    if st.selectbox(
        label='**Choose the uploaded picture to display**',
        key=f'issueimageview-{ind}',
        options=[f"image-{i+1}" for i in range(imagecount)],
        index=None,
        placeholder='choose image number',
        disabled=imagecount == 0
    ):
        imagenum = st.session_state[f'issueimageview-{ind}'].split('-')[1]
        st.image(st.session_state[f'issueimages-{ind}'][int(imagenum) - 1])

# issue details
st.text_input(
    label='**Issue details**',
    key=f'issuedetails-{ind}',
    placeholder='details of the issue'
)

# issue location
st.text_input(
    label='**Location**',
    key=f'issuelocation-{ind}',
    placeholder='building no. / floor no. / room no.'
)

# # specific employee to allocate task
# st.multiselect(
#     label='**Specific employee to alocate task** (if any)',
#     key=f'ADMINallocatetask-{ind}',
#     options=[""],
#     placeholder='employee names will go here'
# )

# issue % completion
st.slider(
    label='**Completion percentage (%)**',
    key=f'issuecomplete-{ind}',
    value=0,
    min_value=0,
    max_value=100,
    step=1
)

# submit 
with st.columns([0.25,0.5,0.25])[1]:
    if st.button(label="submit", type='primary', use_container_width=True):
        list_attrib = [
            f'issueimages-{ind}',           f'issueimageview-{ind}',
            f'issuedetails-{ind}',          f'issuelocation-{ind}',
            f'issuecomplete-{ind}'
        ]
        # only erase now, later send to database
        for attrib in list_attrib:
            del st.session_state[attrib]
        st.session_state['ind'] = not st.session_state['ind']
        st.rerun()
