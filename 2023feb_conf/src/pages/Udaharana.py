import streamlit as st

st.header(" Udāharaṇa / Examples / उदाहरण ")

st.write('''
savarṇadīrgha sandhi -> पुस्तकालयः \n
vṛddhi sandhi -> जनैकता \n
guṇa sandhi -> गजेन्द्रः  \n


For multiple words
"python scripts\model\code\\apply.py iast_test.txt sandhi_test.txt"
''' 
)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 