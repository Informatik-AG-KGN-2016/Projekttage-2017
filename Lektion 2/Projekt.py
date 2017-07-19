while True:

    jahr = int(input("In welchem Jahr bist du gebobren?"))
    monat = int(input("in welchem Monat (als Zahl) hast du Geburstag?"))
    tag = int(input("Am wie vielten Tag hast du Geburstag?"))
    uhrzeit = int(input("Um wie viel Uhr hast du Geburstag?"))
    name = int(input("Wie lautet dein Name?"))
    alter = 2018 - jahr
    alter1 = 2017 - jahr


    if jahr > 2018:
        print("Du Lügner,das Jahr exsestiert noch nicht")
    elif jahr < 2017:
        print ("WOW")

    if monat < 7:
        print("Du hattest schon Geburstag ,OPFER!")
    elif monat > 7:
        print ("Du hast noch Geburtstag dieses Jahr, *Du Opfer*!!!")

    if tag == 18 and monat == 7:
        print("Glückwunsch, du hast geburstag, genau an dem tag wo dieser text erstanden ist!") 

    if uhrzeit == 9 and tag ==18:
        print("Boah,KRAASS,um Neun uhr ist die Uhrzeit vom Text entstanden")

    if name < Boris 
       print("Willkommen in Deutsche Land")

    elif name < Arian 
        print("Hallo mein Herrscher!")

    #if tag == 18 and monat == 7:
    #    print("Glückwunsch, du hast geburstag, genau an dem tag wo dieser text erstanden ist!")





    alter = 2018-jahr
    print("Du bist jetzt", alter , "Jahre alt.")

    antwort = input("\nWollen Sie noch einmal? (yes/no) ")

    if antwort != "yes":
        break
    else:
        print("\n\n")
