import streamlit as st
import pandas as pd

st.markdown(
    '''<p style="
    color:blue;
    text-align:center;
    letter-spacing:10px;
    font-size:50px;
    font-weight:bolder;
    font-family:verdana;
    ">
    APPROVE ASSET REQUESTS
    </p>''',
    unsafe_allow_html = True
)
st.write('\n')

# success mesg display
if 'successfulysaved' in st.session_state:
    st.success("**✅ Your edits are saved successfully**")
    del st.session_state['successfulysaved']

# inserting success mesg flag
def show_success():
    st.session_state['successfulysaved'] = True

# mySQL db data need to be fetched and converted into pandas dataframe

# Sample data for the table
data = {
    "Sl. No." : [i for i in range(1, 11)],
    "Column 1": [f"Row {i}"  for i in range(1, 11)],
    "Column 2": [f"Data {i}" for i in range(1, 11)],
    "Column 3": [f"Info {i}" for i in range(1, 11)],
    "Column 4": [f"Detail {i}" for i in range(1, 11)],
    "Column 5": [f"Value {i}" for i in range(1, 11)],
    "Approve": ["" for  i in range(1, 11)]  # This will hold the dropdown selections
}

# Create a DataFrame
df = pd.DataFrame(data)

# customize column names to center
df = df.style.set_properties(**{'text-align':'left'})

# Display the DataFrame with the dropdown in the last column
# Using the column_config to specify the dropdown for the "Status" column
edited_df = st.data_editor(
    df,
    key='table',
    column_config={
        "Approve": st.column_config.CheckboxColumn(
            label=None,
            help='double click for options'
        )
    },
    disabled=['Sl. No.', 'Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'],
    use_container_width=True,
    hide_index=True
)

# Save button
if st.button("Save", on_click=show_success):
    # Here you can implement the logic to save the data
    # For now, we will just display the saved data
    # st.success("Changes saved successfully!")
    pass