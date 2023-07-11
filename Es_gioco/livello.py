def livello():
    difficolta = input("Scegli la difficoltà: \n[1] Facile\n [2] Medio\n [3] Difficile\n")
    if difficolta=="1":
        tentativi_massimi=5
    elif difficolta=="2":
        tentativi_massimi=3
    elif difficolta=="3":
        tentativi_massimi=2
    else:
        print("Errore")
    return(tentativi_massimi)