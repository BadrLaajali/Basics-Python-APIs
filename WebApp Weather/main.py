import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")

place = st.text_input("Place : ")

days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if place:
    filtered_data, code_erreur, message_erreur = get_data(place, days)
    print (code_erreur)
    if code_erreur != "200":
        st.subheader(message_erreur + ": Error, check Place name and retry")
    else:
        st.subheader(f"{option} for the next {days} days in {place}")
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", 
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            #Extraire le chemin du dictionnaire images en se basant sur les sky_conditions retourner par l'API
            image_paths = [images[condition] for condition in sky_conditions]
            #for img in image_paths:
            st.image(image_paths, width=115)

