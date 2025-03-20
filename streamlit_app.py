import streamlit as st
from streamlit_free_text_select import st_free_text_select

st.write('Hello world!')

value = st_free_text_select(
    label="Query data:",
    options=["Option 1", "Option 2"],
    index=None,
    format_func=lambda x: x.lower(),
    placeholder="Select or enter a question",
    disabled=False,
    delay=300,
    label_visibility="visible",
)

st.write(value)