# import fileinput
# Los Comentarios en Python son conel numeral
print("=" * 80)
print("Mi Primer Script de Python")
print("=" * 80)
print()
print("Escriba su Edad ", end="->\n")
inputdata = int(input())
edad = inputdata
if edad > 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")
  for i in range(edad):
    print(str(i+1)+" Missisippi!!!")
