import datetime


# traitement de l'année de naissance


def controller_input():
    ''' fonction controleur : insertion de l'utilisateur '''
    while True:
        ye = input(' Annee ? :')

        if not ye:
            print("Bye")
            break
        else:
            ''' fonction qui valide la date'''
            y = validate_year(ye)
            '''calcul de l'age et du nbre de jours '''
            dt = datetime.date.today()
            # print('année ', y)
            # print(datetime.date(y, 1, 1))
            # print(dt)
            if isinstance(y, int):
                date_obj = datetime.date(y, 6, 14)
                # print(date_obj)
                age = dt - date_obj
            '''appel de l'affichage '''
            display_line_year(y, age.days)


def controller_file():
    pass


def validate_year(year):
    ''' fonction validation de l'année et calcul des ages et jours.'''
    y = year
    dt = datetime.date.today()
    todyear = dt.year-2000
    if isinstance(year, str):
        try:
            y = int(year)
        except ValueError as e:
            # print(str(e))
            return None
    if datetime.date(y, 1, 1) > dt:
        return 'trop grand !'
    if y <= todyear:
        y += 2000
    elif (y > todyear and y < 99):
        y += 1900
    return y


def display_line_year(display, age):
    d = "Vous êtes né(e) le 14/06/" + str(display) + \
        "  il y a :" + str(age) + " jours."
    print(d)


if __name__ == '__main__':
    controller_input()
