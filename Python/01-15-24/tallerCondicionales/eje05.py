temperatura = float(input("-Temperatura: "))
presion = float(input("-Presion: "))

if(presion > 200 or temperatura > 100):
    print("¡¡ALARMA!!")
else:
    print("Normal")
