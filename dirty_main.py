from application.salary import *
from application.db.people import *
from datetime import date


if __name__ == '__main__':
    print(f"Текущая дата: {date.today()}")

    calculate_salary()
    get_employees()
