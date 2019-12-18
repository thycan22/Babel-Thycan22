import datetime


# traitement de l'année de naissance


''' fonction controleur '''


def controller_input():
    while True:
        ye = input(' Annee ? :')

        if not ye:
            print("Bye")
            break
        else:
            y = validate_year(ye)
            dt = datetime.date.today()
            print('année ', y)
            print(datetime.date(y, 1, 1))
            print(dt)
            date_obj = datetime.date(y, 6, 14)
            print(date_obj)
            age = dt - date_obj
            display_line_year(y, age.days)


def controller_file():
    pass


''' fonction validation de l'année et calcul des ages et jours.'''


def validate_year(year):
    y = year
    dt = datetime.date.today()
    todyear = dt.year-2000
    if isinstance(year, str):
        try:
            y = int(year)
        except ValueError as e:
            print(str(e))
            return None

    print(y)
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
