from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QSplashScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import json
import sys
import time


class SplashScreen(QSplashScreen):
	def __init__(self):
		super().__init__()
		self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
		pixmap = QPixmap("wingslut.jpg")
		self.setPixmap(pixmap)


class MyWindow(QDialog):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setWindowTitle("WingSlut")
		self.setGeometry(0, 0, 600, 400)
		self.UiComponents()
		self.show()

	def UiComponents(self):
		layout = QtWidgets.QVBoxLayout()
		self.input1 = QtWidgets.QLineEdit(self)
		self.input1.setFixedWidth(200)
		self.input1.move(870,350)
		#layout.addWidget(self.input1, alignment= Qt.AlignmentFlag.AlignCenter)

		self.input2 = QtWidgets.QLineEdit(self)
		self.input2.setFixedWidth(200)
		self.input2.move(870,400)
		self.input2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

		self.login = QtWidgets.QPushButton(self)
		self.login.setText("submit")
		self.login.move(1200, 500)
		self.login.clicked.connect(self.get)

		self.label1 = QtWidgets.QLabel("    id", self)
		self.label1.setGeometry(800, 350, 120, 40)
		self.label2 = QtWidgets.QLabel("password", self)
		self.label2.setGeometry(800, 400, 120, 40)
		self.label3 = QtWidgets.QLabel("", self)
		self.label3.setGeometry(800, 450, 120, 40)


		self.setLayout(layout)




		self.showMaximized()

	def get(self):
		admin_id = self.input1.text()
		with open("admin.json", "r") as x:
			admin_data = json.load(x)
		if admin_id == admin_data["id"]:
			admin_pass = self.input2.text()
			if admin_pass == admin_data["password"]:
				self.label3.setText("succesfull login")
				time.sleep(2)
				widget.setCurrentIndex(widget.currentIndex()+1)
			else:
				self.label3.setText("wrong password")
		else:
			self.label3.setText("wrong id")


class MyOtherWindow(QDialog):
	def __init__(self):
		super(MyOtherWindow, self).__init__()
		self.setWindowTitle("WingSlut")
		self.setGeometry(0, 0, 600, 400)
		self.initUI()
		self.show()

	def initUI(self):
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("A")
		self.b1.move(80, 300)
		#self.b1.clicked.connect(self.c1)

		self.b2 = QtWidgets.QPushButton(self)
		self.b2.setText("B")
		self.b2.move(160, 300)
		#self.b2.clicked.connect(self.c2)
		#self.setGeometry(0, 0, 300, 800)

		self.b3 = QtWidgets.QPushButton(self)
		self.b3.setText("C")
		self.b3.move(240, 300)
		#self.b3.clicked.connect(self.c3)

		self.b4 = QtWidgets.QPushButton(self)
		self.b4.setText("D")
		self.b4.move(320, 300)
		#self.b4.clicked.connect(self.c4)

		self.showMaximized()





app = QApplication(sys.argv)
splash = SplashScreen()
splash.show()
time.sleep(2)
widget = QtWidgets.QStackedWidget()
loginwin = MyWindow()
menu = MyOtherWindow()
widget.addWidget(loginwin)
widget.addWidget(menu)
widget.showMaximized()
sys.exit(app.exec())

