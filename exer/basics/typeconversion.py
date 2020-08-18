import datetime

birth_year = input("What year were you born in?")

age = datetime.datetime.now().year - int(birth_year)

print(f"You are {age-1}-{age} years old.")