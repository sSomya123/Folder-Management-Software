import sys
from Methods import delete_folder
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class DeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.Label1=QLabel("Folder Path :",self)
        self.input1_box=QLineEdit(self)
        
        self.Label2=QLabel("Result :",self)
        self.result_label=QLabel(self)
        
        self.Button=QPushButton("Delete",self)
        self.Button.clicked.connect(self.button_fun)

        Layout = QVBoxLayout()
        Layout.addWidget(self.Label1)
        Layout.addWidget(self.input1_box)
       
        Layout.addWidget(self.Label2)
        Layout.addWidget(self.result_label)
        
        Layout.addWidget(self.Button)
        
        self.setLayout(Layout)
        self.setWindowTitle("Simple Delete Folder GUI")
        self.setGeometry(100, 100, 500, 400)
        self.show()

    def button_fun(self):
        folder_path = self.input1_box.text()  
        if folder_path:
            result = delete_folder(folder_path)
            self.result_label.setText(result)
        else:
            self.result_label.setText("Please provide both Folder Path and Folder Name.")
        

app = QApplication(sys.argv)
window = DeleteWindow()
sys.exit(app.exec_())

