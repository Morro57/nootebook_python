corsi = (
    ("Milano", [
        ("gennaio", ("online", 50)),
        ("gennaio", ("in presenza", 30)),
        ("febbraio", ("online", 40)),
        ("febbraio", ("in presenza", 25)),
        ("marzo", ("online", 35)),
        ("marzo", ("in presenza", 20)),
    ]),
    ("Bologna", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 40)),
        ("marzo", ("in presenza", 25)),
    ]),
    ("Roma",[
        ("gennaio", ("online", 40)),
        ("gennaio", ("in presenza", 25)),
        ("febbraio", ("online", 30)),
        ("febbraio", ("in presenza", 35)),
        ("marzo", ("online", 15)),
        ("marzo", ("in presenza", 40)),
    ])
)
#Richiesta città
while True:
    controllo=False
    cittàInp=input("Inserire città da analizzare: ")
    for citta,dati in corsi:
        if(cittàInp==citta):
            controllo=True
    if(controllo==True):
        break
    else:
        print("Errore, città inserita non esistente.")

#Richiesta tipologia
while True:
    controllo2=False
    tipoInp=input("Inserire la tipologia da analizzare: ")
    for citta,dati in corsi:
        for mese,info in dati:
            tipo,partecipanti=info
            if(tipoInp==tipo):
                controllo2=True

    if(controllo2==True):
        break
    else:
        print("Errore, la tipologia inserita non esistente.")

#funzione
def analizza_partecipanti(cittàInp,tipoInp):
    media_partecipanti=0
    cont=0
    max_partecipanti=0
    mese_max_partecipanti=""
    for citta,dati in corsi:
        if(cittàInp==citta):
            for mese,info in dati:
                tipo,partecipanti=info
                if(tipoInp==tipo):
                    media_partecipanti+=partecipanti
                    cont+=1
                    if(partecipanti>max_partecipanti):
                        max_partecipanti=partecipanti
                        mese_max_partecipanti=mese
    media_partecipanti/=cont
    return(round(media_partecipanti,2), (max_partecipanti, mese_max_partecipanti))

funzione=analizza_partecipanti(cittàInp,tipoInp)
print(funzione)