import datetime


def print_header():
    print('-----------------------------------')
    print('           Birthday App            ')
    print('-----------------------------------')
    print()


def get_birthday_from_user():
    print('When were you born? ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Dat [DD]: '))

    bday = datetime.date(year, month, day)
    return bday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    delta_dates = this_year - target_date
    return delta_dates.days


def print_user_information(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days!'.format(-days))
    else:
        print('Happy birthday!!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_user_information(number_of_days)


main()