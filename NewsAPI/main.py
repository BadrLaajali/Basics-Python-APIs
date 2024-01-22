import requests, json, smtplib, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Paramètres du serveur SMTP
smtp_server = "smtp.hostinger.com"
smtp_port = 465
username = ""
password = ""

#Définition de la date
# Obtenir la date et l'heure actuelles
now = datetime.datetime.now()
# Créer un objet timedelta pour un jour
one_day = datetime.timedelta(days=1)
# Soustraire un jour de la date actuelle
yesterday = now - one_day
# Formater la date de J-1
formatted_yesterday = yesterday.strftime("%Y-%m-%d")

# Création de l'objet message
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = "XXXX@gmail.com"  # Remplacez par l'adresse e-mail du destinataire
msg['Subject'] = "Les news pour : " + formatted_yesterday

#Research criterias
categorie = "finance"
language = "en"
# Votre clé API et l'URL
api_key = "000ba67e53c74c899e64655ba636bdd7"
url = f"https://newsapi.org/v2/everything?q={categorie}&from={formatted_yesterday}&language={language}&sortBy=publishedAt&apiKey={api_key}"

# Effectuer la requête GET
response = requests.get(url)
# Obtenir le contenu de la réponse sous forme de JSON
content = response.json()
# Enregistrer ce contenu dans un fichier JSON
with open('articles.json', 'w') as json_file:
    json.dump(content, json_file, indent=4)

body = "Voici la liste des news : "
for data in content["articles"][:5]:
    # Corps de l'e-mail
    body += f"<h2>{data['title']}</h2>"
    body += f"<p>{data['description']}</p>"
    body += f"<p><a href='{data['url']}'>Lire</a></p>"
    
#Envoi de courriel
msg.attach(MIMEText(body, 'html'))
# Connexion au serveur SMTP et envoi de l'e-mail
try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(username, password)
    server.sendmail(username, msg['To'], msg.as_string())
    server.quit()
    print("E-mail envoyé avec succès !")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'e-mail : {e}")
