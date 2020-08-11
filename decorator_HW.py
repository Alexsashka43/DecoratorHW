from _datetime import datetime
import os

def decorator_log(old_function):
    def new_function(*args, **kwargs):
        smth_return = old_function(*args, **kwargs)

        location = os.path.abspath('decorator_log.txt')

        info = dict()
        info['record'] = datetime.now()
        info['args'] = args
        info['kwargs'] = kwargs
        info['return'] = smth_return
        info['name'] = old_function.__name__
        info['location_log'] = location

        with open('decorator_log.txt', 'a', encoding = 'utf-8') as file:
            for keys,values in info.items():
                file.write(f'{keys} : {values}\n')

        return smth_return

    return new_function

@decorator_log

class Contact:
    def __init__(self, name, last_name, phone_number, favorite_contact=False, **kwargs):
        self.dict_of_contact = {}
        self.dict_of_contact['Имя'] = name
        self.dict_of_contact['Фамилия'] = last_name
        self.dict_of_contact['Телефон'] = phone_number
        self.dict_of_contact['Избранный контакт'] = favorite_contact
        self.dict_of_contact['дополнительная информация'] = kwargs

jhon = Contact('Jhon', 'Smith', '+71234567809', 'нет', telegram='@jhony', email='jhony@smith.com')


def get_name(self):
    return self.dict_of_contact['Имя']

get_name(jhon)