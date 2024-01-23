# view.py
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
