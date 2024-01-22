import requests
from sqlalchemy import DDL

API_KEY = ""

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    code_erreur = data["cod"]
    message_erreur = data["message"]
    if code_erreur != "200":
        filtered_data = []
    else:
        filtered_data = data["list"] #Key in API verb return
        # We have 8 entries for 24hours, API return 40 value inside the list because it's 5days
        # User can enter in forecast_days a number of day, so we multply by 8 to get the number of entries that we need to get from the API
        nbr_values = 8 * forecast_days 
        filtered_data = filtered_data[:nbr_values]        

    return filtered_data, code_erreur, message_erreur

if __name__=="__main__":
    get_data(place="Montreal", forecast_days=3)