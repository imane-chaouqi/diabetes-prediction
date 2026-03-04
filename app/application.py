
# 1️ Importation des bibliothèques

import streamlit as st
import numpy as np
import joblib
import base64

# 2️ Configuration de la page

st.set_page_config(
    page_title="Diabetes Prediction App",
    layout="centered"
)

# 3️ Background 

def set_background(image_file):

    with open(image_file, "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

    page_bg = f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Grand titre */
    h1 {{
        color: #00CED1;
        font-weight: bold;
        text-align: center;
    }}

    /* Sous-titres */
    h2, h3 {{
        color: black;
    }}

    /* Labels */
    label {{
        color: black !important;
        font-weight: bold;
    }}

    /* Bouton */
    .stButton>button {{
        background-color: #2f3e46;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
    }}

    .stButton>button:hover {{
        background-color: #1f2a30;
        color: white;
    }}

    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

set_background("app/background1.png")


model = joblib.load("models/model_diabete_random_forest.pkl")




# 5️ Titre et description

st.title(" Prédiction du Risque de Diabète")
st.markdown("""
### Description 
Application de prédiction du risque de diabète développée en Machine Learning.

Le modèle, basé sur l’algorithme Random Forest, est entraîné sur le dataset Pima Indians Diabetes Database
et permet d’estimer la probabilité de diabète à partir de variables médicales.
""")

st.markdown("---") 
st.write("Veuillez saisir les informations médicales du patient ci-dessous :")


# 6️ Entrées utilisateur (bornées)

pregnancies = st.number_input("Nombre de grossesses", 0, 20, 1)

glucose = st.number_input("Taux de glucose", 0, 250, 120)

blood_pressure = st.number_input("Pression artérielle", 0, 200, 70)

skin_thickness = st.number_input("Épaisseur du pli cutané", 0, 100, 20)

insulin = st.number_input("Taux d'insuline", 0, 900, 80)

bmi = st.number_input("Indice de Masse Corporelle (IMC)", 0.0, 70.0, 25.0)

dpf = st.number_input("Indice héréditaire du diabète", 0.0, 3.0, 0.5)

age = st.number_input("Âge", 1, 100, 30)

# 7️ Bouton prédiction

if st.button("Predict") and 'model' in locals():

    # Créer array numpy
    input_data = np.array([[pregnancies,
                            glucose,
                            blood_pressure,
                            skin_thickness,
                            insulin,
                            bmi,
                            dpf,
                            age]])


    # Prédiction
    prediction = model.predict(input_data)

    # Probabilité de la classe 1 (diabète)
    probability = model.predict_proba(input_data)[0][1]

    # Résultat
    if prediction[0] == 1:
     st.error(f"Risque élevé de diabète (probabilité : {probability*100:.2f}%)")
    else:
     st.success(f"Risque faible de diabète (probabilité : {(1-probability)*100:.2f}%)")

st.markdown("---")
st.warning("Cette application fournit une estimation statistique et ne constitue pas un diagnostic médical professionel.")
st.markdown("Projet réalisé par Imane Chaouqi - 2026")