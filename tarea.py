intRows = int(input("Número de Lineas: "))
intCols = int(input("Número de Columnas: "))

print("Coordenadas de Celdas\n")
for i in  range(intRows):
  for j in range(intCols):
    print("(" + str(i) + "," + str(j) + ")\n")
