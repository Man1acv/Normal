import requests
import streamlit as st

st.set_page_config(page_title="Just A Normal Site", page_icon=":star:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Header Section -----
st.subheader("Facts You Didn't know about Animals! :tiger:")
st.title("If You Know More Than 3, You love Animals!")
st.write("Created By Me")

# ---- Load Assets ---

# ---- Facts ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Crazy Facts")
        st.write("##")
        st.write("Cheetahs are the fastest runners on Earth! A Green anaconda can swallow a Full Grown Man! Butterflies taste with their.. Feet?! A Bald Eagle Nest can weigh 2 Tons! Racoons may wash food before eating!")


# ----- Ending ------
with st.container():
    st.write("---")
    st.header("Follow My Sites for More!")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.subheader("If You Liked these Facts")
        st.write("I don't know what you should do.")
