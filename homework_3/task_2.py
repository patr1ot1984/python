def user_data(name, surname, year, address, email, phone):
    print(f"{name}, {surname}, {year}, {address}, {email}, {phone}")
name = input(" имя : ")
surname = input(" фамилия : ")
year = input(" год рождения : ")
address = input(" город проживания : ")
email = input(" email : ")
phone = input(" номер телефона : ")
user_data(name=name, surname=surname, year=year, address=address, email=email, phone=phone)
