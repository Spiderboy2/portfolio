import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Chimman Soni")
    content = """   Hi, I am Chimman Soni!. and i am a learning python online from udemy.
    My teacher name is Mr Ardit suchal. I am always so excited to learn something new.
    Which is one of my hobby too."""
    st.info(content)

st.write("Below you can find some of the apps i have built in python. feel free to contact me!")