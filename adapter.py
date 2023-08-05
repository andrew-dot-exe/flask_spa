from generator import *


person_generator = PersonGenerator()
address_generator = AddressGenerator()

columns_person = {
    'Имя': person_generator.get_name,
    'Фамилия': person_generator.get_surname,
    #TODO:'Отчество': person_generator.get_name,
    #TODO: FIO
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

def get_generated_info(columns: list, amount: int) -> list:
    values = [] # like [(),(),()]
    for i in range(amount):
        value = []
        for column in columns:
            if column in columns_person.keys():
                value.append(columns_person[column]())
            elif column in columns_address.keys():
                value.append(columns_address[column]())
        values.append(value)
    return values
    

if __name__ == '__main__':
    print(get_generated_info(['Фамилия','Имя','Номер паспорта'], 10))