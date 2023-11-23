import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Tristan Day")
    content = """
    Hi, My name is Tristan! I am a Nuclear Medicine Technologist that also does programming. I graduated from the University of Missouri - Columbia in 2021 with a Bachelors Science in Clinical and Diagnostic Sciences
    and a minor in Computer Science. I am currently working for Saint Luke's Health System but I also did a Software Engineering Internship with Cerner (now Oracle Health).
    """
    st.info(content)
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)