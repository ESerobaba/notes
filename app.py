# app.py
from model import RecordModel
from view import RecordView
from controller import RecordController

model = RecordModel()
view = RecordView()
controller = RecordController(model, view)

if __name__ == "__main__":
    controller.run()
