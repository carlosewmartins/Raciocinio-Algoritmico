import datetime as dt

get_year = lambda: dt.date.today().year

age = lambda ano_nascimento: get_year() - ano_nascimento

idade_user = int(input("Em que ano voce nasceu? "))

print(f"Sua idade e: {age(idade_user)} anos")