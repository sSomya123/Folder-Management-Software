import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from Create_folder import CreateWindow
from Delete_folder import DeleteWindow
from Move_folder import MoveWindow
from Copy_folder import CopyWindow

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.Button1 = QPushButton("Create Folder", self)
        self.Button2 = QPushButton("Delete Folder", self)
        self.Button3 = QPushButton("Move Folder", self)
        self.Button4 = QPushButton("Copy Folder", self)

        self.Button1.clicked.connect(self.open_create_window)
        self.Button2.clicked.connect(self.open_delete_window)
        self.Button3.clicked.connect(self.open_move_window)
        self.Button4.clicked.connect(self.open_copy_window)

        layout = QVBoxLayout()
        layout.addWidget(self.Button1)
        layout.addWidget(self.Button2)
        layout.addWidget(self.Button3)
        layout.addWidget(self.Button4)

        self.setLayout(layout)
        self.setWindowTitle("Folder Management")
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def open_create_window(self):
        self.create_window = CreateWindow()
        self.create_window.exec_()

    def open_delete_window(self):
        self.delete_window = DeleteWindow()
        self.delete_window.exec_()

    def open_move_window(self):
        self.move_window = MoveWindow()
        self.move_window.exec_()

    def open_copy_window(self):
        self.copy_window = CopyWindow()
        self.copy_window.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
