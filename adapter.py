from generator import *


person_generator = PersonGenerator()
address_generator = AddressGenerator()

columns_person = {
    'Имя': person_generator.get_name,
    'Фамилия': person_generator.get_surname,
    #TODO:'Отчество': person_generator.get_name,
    #TODO: FIO
    'Возраст': person_generator.get_age,
    'Номер телефона': person_generator.get_phone_number,
    'Номер паспорта': person_generator.get_passport_number,
    'Дата рождения': person_generator.get_DOB
}

columns_address = {
    'Город': address_generator.get_city,
    'Улица': address_generator.get_street,
    'Номер улицы': address_generator.get_street_number,
    'Индекс': address_generator.get_postal_code
}

if __name__ == '__main__':
    l = list(columns_person.keys())
    print(l[0])