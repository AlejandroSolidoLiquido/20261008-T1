estudiante1 = float(input("Nota de la examen (de 0 a 100): "))
porcentaje1 = float(input("Asistencia en clase de 0 a 100 " ))
 
porcentaje1 = float(porcentaje1 / 40 * 100)
if 0 <= estudiante1 <= 100:
    if estudiante1 >= 70:
     print("Aprobado en examen")
    else:
     print("Suspenso en examen")

if 0 <= porcentaje1 <= 100:
    if porcentaje1 >= 80:
     print("Aprobado en asistencia")
    else:
     print("Suspenso en asistencia")

if estudiante1 == 100:
    print("Eres un figuta")
elif estudiante1 >= 90:
    print("Eres un maquina")
elif estudiante1 >= 80:
    print("Vas sobrado cabron")
elif estudiante1 >=70:
    print("Vas bien pero puedes mejorar")
elif estudiante1 >= 60:
    print("Vas mal pero puedes mejorar")
elif estudiante1 >= 50:
    print("Vas muy mal pero puedes mejorar")
elif estudiante1 < 50:
    print("Estas suspendido cabron")    