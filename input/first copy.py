# Premier Traitement

chaine = input("Nom et Prenom ?")
print(chaine)

nom = chaine.split()
print(nom)


print(type(nom))
print(len(nom))

len_listnom = len(nom)
if len_listnom == 2:
    print("nom : " + nom[0]+", prenom : " + nom[1])
elif len_listnom == 3:
    print(f"prénom : {nom[0]} , milieu : {nom[1]} nom :  {nom[2]}")
elif len_listnom == 1:
    print("nom : " + nom[0])
else:
    print("Format demandé: prénom <milieu> nom ")
    print("que faire de : " + " ".join(nom[3:]))
