import datetime


# traitement de l'année


''' fonction controleur '''


def controller_input():
    while True:
        ye = input(' Annee ? :')
        year = int(ye)
        if not year:
            break
        else:
            validate_year(year)


def controller_file():
    pass


''' fonction validation de l'année et calcul des ages et jours.'''


def validate_year(year):
    dt = datetime.datetime.now()
    todyear = dt.year-2000
    y = int(year)
    print(y)
    if y <= todyear:
        y += 2000
    elif (y > todyear and y < 99):
        y += 1900
    print('année ', y)
    age = dt-datetime.date(y)
    days = age*365
    display_line_year(y, age)


def display_line_year(display, age):
    d = "Vous êtes né(e) le " + display + "il y a :" + age
    print(d)


if __name__ == '__main__':
    controller_input()
