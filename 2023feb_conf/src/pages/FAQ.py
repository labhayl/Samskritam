import streamlit as st

st.header("Frequently Asked Questions")
st.write(
    """
1. What is कैलासः / kailāsaḥ ? \n
Ans-San: कैलासः तन्त्रांशसाधन शब्दं विभज्य सन्धिनाम लिखति। \n
Ans-Eng: Kailāsaḥ is a website that separates a word into its constituent parts and determines the sandhi type based on the combination of vowels in the split words. It provides the sandhi name and the separated words.

2. What is the current accuracy of kailāsaḥ ? 

Ans: ~70%

3. What kinds of Sandhi does kailāsaḥ support ? 

Ans: Currently kailāsaḥ supports svara sandhi. Works related to vyanjana sandhi & anunasika sandhi is in progress.

4. What's the time consumed to perform vibhajana(विभजन) by kailāsaḥ ? 

Ans: The entire pipeline consumes around 7.28 seconds to perform the vibhajana and return the words with the sandhi.\n
The model takes 2.33 seconds to perform the split.

(Can take multiple words as input at a time)
(excluding sandhi recognition) 
"""
)

st.subheader(" In work is supported by Department of Science and Technology, (DST), Government of India under the project grant DST/TDT/SHRi-14/2021(C). ")



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
