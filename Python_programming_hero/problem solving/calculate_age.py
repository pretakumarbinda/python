from datetime import datetime
import time

def calculate_age(born):
    today = datetime.today()
    days = (today - born).days  
    age = days // 365
    return age

def get_user_birthday():
    date_str = input("Enter your birthday in DD/MM/YYYY: ")
    try:
        birthday = datetime.strptime(date_str, "%d/%m/%Y")
    except TypeError:
        birthday = datetime.datetime(*(time.strptime(date_str, "%d/%m/%Y")[0:6]))
    return birthday

birthday = get_user_birthday()
age = calculate_age(birthday)
print('Your age: ', age)