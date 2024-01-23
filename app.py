# app.py
from model import RecordsModel, Record
from view import RecordView
from controller import RecordController

model = RecordsModel()
# r1 = Record("1 Запись", 'Первая запись', datetime(2024, 1, 1))
# r2 = Record("2 Запись", 'Вторая запись', datetime(2024, 1, 2))
# r3 = Record("3 Запись", 'Третья запись', datetime(2024, 1, 3))
# r4 = Record("4 Запись", 'Четвертая запись', datetime(2024, 1, 4))
# model.add_record(r1)
# model.add_record(r2)
# model.add_record(r3)
view = RecordView()
controller = RecordController(model, view)
controller.run()
# controller.show_all_records()
# print('----------------------------------------------------------------')
# controller.sort_by_date()
# controller.show_all_records()
# print('----------------------------------------------------------------')
# controller.help()
# controller.save_records()

# print(model.show_all_records())
# print(model.show_record(0))
# model.delete_record(0)
# print('----------------------------------------------------------------')
# print(model.show_all_records())
# model.save_records("records_data.pkl")
# print('----------------------------------------------------------------')
# new_model = RecordsModel()
# new_model.load_records("records_data.pkl")
# print(new_model.show_all_records())
# view = RecordView()
# controller = RecordController(model, view)

# if __name__ == "__main__":
#     controller.run()
