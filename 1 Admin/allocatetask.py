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
    ALLOCATE TASK
    </p>'''
)

ind = st.session_state['ind']

# task image uploader
st.file_uploader(
    label='**Task image** (if any)',
    key=f'ADMINtaskimage-{ind}',
    accept_multiple_files=True,
)

imagecount = 0
if(st.session_state[f'ADMINtaskimage-{ind}'] != None):
    imagecount = len(st.session_state[f'ADMINtaskimage-{ind}'])

# popover to display task images
# since it's a container, no need of key
with st.popover(
    label='**Open this to see task images**' if imagecount>0 else '**No image uploaded**',
    disabled=imagecount==0,
    use_container_width=True
):
    if st.selectbox(
        label='**Choose the uploaded picture to display**',
        key=f'ADMINtaskimageview-{ind}',
        options=[f"image-{i+1}" for i in range(imagecount)],
        index=None,
        placeholder='choose image number',
        disabled=imagecount == 0
    ):
        imagenum = st.session_state[f'ADMINtaskimageview-{ind}'].split('-')[1]
        st.image(st.session_state[f'ADMINtaskimage-{ind}'][int(imagenum) - 1])

# task details
st.text_input(
    label='**Task details**',
    key=f'ADMINtaskdetails-{ind}',
    placeholder='details of the task'
)

# task location
st.text_input(
    label='**Location**',
    key=f'ADMINtasklocation-{ind}',
    placeholder='building no. / floor no. / room no.'
)

# specific employee to allocate task
st.multiselect(
    label='**Specific employee to alocate task** (if any)',
    key=f'ADMINallocatetask-{ind}',
    options=[""],
    placeholder='employee names will go here'
)

# task % completion
st.slider(
    label='**Completion percentage (%)**',
    key=f'ADMINtaskcomplete-{ind}',
    value=0,
    min_value=0,
    max_value=100,
    step=1
)

# submit 
with st.columns([0.25,0.5,0.25])[1]:
    if st.button(label="submit", type='primary', use_container_width=True):
        list_attrib = [
            f'ADMINtaskimage-{ind}',        f'ADMINtaskimageview-{ind}',
            f'ADMINtaskdetails-{ind}',      f'ADMINtasklocation-{ind}',
            f'ADMINallocatetask-{ind}',     f'ADMINtaskcomplete-{ind}'
        ]
        # only erase now, later send to database
        for attrib in list_attrib:
            del st.session_state[attrib]
        st.session_state['ind'] = not st.session_state['ind']
        st.rerun()
