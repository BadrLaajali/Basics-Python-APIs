# Importation des modules nécessaires
from flask import Flask, render_template
import pandas as pd

# Création d'une instance de l'application Flask
# "__name__" est une variable spéciale utilisée par Flask pour déterminer l'emplacement de l'application
app = Flask(__name__)

stations_df = pd.read_csv("./data_small/stations.txt", skiprows=17)
stations_df = stations_df[['STAID','STANAME                                 ']]

# Définition de la route pour la page d'accueil
# La route "/" correspond à la racine du site web
@app.route("/")
def home():
    # Rendu du template HTML pour la page d'accueil
    # Flask cherchera le fichier "home.html" dans le dossier "templates"
    return render_template("home.html", data=stations_df.to_html())

# Définition de la route pour une API
# Cette route accepte des variables dynamiques 'station' et 'date' dans l'URL
@app.route("/api/v1/<station>/<date>")
def details(station, date):
    file_name = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
    weather_df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
    temperature = weather_df.loc[weather_df['    DATE'] == date]['   TG'].squeeze() / 10
    # Renvoi d'une réponse au format JSON avec les données demandées
    return {"station": station, 
            "date": date, 
            "temperature": temperature}
   
#Get all data for a specific station
@app.route("/api/v1/<station>")
def bystation(station):
    file_name = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
    weather_df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
    result = weather_df.to_dict(orient="records")
    return result

#Get data for a specific year in a specific station
@app.route("/api/v1/yearly/<station>/<year>")
def byyear(station, year):
    file_name = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
    weather_df = pd.read_csv(file_name, skiprows=20)
    weather_df["    DATE"] = weather_df["    DATE"].astype(str)
    result = weather_df[weather_df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

# Vérifie si le fichier est le module principal exécuté
# Utile pour éviter que certaines parties du code s'exécutent lorsqu'elles sont importées comme module
if __name__ == "__main__":
    # Exécution de l'application en mode développement
    # Le paramètre debug=True active le mode débogage pour faciliter le développement
    app.run(debug=True)
