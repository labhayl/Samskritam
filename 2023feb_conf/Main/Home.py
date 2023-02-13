import streamlit as st
import os 
import scripts.dev2iast as d2i
import scripts.iast2dev as i2d
import scripts.sandhi.vowel_convert as conv


def sandhi_split(iast_text):
    with open("iast.txt", "w", encoding="utf-8") as f:
        f.write(iast_text)
    os.system(f"python scripts/model/code/apply.py iast.txt sandhi.txt")
    with open("sandhi.txt", "r" , encoding='utf-8') as f:
        output = f.read()
    return output

def vowel_recognize(words):
    #first_word = words[0]
    #last_word = words[1]
    st.text(words[0],words[1])
    return 0



title_page = """
            <h1 style='text-align: center;'>कैलासः / kailāsaḥ </h1>
            """
st.markdown(title_page, unsafe_allow_html=True) 



st.subheader("संस्कृतम् व्याकरणम्")
st.subheader("saṃskṛtam vyākaraṇam ")
input_text = st.text_input("Enter input text / कृपया शब्दान् लिखन्तु : ")
if input_text:
    iast_1 = d2i.iast(input_text)
    st.success("Output:")
    st.text(iast_1)
    split_text = sandhi_split(iast_1)
    st.text(split_text)
    split_text = split_text.replace('-', ' ')
    st.text(split_text)
    dev_1 = i2d.devn(str(split_text)).replace("\n", "").split(" ")
    st.text(dev_1)
    vowel_recognize(dev_1)
    
    



st.caption(" In work is supported by Department of Science and Technology, (DST), Government of India under the project grant DST/TDT/SHRi-14/2021(C). ")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 