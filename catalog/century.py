import datetime


def datetime_input(date_time):
    year = str(date_time.year)
    month = (date_time.month)
    day = (date_time.day)
    century(year, month, day)


def century(year, month, day):

    # year = input('date année?')
    # month = input('date mois?')
    # day = input('date jours?')
    # date = datetime.date(int(year), int(month), int(day))
    # print(date)
    # if not date:
    # print("Bye")

    # else:
    if int(year) < 101:
        if int(year) < 1:
            return '0'
        else:
            return 'Premier'
    if len(year) < 4:
        unite_siecle = year[:1]
        test_siecle = int(unite_siecle)*100
        print('test_siecle ', test_siecle)
        if int(test_siecle) == int(year):
            return {unite_siecle}
        else:
            siecle = int(unite_siecle)
            siecle += 1
            return {siecle}
    if len(year) < 5:
        unite_siecle = year[:2]
        test_siecle = int(unite_siecle)*100
        print('test_siecle ', test_siecle)

        if int(test_siecle) == int(year):
            return {unite_siecle}
        else:
            siecle = int(unite_siecle)
            siecle += 1
            return {siecle}
    return 'pas de date ?'


def validate_year(date):
    ''' fonction validation de l'année '''
    y = date.year


# if __name__ == '__main__':
#     datetime_input(datetime.date(1953, 5, 1))
#     cent = century()
#     print(cent, ' siècle')
