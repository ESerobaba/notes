# view.py
class RecordView:
    def show_all_records(self, records):
        print('Все заметки:')
        [print(rec) for rec in records]

    def show_record(self, rec):
        print('Заметка:')
        print(rec)

    def add_record(self):
        print('Введите заголовок заметки:')
        title = input()
        print('Введите текст заметки:')
        text = input()
        return title, text

    def remove_record(self):
        print('Введите номер заметки которую нужно удалить:')

    def change_record(self):
        print("Введите новый заголовок заметки:")
        title = input()
        print("Введите новый текст заметки:")
        text = input()
        return title, text

    def get_help(self):
        command = {'add': "Добавить запись",
                   'delete': "Удалить запись",
                   'edit': "Редактировать запись",
                   'sort': "Отсортировать по дате в обратном порядке",
                   'save': "Сохранить в файл",
                   'load': "Загрузить из файла"}
        print('Список команд:')
