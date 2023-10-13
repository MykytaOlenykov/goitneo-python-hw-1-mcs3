from datetime import datetime
from collections import defaultdict

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1955, 10, 28)},
    {"name": "Kim Kardashian", "birthday": datetime(1955, 5, 4)},
    {"name": "Jan Koum", "birthday": datetime(1955, 10, 15)},
    {"name": "John Doe", "birthday": datetime(1980, 3, 12)},
    {"name": "Jane Smith", "birthday": datetime(1992, 8, 20)},
    {"name": "Alice Johnson", "birthday": datetime(1977, 10, 17)},
    {"name": "Jane Smith", "birthday": datetime(1992, 10, 17)},
    {"name": "Bob Williams", "birthday": datetime(1985, 10, 13)},
    {"name": "Eve Brown", "birthday": datetime(2000, 9, 17)},
    {"name": "Michael Lee", "birthday": datetime(1964, 10, 12)},
    {"name": "Sophia Rodriguez", "birthday": datetime(1979, 10, 14)},
    {"name": "David Clark", "birthday": datetime(1998, 1, 2)},
    {"name": "Olivia Taylor", "birthday": datetime(1991, 4, 23)},
    {"name": "William Johnson", "birthday": datetime(1972, 12, 10)},
    {"name": "Emily White", "birthday": datetime(1987, 10, 3)},
    {"name": "Daniel Anderson", "birthday": datetime(2005, 6, 15)},
    {"name": "Sophie Harris", "birthday": datetime(1989, 10, 14)},
]

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


def get_birthdays_per_week(users: list):
    grouped_users = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            next_year = birthday_this_year.year + 1
            birthday_this_year = birthday_this_year.replace(year=next_year)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = birthday_this_year.weekday()
            if weekday == 5 or weekday == 6:
                grouped_users[WEEKDAYS[0]].append(name)
                continue

            grouped_users[birthday_this_year.strftime("%A")].append(name)

    for weekday in WEEKDAYS:
        users_list = grouped_users[weekday]
        if users_list:
            message = f"{weekday}: {', '.join(users_list)}"
            print(message)


get_birthdays_per_week(users)
