#fonction qui  verifie si le numero est valide


def valid_num(chaine):
    if len(chaine)!=7 or not chaine.isupper() or chaine.isalpha() or chaine.isdecimal() or  not chaine.isalnum() :
        return False
    else:
        return True

#fonction qui  verifie si le prenom est valide


def valid_prenom(chaine):
    chaine= chaine.strip()
    if len(chaine)<3 or not chaine[0].isalpha() or not chaine.isalnum():
        return False
    else:
        return True
    
    
#fonction qui  verifie si le nom est valide


def valid_nom(chaine):
    chaine= chaine.strip()
    if len(chaine)<2 or not chaine[0].isalpha() or not chaine.isalnum():
        return False
    else:
        return True
    
    
# fonctions verifiant les classes
def valid_class(classe):
    if classe =='':
        return False
    if not classe[0].isdigit() or classe[-1].lower() not in ['a', 'b']:
        return False
    if int(classe[0])  > 6 or int(classe[0]) < 3:
        return False
    return True


#fonction qui  verfie la date



def valid_date(chaine):
    mois = {"ja": "1", "f": "2", "mars": "3", "av": "4", "mai": "5", "juin": "6", "juil": "7", "ao": "8", "sep": "9",
            "oct": "10", "nov": "11",
            "dec": "12"}
    chaine = chaine.strip()
    for x in chaine:
        if x in ["/", "-", ".", ",", ":", " ", "_", ".-", "-."]:
            chaine = chaine.split(x)
            break
    for keys in mois:
        if str(chaine[1].lower()).startswith(keys):
            chaine[1] = mois[keys]
            break
    liste = "/".join(chaine).replace(" ","/").replace("-","/").replace(".","/").replace(",","/")
    liste=liste.split("/")
    try:
        if (int(liste[-1])%4 == 0 and int(liste[-1])%100!= 0) or (int(liste[-1])%400== 0):
            if (int(liste[0]) < 1) or (int(liste[0]) > 31) or (int(liste[1]) < 1) or (int(liste[1]) > 12) or (
                        (int(liste[1]) == 2) and (int(liste[0]) > 29)):
                return False
            else:
                return True
        else:
            if (int(liste[0]) < 1) or (int(liste[0]) > 31) or (int(liste[0]) < 1) or (int(liste[1]) > 12) or (
                        (int(liste[1]) == 2) and (int(liste[1]) > 28)):
                return False
            else:
                return True
    except Exception as e:
        return False
    
import csv
data = open("data.csv")
data1 = csv.DictReader(data)
tabT=[]
tab_inv=[]
tabval=[]
for line in data1:
    line["Note"] = line["Note"].replace(",",";")
    if line["Numero"]==""or line["Nom"]=="" or line["Prénom"]==""or line["Date de naissance"]=="" or line["Classe"]=="" or line["Note"]=="" :
        tab_inv.append(line)

    elif not valid_num(line["Numero"]) or not valid_prenom(line["Prénom"])or not valid_nom(line["Nom"]) \
            or not valid_class(line["Classe"]) or not valid_date(line["Date de naissance"]):

        tabT.append(line)
    else:
        try:
            line["Note"] = line["Note"].split("#")
            d = {}
            for i in line["Note"]:
                i = i.split("[")
                i[1] = i[1].split("]")[0]
                d.setdefault(i[0], i[1])
                line["Note"] = d
            for i in line["Note"]:
                line["Note"][i] = line["Note"][i].split(":")
            liste1 = ["Devoir", "Exam"]
            moyin = 0
            for i in line["Note"]:
                line["Note"][i][0] = line["Note"][i][0].split(";")
                d = {k: v for k, v in zip(liste1, line["Note"][i])}
                d["Devoir"] = [float(c) for c in d["Devoir"]]
                d["Exam"] = float(d["Exam"])
                if (not d["Devoir"][0] or d["Devoir"][0] > 20) or (not d["Exam"] or d["Exam"] > 20):
                    tab_inv.append(line)
                else:
                    moy = (((sum(d["Devoir"]) / len(d["Devoir"]) + 2 * d["Exam"]) / 3)).__round__(2)
                    d.setdefault("Moyenne", moy)
                    line["Note"][i] = d
                    moyin = moy + moyin
            moyG = (moyin / len(line["Note"])).__round__(2)
            line["Note"].setdefault("moyG", moyG)
            tabval.append(line)
        except Exception as e:
            tab_inv.append(line)
Traiter=tabval
classement=[]
for i in range(len(Traiter)-1):
    listeclass=(Traiter[i]["Note"]["moyG"],i,Traiter[i]["Numero"])
    classement.append(listeclass)
classement.sort(reverse=True)


# creation menu
def MENU():
    print("***************MENU****************")
    print("Taper 1 si vous voulez afficher les informations: ")
    print("Taper 2 si vous voulez une information par son numero: ")
    print("Taper 3 pour afficher les cinq premiers: ")
    print("Taper 4 pour modifier les donner invalide: ")
    print("Taper 0 pour quitter")
    

while True:
    MENU()
    try:
        a = int(input("donne un nombre entre 0 et 4:"))
        print("--------------------------------------------------")
        if a in range(0,5):
            if(a==0):
                print("MERCI")
                break
            if(a==1):
                print("LES INFORMATIONS VALIDES")
                print(Traiter)
                print("LES INFORMATIONS INVALIDES")
                print(tab_inv)
            elif(a==2):
                id=int(input("donne l'id"))
                print(Traiter[id])
            elif(a==3):
                print(classement[:5])
            elif(a==4):
                print("attendre")
        else:
            print("erreur")
    except Exception as e:
        print("donner invalide")




