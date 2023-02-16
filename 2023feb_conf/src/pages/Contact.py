import streamlit as st

st.subheader("Contact")
with st.form(
    key="columns_in_form2", clear_on_submit=True
):  # set clear_on_submit=True so that the form will be reset/cleared once it's submitted
    # st.write('Please help us improve!')
    Name = st.text_input(label="Please Enter Your Name")  # Collect user feedback
    Email = st.text_input(label="Please Enter Email")  # Collect user feedback
    Message = st.text_input(label="Please Enter Your Message")  # Collect user feedback
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(
            "Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!"
        )

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
