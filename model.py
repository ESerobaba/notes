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
        return [f"Номер записи: {i} {r}" for i, r in enumerate(self.records)]

    def show_inp_records(self, records):
        return [f"{r}" for r in self.records]

    def show_record(self, number: int):
        if number <= len(self.records):
            return f"Номер записи: {number} {self.records[number]}"
        else:
            print("Нет записи с таким номером")

    def add_record(self, record):
        self.records.append(record)

    def add_record_text(self, title, text):
        self.records.append(Record(title, text))

    def delete_record(self, number: int):
        if number <= len(self.records):
            self.records.pop(number)
        else:
            print("Нет записи с таким номером")

    def change_record(self, number, title, text):
        if title != self.records[number].title:
            self.records[number].title = title
        if text != self.records[number].body:
            self.records[number].body = text

    def sort_by_date(self):
        self.records.sort(key=lambda x: x.time, reverse=True)

    def filter_records_by_date(self, start_date=None, end_date=None):
        filtered_records = []
        for record in self.records:
            if start_date is not None and record.time < start_date:
                continue
            if end_date is not None and record.time > end_date:
                continue
            filtered_records.append(record)
        return filtered_records


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
