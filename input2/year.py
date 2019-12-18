import datetime


# traitement de l'année


Y_YEAR = 0
display = 'nn'


def controller_input():
    while True:
        ye = input(' Annee ? :')
        year = int(ye)
        if year == '':
            display = 'veuillez renseigner une date !'
        elif True:
            display = str(controller_year(year))
        else:
            display = 'Le format demandé YYY ou YY'

    return display


def controller_file():
    pass


def controller_year(year):
    dt = datetime.datetime.now()
    todyear = dt.year-2000
    y = int(year)
    print(y)

    if y <= todyear:
        Y_YEAR = 2000+y
    elif (y > todyear and y < 99):
        Y_YEAR = 1900+y
    else:
        Y_YEAR = y
    print('année '+Y_YEAR)
    return Y_YEAR


def display_line_year():
    pass


a = controller_year('45')
print(a)
input2 = controller_input()
print(input2)

if __name__ == '__main__':
    controller_input()
