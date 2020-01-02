# premier traitement


F_FIRST = "firstname"
F_LAST = "lastname"
F_MIDDLE = "middlename"
F_FULL = "fullname"
F_ERRORE = "error"


def validate_juststring(input):
    t = int(input)


def validate(fullname):
    """ validation et affichage d'une string 
        selon format Prénom <Milieu> Nom 
    """
    names = fullname.split()
    len_listnames = len(names)
    d = {}
    if len_listnames == 2:
        d[F_FIRST] = names[0]
        d[F_LAST] = names[1]
    elif len_listnames == 3:
        d[F_FIRST] = names[0]
        d[F_MIDDLE] = names[1]
        d[F_LAST] = names[2]
    elif len_listnames == 1:
        d[F_LAST] = names[0]
    else:
        error = "Format : Prénom <Milieu> Nom \\n Que faire de : " + \
            " ".join(names[3:])
        d[F_ERRORE] = error
    return d


def manage_input():
    chaine = input("Nom et Prenom ?")
    d = validate(chaine)
    print(d)


if __name__ == '__main__':
    manage_input()
