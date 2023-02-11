import streamlit as st
import subprocess
import os 

from scripts import dev2iast

def dev_to_iast(input_text):
    result = os.system("python dev2iast.py '{}'".format(input_text))
    return result.stdout.decode("utf-8")

title_page = """
            <h1 style='text-align: center;'>कैलासः / kailāsaḥ </h1>
            """
st.markdown(title_page, unsafe_allow_html=True) 



st.subheader("संस्कृतम् व्याकरणम्")
st.subheader("saṃskṛtam vyākaraṇam ")
input_text = st.text_input("Enter input text / कृपया शब्दान् लिखन्तु : ")
if input_text:
    output = dev2iast.iast(input_text)
    st.success("Output:")
    st.text(output)

st.caption(" In work is supported by Department of Science and Technology, (DST), Government of India under the project grant DST/TDT/SHRi-14/2021(C). ")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 