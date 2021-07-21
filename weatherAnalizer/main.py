import lectorDeClima
import climaModeloDatos

def buscar (ciudad, ClimaDatos):
  print("Buscando Data de " + ciudad)
  print("-"*80)
  climaDataApi = lectorDeClima.obtenerClima(ciudad)
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
  ClimaDatos.agregarClima(ciudad, pais, idciudad, temperatura,
                          humedad, presion, tempmax, tempmin, temppercibida)


try:
  ClimaDB = climaModeloDatos.ClimaDatos()
  buscar("Tegucigalpa", ClimaDB)
  buscar("San Pedro Sula", ClimaDB)
  buscar("La Ceiba", ClimaDB)
  buscar("Juticalpa", ClimaDB)
  buscar("Siguatepeque", ClimaDB)
except:
  print("Ocurrio un error al procesar")
