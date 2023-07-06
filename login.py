# Admin Employee
#       User name =  jahannia
#       password =   jahannia

# User Liberary:
#       username = Yunes
#       password = 87356

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from User import Ui_OtherWindow
from employer import Ui_employerWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 379)
        MainWindow.setMinimumSize(QtCore.QSize(524, 379))
        MainWindow.setMaximumSize(QtCore.QSize(524, 379))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("p.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("#MainWindow{\n"
                                 "background-image:url(\"backgroung.jpg\");\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QLabel{\n"
                                 "color: white;\n"
                                 "font: 14pt \"OCR-B 10 BT\";\n"
                                 "\n"
                                 "}\n"
                                 "QLineEdit{\n"
                                 "width:300px;\n"
                                 "height:40px;\n"
                                 "background-color:transparent;\n"
                                 "border: 2px solid #999;\n"
                                 "border-radius: 10px;\n"
                                 "padding-left: 10px;\n"
                                 "color: white;\n"
                                 "font: 12pt \"OCR-B 10 BT\";\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "font: 12pt \"OCR-B 10 BT\";\n"

                                 "color: white;\n"
                                 "width:300px;\n"
                                 "height:40px;\n"
                                 "background-color:transparent;\n"
                                 "border: 2px solid #999;\n"
                                 "border-radius: 10px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "width:300px;\n"
                                 "height:40px;\n"
                                 "background-color:transparent;\n"
                                 "border: 2px solid #999;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: rgba(0, 0, 0, 0.8);\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 50, 333, 277))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMaximumSize(QtCore.QSize(40, 40))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./p.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("OCR-B 10 BT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit_UserName = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_UserName.setObjectName("lineEdit_UserName")
        self.verticalLayout.addWidget(self.lineEdit_UserName)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMaximumSize(QtCore.QSize(40, 40))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 0)")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./t.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("OCR-B 10 BT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.verticalLayout.addWidget(self.lineEdit_Password)
        self.pushButton_Login = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Nova")
        font.setPointSize(10)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.verticalLayout.addWidget(self.pushButton_Login)
        self.error_label = QtWidgets.QLabel(self.widget)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit_UserName.setFocus()
        self.pushButton_Login.clicked.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.lineEdit_UserName.setToolTip(_translate("MainWindow", "Username"))
        self.lineEdit_UserName.setPlaceholderText(
            _translate("MainWindow", "Enter User name"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.lineEdit_Password.setToolTip(_translate("MainWindow", "password"))
        self.lineEdit_Password.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.pushButton_Login.setToolTip(_translate("MainWindow", "submit"))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        self.error_label.setText(_translate("MainWindow", ""))

    def login(self):
        username = self.lineEdit_UserName.text()
        password = self.lineEdit_Password.text()

        database = "./liberary_info.db"

        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("SELECT * FROM login WHERE name=? AND password=?",
                  (username, password))
        data = c.fetchall()

        if len(data) == 0:
            self.error_label.setText("Invalid username or password")

        else:
            if username == 'jahannia' and password == 'jahannia':
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_employerWindow()
                self.ui.setupUi(self.window)
                self.window.show()
            else:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_OtherWindow(password=password, username=username)
                self.ui.setupUi(self.window)
                self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
