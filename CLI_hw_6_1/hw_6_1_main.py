from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Phone(Field):
    def __init__(self, number):
        self.value = self.validate_number(number)

    def validate_number(self, number):
        if len(number) == 10 and number.isdigit(): #Перевіряє, що номер складається рівно з 10 цифр
            return number
        raise ValueError("Phone number must contain exactly 10 digits")

    def __str__(self):
        return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number)) #Додає новий номер телефону як об'єкт Phone до списку phones

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.number == phone_number:
                self.phones.remove(phone) #Видаляє номер телефону зі списку phones, якщо він існує
                return
        raise ValueError("Phone number not found")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.number == old_number:
                phone.number = new_number #Редагує існуючий номер телефону, замінюючи старий номер на новий
                return
        raise ValueError("Old phone number not found")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.number == phone_number:
                return phone #Знаходить і повертає об'єкт Phone за номером телефону або None
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record #Додає запис до self.data. Ключ — record.name.value, значення — сам record

    def find(self, name):
        return self.data.get(name, None) #Знаходить запис за ім'ям. Повертає об'єкт Record або None, якщо запис не знайдено
    
    def delete(self, name):
        if name in self.data:
            del self.data[name] #Видаляє запис за ім'ям, якщо такий запис є у self.data

    def __str__(self):
        contacts = "\n".join(str(record) for record in self.data.values())
        return f"AddressBook:\n{contacts}" #Виводить усі записи в AddressBook у зручному форматі
    
