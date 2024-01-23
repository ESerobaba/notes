# view.py
from datetime import datetime


class RecordView:
    command = {'add': "Добавить запись",
               'delete': "Удалить запись",
               'show_all': "Показать все записи",
               'show': "Показать запись",
               'edit': "Редактировать запись",
               'sort': "Отсортировать по дате в обратном порядке",
               'save': "Сохранить в файл",
               'load': "Загрузить из файла",
               'stop': "Завершение работы программы",
               'filter': "Выборка между двух дат",
               'help': "Помощь"}

    def show_all_records(self):
        print('Все заметки:')

    def show_record(self):
        print('Заметка:')
        return int(input())

    def add_record(self):
        print('Введите заголовок заметки:')
        title = input()
        print('Введите текст заметки:')
        text = input()
        return title, text

    def delete_record(self):
        print('Введите номер заметки которую нужно удалить:')
        return int(input())

    def change_record(self):
        print("Введите новый заголовок заметки:")
        title = input()
        print("Введите новый текст заметки:")
        text = input()
        return title, text

    def get_help(self):
        print('Список команд:')
        [print(k, v) for k, v in self.command.items()]

    def save(self):
        print("Введите имя файла для сохранения:")
        return input()

    def load(self):
        print("Введите имя файла для загрузки:")
        return input()

    def start(self):
        print("Введите команду или help:")

    def end(self):
        print("Завершение работы программы...")

    def command_error(self):
        print("Неизвестная комманда")

    def get_date_input(self, prompt):
        while True:
            try:
                date_str = input(prompt + " (в формате ГГГГ-ММ-ДД): ")
                if date_str.lower() == 'exit':
                    return None
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                return date_obj
            except ValueError:
                print(
                    "Ошибка в формате даты. Попробуйте снова или введите 'exit' для выхода.")

    def filter_data(self):
        print("Фильтр по дате:")
        start_date = self.get_date_input("Начальная дата: ")
        end_date = self.get_date_input("Введите конечную дату: ")
        return start_date, end_date
