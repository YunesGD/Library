# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employer.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import uuid

import sqlite3


class Ui_employerWindow(object):
    def __init__(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("liberary_info.db")
        self.db.open()

    def setupUi(self, employerWindow):
        employerWindow.setObjectName("employerWindow")
        employerWindow.resize(950, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("employer.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        employerWindow.setWindowIcon(icon)
        employerWindow.setStyleSheet("#MainWindow{\n"
                                     "background-image:url(\"lib.jpg\");\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QLabel{\n"
                                     "color: black;\n"
                                     "font: 11pt \"OCR-B 10 BT\";\n"
                                     "\n"
                                     "}\n"
                                     "QLineEdit{\n"
                                     "width:300px;\n"
                                     "height:40px;\n"
                                     "background-color:transparent;\n"
                                     "border: 2px solid #999;\n"
                                     "border-radius: 10px;\n"
                                     "padding-left: 10px;\n"
                                     "color: black;\n"
                                     "font: 12pt \"OCR-B 10 BT\";\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton{\n"
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
                                     "background-color: rgba(0, 0, 0, 0.6);\n"
                                     "}\n"
                                     "")
        self.centralwidget = QtWidgets.QWidget(employerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        # self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_Search = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Search.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.horizontalLayout.addWidget(self.lineEdit_Search)

        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setStyleSheet("background: rgb(106, 203, 255)")
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.add_user = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.add_user.sizePolicy().hasHeightForWidth())
        self.add_user.setSizePolicy(sizePolicy)
        self.add_user.setObjectName("add_user")
        self.verticalLayout_2.addWidget(self.add_user)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_3.addWidget(self.lineEdit_6)
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_3.addWidget(self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setPlaceholderText(
            "ID will be generated automatically")
        self.lineEdit_3.setPlaceholderText(
            "ID will be generated automatically")
        self.verticalLayout_3.addWidget(self.lineEdit_8)
        self.add_book = QtWidgets.QPushButton(self.tab_4)
        self.add_book.setObjectName("add_book")
        self.verticalLayout_3.addWidget(self.add_book)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        employerWindow.setCentralWidget(self.centralwidget)
        # set fill width for talebview
        self.tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.tableView.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("users")
        self.tableView.setModel(self.model)
        self.tableView.show()
        self.model.select()
        self.lineEdit_Search.textChanged.connect(self.search)

        self.add_user.clicked.connect(self.add_user_clicked)
        self.add_book.clicked.connect(self.add_book_clicked)

        self.retranslateUi(employerWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(employerWindow)

    def retranslateUi(self, employerWindow):
        _translate = QtCore.QCoreApplication.translate
        employerWindow.setWindowTitle(_translate("employerWindow", "Employer"))
        self.label_3.setText(_translate("employerWindow", "Enter name : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("employerWindow", "Search user"))
        self.label_4.setText(_translate("employerWindow", "Name :"))
        self.label_5.setText(_translate("employerWindow", "Family :"))
        self.label_6.setText(_translate("employerWindow", "ID :"))
        self.label_10.setText(_translate("employerWindow", "E-mail :"))
        self.add_user.setText(_translate("employerWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), _translate("employerWindow", "Insert User"))
        self.label.setText(_translate("employerWindow", "Name :"))
        self.label_2.setText(_translate("employerWindow", "Author :"))
        self.label_7.setText(_translate("employerWindow", "Publication :"))
        self.label_8.setText(_translate("employerWindow", "Year :"))
        self.label_9.setText(_translate("employerWindow", "ID :"))
        self.add_book.setText(_translate("employerWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_4), _translate("employerWindow", "Add book"))

    def add_user_clicked(self):
        conn = sqlite3.connect('liberary_info.db')
        c = conn.cursor()

        name = self.lineEdit.text()
        if name == "":
            self.lineEdit.setPlaceholderText("You have to  enter Name")
        family = self.lineEdit_2.text()
        if family == "":
            self.lineEdit_2.setPlaceholderText("You have to  enter Family")
        id = str(uuid.uuid4().fields[-1])[:5]
        self.lineEdit_3.setText(id)
        if id == "":
            self.lineEdit_3.setPlaceholderText("You have to  enter ID")
        email = self.lineEdit_9.text()
        if email == "":
            self.lineEdit_9.setPlaceholderText("You have to  enter email")

        if len(name) != 0 and len(family) != 0 and len(id) != 0 and len(email) != 0:
            try:
                c.execute("INSERT INTO login VALUES (?,?)", (name, id))
                c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)",
                          (id, name, family, email, 'None', 'None', 'None'))
                conn.commit()
                self.show_message(
                    f"User added successfully \n ID : {id} \n Name : {name} \n Family : {family} \n Email : {email} \n-----------------------------------------\n username : {name} \n password : {id}")
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_9.clear()

            except:
                self.show_message("something went wrong")
        self.model.select()
        self.tableView.show()

    def add_book_clicked(self):
        status = 'available'
        name = self.lineEdit_4.text()
        if name == "":
            self.lineEdit_4.setPlaceholderText("You have to  enter Name")
        author = self.lineEdit_5.text()
        if author == "":
            self.lineEdit_5.setPlaceholderText("You have to  enter Author")
        publication = self.lineEdit_6.text()
        if publication == "":
            self.lineEdit_6.setPlaceholderText(
                "You have to  enter Publication")
        year = self.lineEdit_7.text()
        if year == "":
            self.lineEdit_7.setPlaceholderText("You have to  enter Year")
        id = str(uuid.uuid4().fields[-1])[:5]
        self.lineEdit_8.setText(id)
        if id == "":
            self.lineEdit_8.setPlaceholderText("you have to  enter ID")
        if len(name) != 0 and len(author) != 0 and len(publication) != 0 and len(year) != 0 and len(id) != 0:
            try:
                conn = sqlite3.connect('liberary_info.db')
                c = conn.cursor()
                c.execute("INSERT INTO book VALUES (?,?,?,?,?,?)",
                          (id, name, author, publication, year, status))
                conn.commit()
                self.show_message(
                    f"Book added successfully \n ID : {id} \n Name : {name} \n Author : {author} \n Publication : {publication} \n Year : {year} \n Status : {status}")
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.lineEdit_7.clear()
                self.lineEdit_8.clear()
            except:
                self.show_message("Something went wrong")
        self.model.select()
        self.tableView.show()

    def search(self, text):
        self.model.setFilter(f"Name LIKE '%{text}%'")
        self.model.select()
        self.tableView.show()

    def show_message(self, message):
        msg = QtWidgets.QMessageBox()
        # set width and height
        msg.setFixedSize(600, 350)

        msg.setText(message)

        msg.setWindowTitle("Message")
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    employerWindow = QtWidgets.QMainWindow()
    ui = Ui_employerWindow()
    ui.setupUi(employerWindow)
    employerWindow.show()
    sys.exit(app.exec_())
