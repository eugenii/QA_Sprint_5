# Вспомогательные функции для тестирования.
from random import sample, randint


# Генерация пары - логин, пароль.
def createAuthPair() -> tuple:
    set_for_pair1 = list('abcdefghijklmnpqrstuvwxxyz')
    set_for_pair2 = list('123456789')
    login = ''.join(sample(set_for_pair1, randint(2, 6))) + '@' + ''.join(sample(set_for_pair1, randint(2, 5)))
    password = ''.join(sample(set_for_pair2, randint(6, 8)))
    return login, password