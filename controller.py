# controller.py
from model import RecordsModel, Record
from view import RecordView


class RecordController:
    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view

    def load_records(self, filename):
        # Обработать запрос на загрузку записей
        self.model.load_records(filename)

    def save_records(self, filename):
        # Обработать запрос на сохранение записей
        self.model.save_records(filename)

    def show_all_records(self):
        self.view.show_all_records(self.model.show_all_records())

    def show_record(self, number):
        self.view.show_record(self.model.show_record(number))

    def add_record(self):
        title, text = self.view.add_record()
        self.model.add_record_text(title, text)

    def delete_record(self, number):
        self.model.delete_record(number)

    def change_record(self, number):
        title, text = self.view.change_record()
        self.model.change_record(number, title, text)

    def sort_by_date(self):
        self.model.sort_by_date()

    def run(self):
        # Основной цикл приложения
        pass
