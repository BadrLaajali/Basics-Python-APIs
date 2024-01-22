import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

# Chargement du DataFrame
happiness_df = pd.read_csv("happy.csv")

# Sélection des axes pour le graphique
x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"), index=0)
y_axis = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

# Vérification pour s'assurer que les axes X et Y ne sont pas identiques
if (x_axis != y_axis) :
    st.subheader(f"{x_axis} and {y_axis}")

    # Création du graphique de dispersion avec Plotly Express
    figure = px.scatter(happiness_df, x=x_axis.lower(), y=y_axis.lower(), labels={"x": x_axis, "y": y_axis})

    # Ajout d'un titre au graphique
    figure.update_layout(title=f"Relationship between {x_axis} and {y_axis}")

    # Affichage du graphique
    st.plotly_chart(figure)
else:
    st.error("Please select different options for X and Y axes.")
