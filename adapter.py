import csv
import json

from generator import *

person_generator = PersonGenerator()
address_generator = AddressGenerator()

columns_person = {
    'Имя': person_generator.get_name,
    'Фамилия': person_generator.get_surname,
    'Отчество': person_generator.get_patronymic,
    'ФИО': person_generator.get_FIO,
    'Имя, фамилия': person_generator.get_fullname,
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

def get_generated_info(columns: list, amount: int, gender = None) -> list:
    values = [] # like [(),(),()]
    for i in range(amount):
        value = []
        for column in columns:
            if column in columns_person.keys():
                """ 
                первым трем полям нужно передавать значение пола, если оно есть.
                так делать не очень хорошо, но пока не хочется городить огороды.
                """
                if gender != 'Any' and 'gender' in columns_person[column].__code__.co_varnames:
                    value.append(columns_person[column](gender))
                else:
                    value.append(columns_person[column]())
            elif column in columns_address.keys():
                value.append(columns_address[column]())
        values.append(value)
    return values
    

def save_json(values: list):
    with open('download/values.json', 'w') as jsonfile:
        json.dump(values, jsonfile, ensure_ascii=False, sort_keys=True, indent=4)
    return 'values.json' # return name of file for download.


def save_csv(values: list):
    with open('download/values.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for value in values:
            writer.writerow(value)
    return 'values.csv' # return name of file for download.

if __name__ == '__main__':
    values = get_generated_info(['Фамилия','Имя','Номер паспорта'], 10)
    print(save_json(values))