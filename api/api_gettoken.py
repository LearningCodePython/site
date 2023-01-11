# by : Cristo Emiliano Hernandez Darias 
#
## Repo API_Yeastar in 10.19.19.16/BonoboGit
## Nueva rama para hacer pruebas con la central de Guayarmina 10.102.0.10

## take_toke.py se concecta con la central y almacena en la variable tocken el valor de token necesario
## para posteriormente hacer el POST a la central, necesario para interectuar con la API de la Yeastar

import requests
from requests.models import Response
import urllib3
import api_data

urllib3.disable_warnings()

def getoken (): # Función que captura el token para almacenarlo en la variable toke.
  """_summary_
    Función que nos devuelve el token necesario para el resto de acciones,
    se almacena en la variable token
  """
  url = "https://" + api_data.host + ":8088/api/v1.1.0/login"
  payload="{ \"username\":" + api_data.api_user + ",\"password\":" + api_data.api_password+ ",\"port\": \"8260\"}"
  headers = {
    'Content-Type': 'text/plain'
  }
  r = requests.post(url, headers=headers, data=payload, verify=False)
  jsonResponse = r.json()
  token = (jsonResponse["token"]) #Selecciona al valor de la clave "token"
  print (token)
  #return token

getoken()
