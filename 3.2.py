def user_info(name, year, surname, mobile, city, email):
    return print(f"""Уважаемый, {name} {surname}! 
Как только вы родились в {year}-м году, мы успешно за вами следим.
Сейчас вы проживаете в городе {city}, и у нас к вам предложение.
Подробности на почте {email}, скоро мы позвоним вам на номер {mobile} и озвучим детали. 
С заботой о вас - ФСБ""")

user_info(name='Коля', surname='Соколов', email='sokolov@privivki.net', mobile=89519999999, year=2000, city='Москва')