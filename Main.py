#Para que no digan que no lo puse
print("Hello World!")


# funcion de clase para convertir hora en minutos

hora = input("Ingrese la hora: ")

#intentando evitar problemas de input

if ("." in hora) or ("," in hora):
  hora_num = float(hora)

elif ":" in hora:
  nueva_hora = hora.replace(":", ".")
  hora_num = float(nueva_hora)
else:
  hora_num = int(hora)

#convertir hora en minutos
minutos = hora_num *60

# mostrar el resultado de manera "bonita"
print(f"""la hora ingresada es {hora}
{hora_num} horas contienen {minutos} minutos""")
