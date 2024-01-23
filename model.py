from abc import ABC, abstractmethod
from datetime import datetime

import pickle


class AbstractModel(ABC):
    @abstractmethod
    def __init__(self):
        self.records = []

    @abstractmethod
    def load_records(self, filename):
        # Загрузить записи из файла
        pass

    @abstractmethod
    def save_records(self, filename):
        # Сохранить записи в файл
        pass

    @abstractmethod
    def show_all_records(self):
        # Отобразить записи
        pass

    @abstractmethod
    def show_record(self, number: int):
        pass

    @abstractmethod
    def add_record(self, record):
        pass

    @abstractmethod
    def delete_record(self, number: int):
        pass


class RecordsModel(AbstractModel):
    def __init__(self):
        self.records = []

    def load_records(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.records = pickle.load(file)
        except FileNotFoundError:
            print("Файл не найден. Загрузка не выполнена.")
        except pickle.UnpicklingError:
            print("Ошибка десериализации. Загрузка не выполнена.")

    def save_records(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.records, file)

    def show_all_records(self):
        [print("Номер записи:", i, r) for i, r in enumerate(self.records)]

    def show_record(self, number: int):
        print("Номер записи:", number, self.records[number])

    def add_record(self, record):
        self.records.append(record)

    def delete_record(self, number: int):
        if number <= len(self.records):
            self.records.pop(number)
        else:
            return 0


class AbstractRecord(ABC):
    @abstractmethod
    def __init__(self, title="", body="", time=datetime.now()):
        pass

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def set_body(self, body):
        pass

    @abstractmethod
    def set_time(self, time):
        pass


class Record(AbstractRecord):
    def __init__(self, title="", body="", time=datetime.now()):
        self.title = title
        self.body = body
        self.time = time

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_time(self):
        return self.time

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def set_time(self, time):
        self.time = time

    def __repr__(self) -> str:
        return f"Title: {self.title}\n Body: {self.body}\n Time: {self.time}\n"

    def __str__(self) -> str:
        return self.__repr__()
