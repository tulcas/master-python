"""
Ejericio 10
Nota de 10 alumnos y cuantos aprobados y desaprobados
"""

i = 1
aprobado = 0
des_aprobado = 0
while i <= 10:
    nota = int(input(f"Ingresa la nota del alumno numero: {i} : "))
    i += 1
    if nota >= 7:
        aprobado += 1
    else:
        des_aprobado += 1
    
print(f"TOTAL APROBADOS : {aprobado}")
print(f"TOTAL DES-APROBADOS : {des_aprobado}")
