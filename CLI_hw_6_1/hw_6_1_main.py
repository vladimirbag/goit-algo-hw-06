from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __str__(self):
        return self.value

class Phone(Field):
    def __init__(self, number):
        self.value = self.validate_number(number)

    def validate_number(self, number):
        if len(number) == 10 and number.isdigit():  # Перевіряє, що номер складається рівно з 10 цифр
            return number
        raise ValueError("Phone number must contain exactly 10 digits")

    def __str__(self):
        return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))  # Додає новий номер телефону як об'єкт Phone до списку phones

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:  # Використовуємо phone.value замість phone.number
                self.phones.remove(phone)
                return
        raise ValueError("Phone number not found")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:  # Використовуємо phone.value замість phone.number
                phone.value = Phone(new_number).value
                return
        raise ValueError("Old phone number not found")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:  # Використовуємо phone.value замість phone.number
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  # Використовуємо record.name.value як ключ

    def find(self, name):
        return self.data.get(name, None)  # Знаходить запис за ім'ям. Повертає об'єкт Record або None, якщо запис не знайдено

    def delete(self, name):
        if name in self.data:
            del self.data[name]  # Видаляє запис за ім'ям, якщо такий запис є у self.data

    def __str__(self):
        contacts = "\n".join(str(record) for record in self.data.values())
        return f"AddressBook:\n{contacts}"  # Виводить усі записи в AddressBook у зручному форматі

        """ПЕРЕВіРКА"""
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
