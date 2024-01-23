# app.py
from model import RecordsModel, Record
from view import RecordView
from controller import RecordController

model = RecordsModel()
r1 = Record("1 Запись", 'Первая запись')
r2 = Record("2 Запись", 'Вторая запись')
r3 = Record("3 Запись", 'Третья запись')
model.add_record(r1)
model.add_record(r2)
model.add_record(r3)
model.show_all_records()
model.show_record(0)
model.delete_record(0)
print('----------------------------------------------------------------')
model.show_all_records()
model.save_records("records_data.pkl")
print('----------------------------------------------------------------')
new_model = RecordsModel()
new_model.load_records("records_data.pkl")
new_model.show_all_records()
# view = RecordView()
# controller = RecordController(model, view)

# if __name__ == "__main__":
#     controller.run()
