import streamlit
import requests

streamlit.set_page_config(page_title="Lies page", layout="wide")
streamlit.title("Lies form")

with streamlit.form(key = "my-form"):
    col1, col2 = streamlit.columns(2)
    with col1:
        streamlit.subheader("Politician")
        politician_name = streamlit.text_input("Name", placeholder="Lézer Jonatán")
        age = streamlit.number_input("Age", step=1, min_value=18)
    with col2:
        streamlit.subheader("Party")
        party_name = streamlit.selectbox("Party", ["Fidesz", "Tisza", "DK", "Mi Hazánk", "MSZP"])
        color = streamlit.color_picker("Color", value="#FF6A00")
    
    col3, col4 = streamlit.columns(2)
    with col3:
        streamlit.subheader("Lie")
        lie_date = streamlit.date_input("Date", "today")
        lie = streamlit.text_area("Lie")
    with col4:
        streamlit.subheader("Review")
        consent = streamlit.checkbox("Yes, I really want to store these data!")

    submit = streamlit.form_submit_button("Submit")
    if submit:
        if consent and len(politician_name) >= 1:
            form_data_dict = {"politician_name": politician_name, "age": age, "party_name": party_name, "color": color, "lie_date": lie_date, "lie": lie}
            print(f"form_data_dict: {form_data_dict}")

            res = requests.post(url="https://python-forms.vercel.app/api/lies", data=form_data_dict)
            print(f"res.ok: {res.ok}")
            print(f"res.status_code: {res.status_code}")
            print(f"res.text: {res.text}")

            streamlit.success("OK")
        else:
            streamlit.error("Fill fields")
    else:
        streamlit.error("Fill fields")