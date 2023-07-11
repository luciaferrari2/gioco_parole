## GIOCO DELL'IMPICCATO ##

#1) Richiesta: "Vuoi giocare?" ----> accesso
#2) Abbiamo una lista di parole ----> lista_parole
#3) Numero tentativi sbagliati ----> tentativi_sbagliati
#4) Stringa che prende randomicamente una parola da lista_parole ----> parola
#5) Input dell'utente ----> lettera
#6) Due condizioni per uscire dai cicli for/while ----> tentativi finiti o parola trovata
#7) Inizializzare una stringa composta da "_" di lunghezza = len(parola) ----> parola_segreta


import random
import listToString
import livello

tentativi_massimi=5
tentativi_sbagliati=0

lista_parole =["casa","Java","Python","pizza","caffè","giraffa","parallelepipedo","contemporaneamente"]
parola_corretta = True # se la parola precedente è corretta voglio continuare a giocare

# Richiesta: "Vuoi giocare?" ----> accesso e scegli difficoltà
accesso=input("Ti va di giocare?\n [Sì] [No]\n").lower()

if accesso in ["si","sì"]:
    tentativi_massimi=livello.livello() #funzione che permette all'utente di scegliere il livello di difficoltà

    # Iniziamo il ciclo, che ricomincia se non abbiamo superato il massimo di tentativi (quindi se la parola è stata trovata)
    while tentativi_sbagliati<=tentativi_massimi:
        tentativi_sbagliati=0
        parola=random.choice(lista_parole).lower()
        parola_segreta='_ '*len(parola)
        list_parola_segreta=list(parola_segreta)
        print("Parola: ", parola_segreta, "\n")

        count_parola=0 # inseriamo un contatore per capire quando abbiamo inserito tutte le lettere della parola

        while tentativi_sbagliati<tentativi_massimi and not count_parola==len(parola): # Esco dal ciclo se supero i tentativi o se indovino la parola
            lettera=input("Che lettera vuoi aggiungere? \n").lower()

            count_lettera=0 # inseriamo un contatore per contare le lettere inserite e capire se sono presenti o meno

            for i in range(len(parola)): #scorro la parola e aggiorno la parola_segreta se trovo la lettera inserita dall'utente
                if parola[i]==lettera:
                    list_parola_segreta[2*i]=lettera
                    count_lettera+=1
                    count_parola+=1
            if count_lettera==0: # se la lettera non è presente, aggiorno i tentativi
                tentativi_sbagliati+=1
                print("La lettera non è presente! Riprova. Tentativi rimasti: ", tentativi_massimi-tentativi_sbagliati, "\n")
            else:
                parola_segreta=listToString.listToString(list_parola_segreta)
                #parola_segreta="".join(map(str,list_parola_segreta))
                print("Parola: ", parola_segreta, "\n")

        if count_parola>=len(parola):
            print("Parola trovata! Puoi continuare il gioco.\n")

    print("Hai perso! Tentativi esauriti.\n")