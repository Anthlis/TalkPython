import datetime


def print_header():
    print('-----------------------------------')
    print('        PPL(A) CURRENCY APP')
    print('-----------------------------------')
    print('     Today's Date: )
    print()


def get_currency_from_user():
    print('When did you last fly on Type? ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    currency = datetime.datetime(year, month, day)
    return currency


def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_currency_information(days):
    if days < 90:
        print("Your currency expires in {} days, you'd best plan another flight soon!".format(-days))
    elif days > 90:
        print('Your currency on this Type expired {} days ago'.format(days))
    else:
        print('Did you have a good flight today?')


def main():
    print_header()
    bday = get_currency_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_currency_information(number_of_days)


main()