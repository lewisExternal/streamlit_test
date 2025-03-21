import streamlit as st
import requests
from streamlit_free_text_select import st_free_text_select

def render_select_box():
    select_box = st_free_text_select(
        label="Query data:",
        options=["Option 1", "Option 2"],
        index=None,
        format_func=lambda x: x.lower(),
        placeholder="Select or enter a question",
        disabled=False,
        delay=300,
        label_visibility="visible",
    )
    st.write(select_box)

def test_networking():
    if st.button("Press me"):
        response = requests.get("https://feeds.bbci.co.uk/news/rss.xml")
        st.write(response.text)


if __name__ == '__main__':
    pass 