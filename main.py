from chainageAvant import *
from Rule import *
from chainageArriere import *
import os

def Menu():
    print("Veuillez choisir une des trois options suivantes:  ")
    print("1....Chainage Avant")
    print("2....Chainage Arrière")
    print("3....Quitter")
    print("> ",end="")
    choix = input()
    if(0<int(choix)<4):
        return choix
    else:
        print("Option invalide",end=",")
        Menu()

def ManualInput(Faits, Regles):
    print("Veuillez Remplir les tables suivantes: ")
    print("---Table de Faits---")
    print("Quelle est la taille de cette table?")
    Taille_Faits = input(">")
    for i in range(int(Taille_Faits)):
        Faits.append(input(f"Saisir le fait N°{i+1} >"))


    print("---Table de Règles---")
    print("Quelle est la taille de cette table?")
    Taille_Règles = input(">")
    print("Entrer les règles sous la forme:  Nom_Règle : liste_données -> liste_resultat")
    print("Exemple: R1 : A,B -> C,D")

    for i in range(int(Taille_Règles)):
        tmp = input(f"Saisir la règle N°{i+1} >")
        name = tmp.split(":")[0].replace(" ","")
        donnee = [x for x in tmp.split(":")[1].split("->")[0].replace(" ","").split(",")]
        results = [x for x in tmp.split(":")[1].split("->")[1].replace(" ","").split(",")]
        NewRule = Rule(name,donnee,results)

        Regles.append(NewRule)


def FileInput(Faits, Regles,NbrFacts,NbrRules, Fait_Filename,Regle_Filename):
    with open(os.path.join(Fait_Filename),"r") as FaitsInp:
        for i in range(int(NbrFacts)):
            Faits.append(FaitsInp.readline().replace("\n",""))
        FaitsInp.close()
    with open(os.path.join(Regle_Filename),"r") as RegleInp:
        for i in range(int(NbrRules)):
            tmp = RegleInp.readline()
            name = tmp.split(":")[0].replace(" ","")
            donnee = tmp.split(":")[1].strip().split("ALORS")[0].replace("[","").replace("]","").replace("SI","").replace(" ","")
            resultat = tmp.split(":")[1].strip().split("ALORS")[1].replace(" ","").replace("[","").replace("]","")

            NewRule = Rule(name,[x for x in donnee.split(",") if x != ""],[x for x in resultat.split(",") if x != ""])
            Regles.append(NewRule)
        RegleInp.close()



def Main():
    Regles = []
    Faits = []
    print("Choisissez la méthode de saisie des données")
    print("1....Saisie manuelle ")
    print("2....Lecture depuis un fichier")
    choixInp = input(">")
    
    match choixInp:
        case "1":
            ManualInput(Faits, Regles)
        case "2":
            print("Saisir le nom du fichier contenant les faits")
            NomFaits = input(">").strip()
            NbrFaits = input("Nombre de Faits dans ce fichier \n >")
            print("Saisir le nom du fichier contenant les Règles")
            NomRegles = input(">").strip()
            NbrRegles = input("Nombre de règles dans ce fichier \n >")
            FileInput(Faits, Regles,NbrFaits,NbrRegles,NomFaits,NomRegles)

        case _:
            print("Option invalide")


    while(True):
        choix = Menu()
        try:
            match choix:
                case "1":
                    
                    NewRules,NewFacts = Avant(Regles,Faits)
                    print(NewRules)
                    print(NewFacts)
                case "2":
                    print("Quel est votre but?")
                    target = input(">")

                    tmpRegle = [x for x in Regles]
                    tmpFaits = [x for x in Faits]

                    Exists = Arriere(tmpRegle,tmpFaits,target)
                    if(Exists[0]):
                        print("Le but est atteint !!!")
                        print(f"Voici la nouvelle base de Faits: {Faits}")
                        print(f"Voici la nouvelle base de Règles: {Exists[1]}")
                    else:
                        print("Impossible de le trouver !!")
                case "3":
                    print("Au revoir ....")
                    break
                case _:
                    print("Vous avez selectionner un mauvais choix")
                    break
        except:
            print("Quelque chose c'est passée...")

if __name__ == "__main__":
    Main()