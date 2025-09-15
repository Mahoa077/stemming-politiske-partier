import random
#denne har jeg brukt for å få et random tall hver gang koden går

partier = ["ap", "mdg", "h", "frp", "r", "sp", "sv", "krf", "v"]
stemmer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
stemmere = list(range(0,100))
flest = -1
output1 = ""
output2 = ""
output3 = ""

# her har jeg gitt ulike variabler verdier 

def prosent_regning(stemmer):
    total = sum(stemmer)
    prosent = stemmer[i]
    svar = (prosent / total) * 100
    svar = round(svar,2)
    return svar

#så her har jeg brukt ulike variabler til å finne ut av hvor mange prosent stemmer hvert parti har fått, ut av 100 prosent

for i in stemmere:
    parti = random.choice(partier)
    for i in range(len(partier)):
        if parti == partier[i]:
           stemmer[i] += 1

#her har jeg brukt randomchoice for å få et random antall stemmer til de ulike partiene ut av 100. Jeg har gjort sånn at hvis parti er i parti listen, så skal den få 1 stemme til hvis den blir stemt på

for i in range(len(partier)):
    output1 += f"{partier[i]}: {stemmer[i]}\n"
print (output1)
#her printer jeg ut partiene og hvor mange stemmer hvert parti fikk

print("Prosenten")
for i in range(len(stemmer)):
    output2 += (f"{partier[i]}: {prosent_regning(stemmer)}\n")
print (output2)
#her printer jeg ut pariet og hvor mange prosent stemmer de fikk ut av 100 stemmer, i prosentanndel

flestindex = -1

for i in range(len(stemmer)):
    if stemmer[i] > flest:
        flest = stemmer[i]
        flestindex = i
    # her har jeg lagd en for løkke som finner ut av hvilket parti som har flest stemmer
print (f"Partiet med flest stemmer er {partier[flestindex]}")
#denne printer ut det partiet med flest stemmer nede i terminalen
output3 += (f"Partiet med flest stemmer er {partier[flestindex]}")
#denne printer ut hvilket parti som har mest stemmer inne i det nye dokumentet. Grunne til at jeg har denne utafor for løkken er at hvis jeg har den inne i for løkken, så vil den printe ut flere partier i det nye dokumentet. som da er feil og ikke det jeg vil. 

with open("my_file.txt", "w") as file:
    file.write(output1)
    file.write("\n")
    file.write("Prosent stemmer \n")
    file.write(output2)
    file.write("\n")
    file.write(output3)
#dette er opsettet inne i mitt nye dokument som viser hva som blir printet ut. Så jeg har skrevet det opp som jeg vil at det skal komme inne i det nye dokumentet. 


#

""""
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
    for i in range(len(partier)):
        if stemme == partier[i]:
           stemmer[i] += 1
           print (stemmer[i])


for i in range(len(partier)):
    print(f"{partier[i]}: {stemmer[i]}")

print("Prosenten")
for i in range(len(stemmer)):
    print(prosent_regning(stemmer))

"""