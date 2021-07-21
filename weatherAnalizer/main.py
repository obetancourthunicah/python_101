import lectorDeClima
import climaModeloDatos

print("Buscando Data de Tegucigalpa")
print ("-"*80)
climaDataApi = lectorDeClima.obtenerClima("Tegucigalpa")
ciudad = climaDataApi["name"]
pais = climaDataApi["sys"]["country"]
idciudad = climaDataApi["sys"]["id"]
temperatura = climaDataApi["main"]["temp"]
humedad = climaDataApi["main"]["humidity"]
presion = climaDataApi["main"]["pressure"]
tempmax = climaDataApi["main"]["temp_max"]
tempmin = climaDataApi["main"]["temp_min"]
temppercibida = climaDataApi["main"]["feels_like"]

#Agregando registro a la DB
ClimaDatos = climaModeloDatos.ClimaDatos()
ClimaDatos.agregarClima(ciudad, pais, idciudad, temperatura,
                        humedad, presion, tempmax, tempmin, temppercibida)
