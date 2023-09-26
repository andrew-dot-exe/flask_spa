import json
from datetime import date as dt
from random import randint, choice
from os.path import join


PERSONS = join('generator', 'data', 'person.json')
ADDRESS = join('generator', 'data', 'address.json')


class Genders:
    MALE = "male"
    FEMALE = "female"
    ANY = "any"


class PersonGenerator:
    genders = ["male", "female"]

    def __init__(self):
        f = open(PERSONS, 'r', encoding='utf-8')
        json_t = ''.join(f.readlines())
        json_l = json.loads(json_t)
        f.close()
        self.names = json_l["names"]
        self.surnames = json_l["surnames"]
        self.patronymcs = json_l["patronymic"]
        self.selected_gender = None
        self.age = None

    def get_names(self, gender=None) -> list:
        """
        Метод, который возвращает все имена,
        если не указан пол. Если указан пол,
        то возвращает список имен этого пола
        """
        if gender is None:
            return self.names
        return self.names[gender]

    def decide_gender(self, reroll=True) -> str:
        """
        Этот метод выбирает пол для дальнейшей генерации.
        Если reroll=True, то этот метод возвращает новый пол,
        но не перезаписывает его.
        """
        if reroll:
            return choice(self.genders)
        if self.selected_gender is None:
            self.selected_gender = choice(self.genders)
        return self.selected_gender

    def get_name(self, gender=None) -> str:
        """
        Этот метод возврашает имя в соответствии с полом.
        """
        if gender is None:
            gender = self.decide_gender()
        return choice(self.names[gender])

    def get_surname(self, gender=None) -> str:
        """
        Этот метод возвращает фамилию с соответсвии с полом.
        """
        if gender is None:
            gender = self.decide_gender()
        return choice(self.surnames[gender])

    def get_patronymic(self, gender=None) -> str:
        if gender is None:
            gender = self.decide_gender()
        return choice(self.patronymcs[gender])

    def get_fullname(self, gender=None) -> str:
        """
        Этот метод возвращает сразу и имя, и фамилию.
        """
        if gender is None:
            gender = self.decide_gender()
        if gender == Genders.ANY:
            gender = self.decide_gender(reroll=True)
        return ' '.join([self.get_name(gender), self.get_surname(gender)])

    def get_FIO(self, gender=None) -> str:
        """
        Этот метод возвращает фамилию, имя и отчество в принятом
        порядке (Фамилия Имя Отчество).
        """
        if gender is None:
            gender = self.decide_gender()
        if gender == Genders.ANY:
            gender = self.decide_gender(reroll=True)
        return ' '.join([self.get_surname(gender), self.get_name(
            gender), self.get_patronymic(gender)])

    def get_age(self) -> int:
        """
        Этот метод возвращает возраст.
        """
        self.age = randint(18, 99)
        return self.age

    def get_phone_number(self) -> str:
        """
        Возвращает телефонный номер с в международном формате.
        """
        number = '+79' + ''.join([str(randint(0, 9)) for i in range(8)])
        return number

    def get_passport_number(self):
        """
        Возвращает серию и номер паспорта в формате #### ######
        """
        passport = ''.join([str(randint(0, 9)) for i in range(
            3)]) + ' ' + ''.join([str(randint(0, 9)) for i in range(6)])
        return passport

    def get_DOB(self):
        """
        Генерирует дату рождения человека с учетом возраста и текущего года.
        """
        if self.age is None:
            return None
        year = dt.today().year - self.age
        month = randint(1, 12)
        if month > dt.today().month:
            year -= 1
        if month == 2:
            date = randint(1, 28)
        else:
            date = randint(1, 30)
        date_lst = [str(date), str(month), str(year)]
        return '.'.join(date_lst)


class AddressGenerator:
    def __init__(self):
        with open(ADDRESS) as f:
            json_t = ''.join(f.readlines())
            text = json.loads(json_t)
            self.cities = text['city']
            self.region = text['regions']
            self.streets = text['street']

    def get_city(self) -> str:
        """
        Возвращает случайно выбраннный город
        """
        return choice(self.cities)

    def get_street(self) -> str:
        """
        Возвращает случайно выбранную улицу
        """
        return choice(self.streets)

    def get_street_number(self) -> str:
        """
        Возвращает случайно выбранный номер улицы.
        Почему 220 - не знаю.
        """
        return str(randint(1, 220))

    def get_postal_code(self) -> str:
        """
        Возвращает случайный индекс (6 цифр) в виде строки
        """
        postal_code = [str(randint(0, 9)) for i in range(6)]
        return ''.join(postal_code)

    def get_full_address(self) -> str:
        city = choice(self.cities)
        street = choice(self.streets)
        return f"г. {city}, ул. {street}, {str(self.get_street_number())} "


if __name__ == '__main__':
    pg = PersonGenerator()
    print(pg.get_patronymic())
