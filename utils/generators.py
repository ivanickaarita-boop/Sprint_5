import random
import string


def generate_email():
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f'ivan_ivanov_44_{random_digits}@yandex.ru'


def generate_password(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))