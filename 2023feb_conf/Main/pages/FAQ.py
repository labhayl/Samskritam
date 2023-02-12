import streamlit as st

st.header("Frequently Asked Questions")
st.write(
    """
1. What is कैलासः / kailāsaḥ ?
Ans-San: कैलासः तन्त्रांशसाधन शब्दं विभज्य सन्धिनाम लिखति। 
Ans-Eng: Kailāsaḥ is a website that separates a word into its constituent parts and determines the sandhi type based on the combination of vowels in the split words. It provides the sandhi name and the separated words.
"""
)

st.subheader(" In work is supported by the Department of Science and Technology(DST), Government of India under the project grant DST/TDT/SHRi-14/2021(C). ")



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
