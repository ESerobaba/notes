# controller.py
from model import RecordsModel, Record
from view import RecordView


class RecordController:
    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view

    def load_records(self, filename=None):
        if filename is None:
            filename = self.view.load()
        # Обработать запрос на загрузку записей
        self.model.load_records(filename)

    def save_records(self, filename=None):
        if filename is None:
            filename = self.view.save()
        # Обработать запрос на сохранение записей
        self.model.save_records(filename)

    def show_all_records(self):
        self.view.show_all_records()
        [print(rec) for rec in self.model.show_all_records()]

    def show_record(self):
        print(self.model.show_record(self.view.show_record()))

    def add_record(self):
        title, text = self.view.add_record()
        self.model.add_record_text(title, text)

    def delete_record(self):
        self.model.delete_record(self.view.delete_record())

    def change_record(self, number):
        title, text = self.view.change_record()
        self.model.change_record(number, title, text)

    def sort_by_date(self):
        self.model.sort_by_date()

    def help(self):
        self.view.get_help()

    def stop(self):
        self.view.end()

    def filter_data(self):
        start_date, end_date = self.view.filter_data()
        if start_date is not None and end_date is not None:
            filtered_records = self.model.filter_records_by_date(
                start_date, end_date)
            print(filtered_records)

    def run(self):
        while True:
            self.view.start()
            # self.view.get_help()
            command = input()
            if command not in self.view.command:
                self.view.command_error()
                continue
            else:
                if command == 'add':
                    self.add_record()
                elif command == 'delete':
                    self.delete_record()
                elif command == 'edit':
                    self.change_record()
                elif command == 'sort':
                    self.sort_by_date()
                elif command == 'save':
                    self.save_records()
                elif command == 'load':
                    self.load_records()
                elif command == 'help':
                    self.help()
                elif command == 'show_all':
                    self.show_all_records()
                elif command == 'show':
                    self.show_record()
                elif command == 'filter':
                    self.filter_data()
                elif command == 'stop':
                    break
