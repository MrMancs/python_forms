import streamlit

streamlit.set_page_config(page_title="Lies page", layout="wide")
streamlit.title("Lies form")

with streamlit.form(key = "my-form"):
    col1, col2 = streamlit.columns(2)
    with col1:
        streamlit.subheader("Politician")
    with col2:
        streamlit.subheader("Party")

    submit = streamlit.form_submit_button("Submit")