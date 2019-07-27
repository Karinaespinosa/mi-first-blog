KEF="Karina Espinosa Flores"
print(KEF)
print("hello word "+ KEF)
if 9<20:
    print("correcto")
if 9>20:
    print("incorrecto")
else:
    print("9 no es mayor que 20")
if "Patricia" in KEF:
    print("este no es mi nombre")
elif "Karina" in KEF:
    print ("ese es mi nombre")
else:
    print("¿Cómo te llamas?")

segundo_nombre="Patricia"
if segundo_nombre in KEF:
    print ("tengo un segundo nombre" + "Me llamo Karina Patricia")
elif segundo_nombre not in KEF:
    print("tengo solo un nombre " + "es Karina con K")

primer_apellido="Espinosa"
if primer_apellido in KEF:
    print("Espinosa con s " + "porfavor")
elif primer_apellido not in KEF:
    print("ese no es mi apellido, mi apellido es Román")
else:
    print ("¿Cúal es tu apellido?")

    
