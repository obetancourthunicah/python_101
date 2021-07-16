# https://randomuser.me/

# Importar una libreria estandar de python que
# permite realizar peticion http o https
# poder analizar y revisar el contenido devuelto

# Convertir con otra libreria la respuesta en json
# a un diccionario de python

import requests
import json

url = "https://randomuser.me/api/?results=10"

response = requests.get(url)

jsonDataString = response.text

jsonDictionary = json.loads(jsonDataString)


#persona = jsonDictionary["results"][0]

def imprimirRegistro(persona):
  nombre = persona["name"]["first"] + " " + persona["name"]["last"]
  correo = persona["email"]
  genero = persona["gender"]
  telefono = persona["phone"]
  edad = persona["dob"]["age"]
  print(nombre, correo, genero, telefono, edad, sep=",")

for currentPersona in jsonDictionary["results"]:
  imprimirRegistro(currentPersona)

#print(json.dumps(persona, indent=4, sort_keys=True))
#print(len(jsonDictionary["results"]))
#print(json.dumps(jsonDictionary, indent=4, sort_keys=True))
