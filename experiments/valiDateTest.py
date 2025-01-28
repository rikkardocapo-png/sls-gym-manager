from datetime import datetime


def valiDate(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

print(valiDate("nhefwf"))