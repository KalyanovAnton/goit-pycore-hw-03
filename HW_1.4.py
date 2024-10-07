from datetime import datetime, timedelta 
def get_upcoming_birthdays(users):
    date_today = datetime.today().date()
    list_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=date_today.year)
        if date_today > birthday_this_year:
            birthday_this_year = birthday_this_year.replace(year=date_today.year + 1)

        difference_days = (birthday_this_year - date_today).days

        if 0 <= difference_days <= 7:
            if birthday_this_year.weekday() == 5:
               congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                  congratulation_date = birthday_this_year + timedelta(days=1)
            else :
                  congratulation_date = birthday_this_year

            list_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return list_birthdays
users_birthday = [
    {"name": "John Doe", "birthday": "1985.10.12"},
    {"name": "Jane Smith", "birthday": "1990.10.07"}
]
upcoming_birthdays = get_upcoming_birthdays(users_birthday)
print("Список привітань на цьому тижні:", upcoming_birthdays)
