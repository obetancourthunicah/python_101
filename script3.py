#Estructura de Datos Tupla

errors = ( "no se encontro dato",
          "data ingresada es inválida",
          "no hay conexión" )

lstSquare = list()

point = (0, 0, 0) # x y z
lstSquare.append(point)
point = (10, 10, 0) # x y z
lstSquare.append(point)
point = (0, 0, 10)  # x y z
lstSquare.append(point)

for (x, y, z) in lstSquare:
  print(x,y,z, sep=":")
