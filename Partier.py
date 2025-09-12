import random

partier = ["ap", "mdg", "h", "frp", "r", "sp", "sv", "krf", "v"]
stemmer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
stemmere = list(range(0,100))
flest = -1

def prosent_regning(stemmer):
    total = sum(stemmer)
    prosent = stemmer[i]
    svar = (prosent / total) * 100
    svar = round(svar,2)
    return svar

for i in stemmere:
    parti = random.choice(partier)
    for i in range(len(partier)):
        if parti == partier[i]:
           stemmer[i] += 1

for i in range(len(partier)):
    print(f"{partier[i]}: {stemmer[i]}")

print("Prosenten")
for i in range(len(stemmer)):
    print(prosent_regning(stemmer))

flestindex = -1

for i in range(len(stemmer)):
    if stemmer[i] > flest:
        flest = stemmer[i]
        flestindex = i

print(partier[flestindex])

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