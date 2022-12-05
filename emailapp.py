import requests 
import streamlit as st
from streamlit_lottie import st_lottie
import openai
from ml_backend import ml_backend

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#load lottie

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m0D4rj.json")

with st.container() :
    st.title("Outil de génération de Lettres par IA :pencil:")
    st.text("by MaLettre.ai - Simo B")

st.markdown(""" 

# À propos

""")

st.write("""Jouez avec les curseurs et vos indications pour générer en quelques secondes vos propres lettres ! 
À la fin, vous pouvez envoyer automatiquement votre lettre à un destinataire via Gmail""")

with st.container() :
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: 
        st.subheader("""
Bénéfices commerciaux ou personnels et cas d'utilisation:""")

        st.write("""
- Temps économisé pour écrire des lettres de taille moyenne à longue
- Allegement de la charge mentale
- L'anxiété d'écrire une lettre dans n'importe quel style d'écriture est soulevée grâce au modèle de langage d'intélligence artificielle (GPT3) utilisé.
""")

    with right_column:
        st_lottie(lottie_coding, height=350, key="coding")

with st.container() :
    st.write("---")
    st.markdown("# Générer une lettre")

backend = ml_backend()

with st.form(key="form"):
    prompt = st.text_input("Donnez le plus d'indications possibles concernant la lettre souhaitée")
    st.text(f"(Example: Rédige moi une lettre sur un ton amicale pour remercier mon voisin de son aide)")

    slider = st.slider("Faites varier le nombre de caractères de votre lettre", min_value=2000, max_value=10000)


    submit_button = st.form_submit_button(label='Générer la lettre')

    if submit_button:
        with st.spinner("Génération en cours..."):
            output = backend.generate_email(prompt)
        st.markdown("# Votre lettre:")
        st.subheader(output)

        st.markdown("____")
        st.markdown("# Envoyer par email ?")
        st.subheader("Vous pouvez appuyer à nouveau sur le bouton Générer une lettre si vous n'êtes pas satisfait du résultat du modèle.")
        
        st.subheader("Sinon:")
        st.text(output)
        url = "https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + backend.replace_spaces_with_pluses(output)

        st.markdown("[Cliquez-ici pour l'envoyer]({})".format(url))
