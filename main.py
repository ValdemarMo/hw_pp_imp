from aplication.salary import calculate_salary as cs
from aplication.db.people import get_employees as ge
from datetime import datetime, date, time

if __name__ == '__main__':
    x1 = ge()
    x2 = cs()
    t = datetime.today()
    print(t.strftime("%A, %d. %B %Y %I:%M%p"))