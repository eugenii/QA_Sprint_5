# Вспомогательные функции для тестирования.
from random import sample, randint


# Генерация пары - логин, пароль.
# ключи: 
# valid_email - True/False - верный/неверный
# valid_password - True/False - верный/неверный (короткий пароль)
def createAuthPair(valid_email=True, valid_password=True) -> tuple:
    set_for_pair1 = list('abcdefghijklmnpqrstuvwxxyz')
    set_for_pair2 = list('123456789')
    login = ''.join(sample(set_for_pair1, randint(2, 6))) + '@' + ''.join(sample(set_for_pair1, randint(2, 5)))
    password = ''.join(sample(set_for_pair2, randint(6, 8)))
    if not valid_email:
        login.replace('@', '')
    if not valid_password:
        password = password[:5]
    return login, password