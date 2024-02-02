import requests
import streamlit as st

st.set_page_config(page_title="Dirk Und Ich, Yousef El-Sayed", page_icon=":star:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Header Section -----
st.subheader("Das enthält die Inhalt und ist in drei Teile geteilt:")
st.title("Beginn")
st.write("Es gibt ein Junge der Andreas heißt. Er wohnt mit seiner normalen Familie. Andreas ist 12 Jahre alt. Er hat zwei Brüder, Dirk und Björn. Dirk ist 11 und Björn ist 2. Seine Eltern sind nicht streng, sondern nett. Andreas hat keine viele Freunde, sondern nur 3 beste Freunde: Susanne, Christiane und Richard. Richard und Andreas sind so gute Freunde, dass sie sich gegenseitig 'Blutsbruder' nennen. Alle diese Freunde hassen, wenn es zu langweilig wird. Sie wollen, dass es immer Spaß gibt.")

# ---- Load Assets ---

# ---- What I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Höhepunkt")
        st.write("##")
        st.write("Auf einem Tag war Richard in seinen Raum, und guckte durch sein Fensterrohr. Er hatte ein riesiges Fenster, wo sein Bett drunter stand. Aber Dann sah Richard etwas sehr komisches. Herr und Frau Berger haben zusammengestritten. Sie wohnten an der anderen Seite der Straße. Herr Berger hatte seine Frau eine gescheuert. Sie rannte aus dem Wohnzimmer raus, Herr Berger hat sie verfolgt und das Licht ging aus. Dann kam Herr Berger zurück, aber mit einen großen Plastiksack. Er ging durch den Garten und zog den Sack, bis zu einer Tür im Haus, die in einen Kellerraum runterführte. Da zerrte er ihn ein, und schwitzte dabei wie verrückt. Luzy, der Schäferhund von Bergers, jaulte dabei und versuchte an dem Plastik rumzukratzen. Dann kam Herr Berger mit Luzy wieder aus dem Keller. Das hat er Andreas, Dirk und Susanne erzählt. Sie haben geplant, dass sie Nachweisen finden müssen, vor sie die Polizei anrufen. Sie trugen schwarze Kleider und brachten eine kleine Taschenlampe mit. Die Kinder rannten durch die Straße bis zu das Bergers Haus. Dann waren sie um das Hausherum gegangen, bis sie den Keller gefunden haben. Die Tür war geschlossen, aber sie haben ein Fenster gefunden. Susanne ist durch das Fenster geklettert. Danach die anderen. Sie haben eine Waschmaschine gefunden, und daneben lag der Sack. Sie hatten alle Angst. Aber Richard hat die Plastiksacke gerissen. Dann hörten sie Herr Berger auf die Treppe.")
# ----- Projects ------
with st.container():
    st.write("---")
    st.header("Schluss")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.subheader("Schluss")
        st.write("Dann kam er und sagte: 'Hände hoch!'. Im Sack gab es nur Wäsche. Und Frau Berger war beurlaubt. Sie hatten Ärger mit ihren Eltern, weil sie sich in den Keller von jemandem geschlichen hatten.")
