from abc import ABC, abstractmethod
import datetime


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


class RecordsModel(AbstractModel):
    def __init__(self):
        self.records = []

    def load_records(self, filename):
        # Загрузить записи из файла
        pass

    def save_records(self, filename):
        # Сохранить записи в файл
        pass


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
