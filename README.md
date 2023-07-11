# gioco_parole
---

Repository contenente il gioco dell'impiccato. Indovina la parola!

- Il programma chiede al giocatore

> "Ti va di giocare?

accettando in input un "si" --> si ha accesso al programma, altrimenti si esce

- il programma ti permette di scegliere la difficolta di gioco [facile], [media] o [difficile] tramite i numeri 1, 2 o 3. La differenza sta nel numero di tentativi sbagliati concessi all'utenti nell'indovinare le lettere nella parola

>     difficolta = input("Scegli la difficoltà: \n
>     
>       [1] Facile\n
>     
>       [2] Medio\n
>     
>       [3] Difficile\n")
> 
>     if  difficolta=="1":
>     
>         tentativi_massimi=5
>     
>     elif  difficolta=="2":
>     
>         tentativi_massimi=3
>     
>     elif  difficolta=="3":
>     
>         tentativi_massimi=2
>     
>     else:
>     
>         print("Errore")

- Il programma pesca randomicamente una `parola` da una lista di parole chiamata `lista_parole` e crea una `parola_segreta` composta da tanti "_ " quante sono le lettere nella parola

- l'utente gioca inserendo una lettera per volta cercando di indovinare tutte le lettere della parola

- l'utente inserisce una `lettera`

- se la lettera è presente nella parola, comparirà al posto degli underscore corrispondenti e si aggiorneranno dei contatori che contano se la lettera è tra le presenti (`count_lettera`) e quante lettere della parola abbiamo indovinato (`count_parola`) :

>      if parola[i]==lettera:
>     
>          list_parola_segreta[2*i]=lettera
>     
>          count_lettera+=1
>     
>          count_parola+=1

- se la lettera non è tra le presenti (`count_lettera == 0`) hai un tentativo disponibile in meno:

>      if count_lettera==0: # se la parola non è presente, aggiorno i tentativi
>     
>          tentativi_sbagliati+=1
>     
>          print("La lettera non è presente! Riprova. Tentativi rimasti: ", tentativi_massimi-tentativi_sbagliati, "\n")

- altrimenti aggiorniamo la parola segreta

    > else:
    > 
    >      parola_segreta=listToString.listToString(list_parola_segreta)
    > 
    >       print("Parola: ", parola_segreta, "\n")

- Il gioco finisce quando finiscono i tentativi. Se però si indovina, il gioco continua proponendo una nuova parola.
