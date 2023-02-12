import streamlit as st
import subprocess
import os 
from scripts import dev2iast

def dev_to_iast(input_text):
    result = os.system("python dev2iast.py '{}'".format(input_text))
    return result.stdout.decode("utf-8")

def sandhi_split(iast_text):
    with open("iast.txt", "w", encoding="utf-8") as f:
        f.write(iast_text)
    os.system(f"python scripts/model/code/apply.py iast.txt sandhi.txt")
    with open("sandhi.txt", "r" , encoding='utf-8') as f:
        output = f.read()
    return output



title_page = """
            <h1 style='text-align: center;'>कैलासः / kailāsaḥ </h1>
            """
st.markdown(title_page, unsafe_allow_html=True) 



st.subheader("संस्कृतम् व्याकरणम्")
st.subheader("saṃskṛtam vyākaraṇam ")
input_text = st.text_input("Enter input text / कृपया शब्दान् लिखन्तु : ")
if input_text:
    iast_1 = dev2iast.iast(input_text)
    st.success("Output:")
    st.text(iast_1)
    split_text = sandhi_split(iast_1)
    st.text(split_text)
    dev_1 = iast_to_dev(split_text.replace('-', ' '))
    st.text(dev_1)

st.caption(" In work is supported by Department of Science and Technology, (DST), Government of India under the project grant DST/TDT/SHRi-14/2021(C). ")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 