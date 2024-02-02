inGame = True
winsA = 0
winsB = 0

while inGame:
    jugadorA = input("Jugador A: ")
    jugadorB = input("Jugador B: ")
    
    if(jugadorA == "piedra"):
        if(jugadorB == "tijera"):
            winsA += 1
        elif(jugadorB == "papel"):
            winsB += 1
    elif(jugadorA == "papel"):
        if(jugadorB == "piedra"):
            winsA += 1
        elif(jugadorB == "tijera"):
            winsB += 1
    elif(jugadorA == "tijera"):
        if(jugadorB == "papel"):
            winsA += 1
        elif(jugadorB == "piedra"):
            winsB += 1
    
    print(f"""
          Puntos A      Puntos B
             {winsA}              {winsB}
          """)
    
    if(winsA == 3):
        inGame = False
        print("Jugador A ganador")
    elif(winsB == 3):
        inGame = False
        print("Jugador B ganador")
        