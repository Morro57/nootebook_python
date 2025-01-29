tupla_partite = (
    ("GiocatoreA", "GiocatoreB", 3, 2),
    ("GiocatoreC", "GiocatoreD", 2, 3),
    ("GiocatoreB", "GiocatoreC", 3, 0),
    ("GiocatoreA", "GiocatoreD", 3, 1),
    ("GiocatoreB", "GiocatoreD", 2, 3),
)

#P1
def media_set_partita(tupla_partite):
    media=0
    cont=0
    for giocatore1,giocatore2,set1,set2 in tupla_partite:
        media+=set1+set2
        cont+=1
    media /= cont
    return f"La media dei set giocati è di {media:.2f}."


#P2
def media_set_giocatore(tupla_partite, giocatore):
    media=0
    cont=0
    for giocatore1,giocatore2,set1,set2 in tupla_partite:
        if(giocatore==giocatore1 or giocatore==giocatore2 ):
            media=set1+set2
            cont+=1

    media/=cont
    return f"La media dei set vinti dal {giocatore} è di {media:.2f} set vinti."


#P3
def match_piu_combattuto(tupla_partite): 
    giocatore1max=""
    giocatore2max=""
    set1max=0
    set2max=0
    max=0
    setTot=0
    for giocatore1,giocatore2,set1,set2 in tupla_partite:
        setTot=set1+set2
        if(setTot>max):
            max=setTot
            set1max=set1
            set2max=set2
            giocatore1max=giocatore1
            giocatore2max=giocatore2
    print(f"(Set giocati,({giocatore1max} - {giocatore2max}))")
    return (max,(set1max,set2max))

#P4
def match_meno_combattuto(tupla_partite):
    giocatore1min=""
    giocatore2min=""
    set1min=0
    set2min=0
    min=10
    setTot=0
    for giocatore1,giocatore2,set1,set2 in tupla_partite:
        setTot=set1+set2
        if(setTot<min):
            min=setTot
            set1min=set1
            set2min=set2
            giocatore1min=giocatore1
            giocatore2min=giocatore2
    print(f"(Set giocati,({giocatore1min} - {giocatore2min}))")
    return(min,(set1min,set2min))

#P5
def percentuale_vittorie_giocatore(tupla_partite, giocatore):
    vinta=0
    cont=0
    percentuale=0
    for giocatore1,giocatore2,set1,set2 in tupla_partite:
        if(giocatore==giocatore1):
          cont+=1
          if(set1>set2):
              vinta+=1  
        elif(giocatore==giocatore2 ):
            cont+=1
            if(set1<set2):
                vinta+=1
    percentuale=(vinta/cont)*100
    return f"La percentuale di partite vinte dal {giocatore} è del {percentuale:.2f}%."

#Menù
while True:
    scelta=int(input("Menù:\n1. Visualizzare la media dei set per partita;\n2. Visualizzare media del set di un giocatore;\n3. Mostra il match più combattuto;\n4. Mostra match meno combattuto;\n5.Visualizza percentuale vittorie di un giocatore;\n6. Esci."))
    if(scelta<1 or scelta>6):
        print("Errore nella digitazione")
    elif(scelta==1):
        print(media_set_partita(tupla_partite))
    elif(scelta==2):
        while True:
            controllo=False
            giocatoreInp=input("Inserisci il nome del giocatore da visualizzare: ")
            for giocatore1,giocatore2,set1,set2 in tupla_partite:
                if(giocatoreInp==giocatore1 or giocatoreInp==giocatore2 ):
                    controllo=True

            if(controllo==True):
                print(media_set_giocatore(tupla_partite, giocatoreInp))
                break
            else:
                print("Errore,giocatore non esistente o non trovato.")

    elif(scelta==3):
        print(match_piu_combattuto(tupla_partite))
    elif(scelta==4):
        print(match_meno_combattuto(tupla_partite))
    elif(scelta==5):
        while True:
            controllo=False
            giocatoreInp=input("Inserisci il nome del giocatore da visualizzare: ")
            for giocatore1,giocatore2,set1,set2 in tupla_partite:
                if(giocatoreInp==giocatore1 or giocatoreInp==giocatore2 ):
                    controllo=True

            if(controllo==True):
                print(percentuale_vittorie_giocatore(tupla_partite, giocatoreInp))
                break
            else:
                print("Errore,giocatore non esistente o non trovato.")
    elif(scelta==6):
        print("Programma terminato.")
        break