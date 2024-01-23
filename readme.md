Приложение работает путем ввода комманд в консоле.
Пример:

```
Введите команду или help:
load
Введите имя файла для загрузки:
test.pkl
Введите команду или help:
show_all
Все заметки:
Номер записи: 0 Title: 1 Запись
 Body: Первая запись
 Time: 2024-01-01 00:00:00

Номер записи: 1 Title: 2 Запись
 Body: Вторая запись
 Time: 2024-01-02 00:00:00

Номер записи: 2 Title: 3 Запись
 Body: Третья запись
 Time: 2024-01-03 00:00:00

Введите команду или help:
add
Введите заголовок заметки:
123
Введите текст заметки:
123
Введите команду или help:
show_all
Все заметки:
Номер записи: 0 Title: 1 Запись
 Body: Первая запись
 Time: 2024-01-01 00:00:00

Номер записи: 1 Title: 2 Запись
 Body: Вторая запись
 Time: 2024-01-02 00:00:00

Номер записи: 2 Title: 3 Запись
 Body: Третья запись
 Time: 2024-01-03 00:00:00

Номер записи: 3 Title: 123
 Body: 123
 Time: 2024-01-23 20:21:58.314623

Введите команду или help:
save
Введите имя файла для сохранения:
test5.pkl
Введите команду или help:
show_all
Все заметки:
Номер записи: 0 Title: 1 Запись
 Body: Первая запись
 Time: 2024-01-01 00:00:00

Номер записи: 1 Title: 2 Запись
 Body: Вторая запись
 Time: 2024-01-02 00:00:00

Номер записи: 2 Title: 3 Запись
 Body: Третья запись
 Time: 2024-01-03 00:00:00

Номер записи: 3 Title: 123
 Body: 123
 Time: 2024-01-23 20:21:58.314623

Введите команду или help:
add
Введите заголовок заметки:
qwe
Введите текст заметки:
123
Введите команду или help:
filter
Фильтр по дате:
Начальная дата:  (в формате ГГГГ-ММ-ДД): 2024-01-01
Введите конечную дату:  (в формате ГГГГ-ММ-ДД): 2024-02-01
[Title: 1 Запись
 Body: Первая запись
 Time: 2024-01-01 00:00:00
, Title: 2 Запись
 Body: Вторая запись
 Time: 2024-01-02 00:00:00
, Title: 3 Запись
 Body: Третья запись
 Time: 2024-01-03 00:00:00
, Title: 123
 Body: 123
 Time: 2024-01-23 20:21:58.314623
, Title: qwe
 Body: 123
 Time: 2024-01-23 20:21:58.314623
]
Введите команду или help:
show
Заметка:
0
Номер записи: 0 Title: 1 Запись
 Body: Первая запись
 Time: 2024-01-01 00:00:00

Введите команду или help:
delete
Введите номер заметки которую нужно удалить:
1
Введите команду или help:
show_all
Все заметки:
Номер записи: 0 Title: 1 Запись
 Body: Первая запись
 Time: 2024-01-01 00:00:00

Номер записи: 1 Title: 3 Запись
 Body: Третья запись
 Time: 2024-01-03 00:00:00

Номер записи: 2 Title: 123
 Body: 123
 Time: 2024-01-23 20:21:58.314623

Номер записи: 3 Title: qwe
 Body: 123
 Time: 2024-01-23 20:21:58.314623

Введите команду или help:
show
Заметка:
1
Номер записи: 1 Title: 3 Запись
 Body: Третья запись
 Time: 2024-01-03 00:00:00

```

Все комманды:

1. add-> Добавить запись
2. delete-> Удалить запись
3. show_all-> Показать все записи
4. show-> Показать запись
5. edit-> Редактировать запись
6. sort-> Отсортировать по дате в обратном порядке
7. save-> Сохранить в файл
8. load-> Загрузить из файла
9. stop-> Завершение работы программы
10. filter-> Выборка между двух дат
11. help-> Помощь
