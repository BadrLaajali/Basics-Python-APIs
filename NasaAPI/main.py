import requests
import streamlit as st

api_key = ""
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Effectuer la requête GET
response = requests.get(url)
# Obtenir le contenu de la réponse sous forme de JSON
data = response.json()
#Initialise data into variables
img_url = data["url"]
img_title = data["title"]
img_description = data["explanation"]

get_img = requests.get(img_url)
img_data = get_img.content

#Save the picture
with open("image.jpg", 'wb') as img:
    img.write(img_data)

#Create web page
st.set_page_config(layout="centered")

st.title(img_title)
st.image("image.jpg", width=600)
st.info(img_description)
