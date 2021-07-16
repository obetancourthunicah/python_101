# Estructura de Diccionario
# Los diccionarios en python 3.6 o menor no son ordenados
# Los diccionarios en python 3.7 o superior SON ORDENADOS
dctPersona = {
  "codigo":"0801198412349",
  "nombre":"Orlando",
  "apellido":"Betancouth",
  "direccion":"Col Roble Oeste Lote 3",
  "telefonos": list(["00000000","11111111"]),
  "amigos": list(
    [
      {"nombre": "Amigo 1", "tel": "88888888"},
      {"nombre": "Amigo 2", "tel": "77777777"},
    ]
  )
}

print(dctPersona)

print(("-"*80))

print(dctPersona["direccion"])
