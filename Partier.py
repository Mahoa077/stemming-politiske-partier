

partier = ["arbeiderpartiet", "miljøpartet de grønne", "høyre", "fremskrittpartiet", "rødt", "senterpartiet", "sosialistisk venstre", "kristelig folkeparti", "venstre"]
stemmer = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]

should_continue = True


while should_continue:
    print (f"Du kan stemme disse partiene {partier}")
    stemme = input("Skriv partiet du vil stemme på: ").lower()
    print (f"Du stemte {stemme}")
    
    if stemme == "stop":
        print("Stopper stemmingen")
        should_continue = False
    elif stemme not in partier:
        print ("ikke lov å stemme det!")
    elif input == "stemme":
        print("Ny person kan stemme")
        input("Stem: ")
