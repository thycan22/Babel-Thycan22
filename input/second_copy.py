import re

# Premier Traitement

F_FIRSTNAME = "firstname"
F_MIDDLENAME = "middle"
F_LASTNAME = "lastname"
F_FULLNAME = "fullname"
F_ERRORE = "erreur"


def validate_juststring(input):
    """si la string input contient juste des caractères A-Z"""
    # si vide
    # enlevé les espaces
    # regarde si AZ ou az
    if not len(input):
        return False
    r = re.match("^[A-Za-z]+$", input)
    print(r)
    return True if r else False


def validate_display(in_nom):
    """ 
        validation et affichage d'un string
        selon format prénom <milieu> nom
    """
    nom = in_nom.split()
    # print(nom)
    print(type(nom))
    # print(len(nom))

    # vérifier que chaque str de nom ne comporte que des lettres de l'alphabet
    type(nom)
    d = {}
    for n in nom:
        # n=n.strip() enleve les espaces
        if not validate_juststring(n):
            # return error
            d += {F_ERRORE: 'erreur de validation : '+n}

    if verifCharactere(nom):
        len_listnom = len(nom)
        if len_listnom == 2:
            d = {F_FIRSTNAME: nom[0], F_LASTNAME: nom[1]}

        elif len_listnom == 3:
            d = {F_FIRSTNAME: nom[0],
                 F_MIDDLENAME: nom[1], F_LASTNAME: nom[2]}

        elif len_listnom == 1:
            d = {F_FIRSTNAME: nom[0]}

        else:
            return
            "Format demandé: prénom <milieu> nom , que faire de : " + \
                " ".join(nom[3:])
    else:
        d = {F_ERRORE: "Que des caractères !"}
    return d


def manage_input():
    chaine = input("Nom et Prenom ?")
    return chaine


def verifCharactere(chaine):
    if isinstance(chaine, int):
        return False
    else:
        return True


if __name__ == '__main__':
    manage_input()
