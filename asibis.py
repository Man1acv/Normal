import requests
import streamlit as st

st.set_page_config(page_title="Asibi's", page_icon=":star:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Header Section -----
st.subheader("Here You Can Buy The Battle Pass, and stuff from the Item Shop from me for extremely cheap!")
st.title("Asibi's Fortnite Shop")
st.write("This is The Official Site")

# ---- Load Assets ---

# ---- What I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Pricing")
        st.write("##")
        st.write("Battle Pass: 380 EGP │ 200 Vbuck Item: 100 EGP │ 300 Vbuck Item: 110 EGP │ 500 Vbucks Cosmetic: 160 EGP │ 800 Vbucks Cosmetic: 320 EGP │ 1000 Vbucks Cosmetic: 400 EGP │ 1200 Vbucks Cosmetic: 480 EGP │ 1400 Vbucks Cosmetic: 540 EGP │ 1500 Vbucks Cosmetic: 580 EGP │ 1700 Vbucks Bundle: 640 EGP │ 1800 Vbucks Cosmetic: 680 EGP │ 2000 Vbucks Cosmetic/Bundle 750 EGP │ 2100 Bundle: 790 EGP │ 2200 Vbucks Bundle: 830 EGP │ 2300 Vbucks Bundle: 870 EGP │ 2400 Vbucks Bundle: 910 EGP │ 2500 Vbucks Bundle: 950 EGP │ 4000-4600 Vbucks Bundle: 1500 EGP (Very Cheap!)")


# ----- Projects ------
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.subheader("This Number is the Number used to Contact me, we shall discuss what you need and everything there.")
        st.write("Phone Number (Whatsapp): +20 1029845823")
