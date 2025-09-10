

partier = ["Arbeiderpartiet", "Miljøpartiet De Grønne", "Høyre", "FremskrittPartiet", "Rødt", "Senterpartiet", "Sosialistisk Venstre", "Kristelig Folkeparti", "Venstre"]
stemmer = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
svar2 = ["arbeiderpartiet", "miljøpartet de grønne", "høyre", "fremskrittpartiet", "rødt", "senterpartiet", "sosialistisk venstre", "kristelig folkeparti", "venstre"]



if True:
    print (f"Du kan stemme disse partiene {partier}")
    stemme = input("skriv partiet du vil stemme på: ").lower()
    print (f"Du stemte {stemme}")
    if stemme != "partier":
        print ("ikke lov å stemme det!")