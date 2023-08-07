import streamlit as st

st.header('This is a header')
st.subheader('This is a subheader')
st.write('This is some text')

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: red;
        color: white;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


 
