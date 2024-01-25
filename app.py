from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Just A Normal Site", page_icon=":star:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Header Section -----
st.subheader("Hi, This is my First ever Website :wave:")
st.title("I am just someone trying to program")
st.write("This Website is a Tryout")

# ---- Load Assets ---
lottie_coding = load_lottieur1("https://lottie.host/cb6ce3c9-123a-46bb-9468-bae5ddc6b366/MxKkdyBsy4.json")
img_contact_form = Image.open("images/image_coding.jpg")

# ---- What I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("I Am Learning How to Program, Make Apps and Sites, and much more. Coding is hard to learn, but it is very useful these days, since technology is in every house.")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# ----- Projects ------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("I don't have any particullar Projects")
        st.write("But i am trying to learn coding as soon as possible to know how to make good sites/apps.")

