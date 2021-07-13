#Estructuras de datos
#Lista
intItems = int(input("Items en la lista"))
lstItems = list()
for i in range(intItems):
  item = input("Agregar Item " + str(i + 1) + " :")
  lstItems.append(item)

#len duevuelve la cantidad de elementos en una lista
for j in range(len(lstItems)):
  #lstItems[j] = lstItems[j] + " printed"
  print("Item " + str(j + 1) + " :" + lstItems[j])

#Encontrar un elemento dentro de una lista (valor)
strSearch = input("Buscar en : ")
if strSearch in lstItems:
  print("Si hay en la lista")
else:
  print("No se encontro en la lista")
