import datetime
def get_days_from_today(date):
    try:
        date_today = datetime.datetime.today()
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        difference = date_today.toordinal() - given_date.toordinal()
        return difference
    except ValueError:
        return("Використовуйте формат 'YYYY-MM-DD'.")      


print(get_days_from_today('2025-05-23'))