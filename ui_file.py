from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 419)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.826109, y1:1, x2:0.134348, y2:0.182, stop:0.0945274 rgba(55, 54, 83, 255), stop:1 rgba(134, 65, 80, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.createButton = QtWidgets.QPushButton(Form)
        self.createButton.setGeometry(QtCore.QRect(80, 110, 181, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(0, 0, 0);")
        self.createButton.setObjectName("createButton")
        self.editButton = QtWidgets.QPushButton(Form)
        self.editButton.setGeometry(QtCore.QRect(80, 150, 181, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(0, 0, 0);")
        self.editButton.setObjectName("editButton")
        self.showButton = QtWidgets.QPushButton(Form)
        self.showButton.setGeometry(QtCore.QRect(80, 260, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.showButton.setFont(font)
        self.showButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(0, 0, 0);")
        self.showButton.setObjectName("showButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 300, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.main_spinBox = QtWidgets.QSpinBox(Form)
        self.main_spinBox.setGeometry(QtCore.QRect(140, 300, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.main_spinBox.setFont(font)
        self.main_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(0, 0, 0);")
        self.main_spinBox.setMaximum(10000)
        self.main_spinBox.setObjectName("main_spinBox")
        self.databaseButton = QtWidgets.QPushButton(Form)
        self.databaseButton.setGeometry(QtCore.QRect(80, 190, 181, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.databaseButton.setFont(font)
        self.databaseButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-color: rgb(0, 0, 0);")
        self.databaseButton.setObjectName("databaseButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Заметки"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">NoteApp</span></p></body></html>"))
        self.createButton.setText(_translate("Form", "Создать заметку"))
        self.editButton.setText(_translate("Form", "Редактировать БД"))
        self.showButton.setText(_translate("Form", "Показать заметку"))
        self.label_2.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">ID:</span></p></body></html>"))
        self.databaseButton.setText(_translate("Form", "Показать БД"))


class Ui_edit(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 351)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.826109, y1:1, x2:0.134348, y2:0.182, stop:0.0945274 rgba(55, 54, 83, 255), stop:1 rgba(134, 65, 80, 255));\n"
            "border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.edit_spinBox.setGeometry(QtCore.QRect(240, 20, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.edit_spinBox.setFont(font)
        self.edit_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(0, 0, 0);")
        self.edit_spinBox.setMaximum(10000)
        self.edit_spinBox.setObjectName("edit_spinBox")
        self.edit_foundButton = QtWidgets.QPushButton(self.centralwidget)
        self.edit_foundButton.setGeometry(QtCore.QRect(10, 50, 191, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.edit_foundButton.setFont(font)
        self.edit_foundButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 0, 0);")
        self.edit_foundButton.setObjectName("edit_foundButton")
        self.edit_saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.edit_saveButton.setGeometry(QtCore.QRect(210, 50, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.edit_saveButton.setFont(font)
        self.edit_saveButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(0, 0, 0);")
        self.edit_saveButton.setObjectName("edit_saveButton")
        self.edit_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.edit_tableWidget.setGeometry(QtCore.QRect(10, 90, 431, 241))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        self.edit_tableWidget.setFont(font)
        self.edit_tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 0, 0);")
        self.edit_tableWidget.setObjectName("edit_tableWidget")
        self.edit_tableWidget.setColumnCount(0)
        self.edit_tableWidget.setRowCount(0)
        self.edit_deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.edit_deleteButton.setGeometry(QtCore.QRect(330, 50, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.edit_deleteButton.setFont(font)
        self.edit_deleteButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-color: rgb(0, 0, 0);")
        self.edit_deleteButton.setObjectName("edit_deleteButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заметки (редактирование)"))
        self.edit_foundButton.setText(_translate("MainWindow", "Найти заметку"))
        self.edit_saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.edit_deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">Укажите ID заметки:</span></p></body></html>"))


class Ui_create(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 323)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.826109, y1:1, x2:0.134348, y2:0.182, stop:0.0945274 rgba(55, 54, 83, 255), stop:1 rgba(134, 65, 80, 255));")
        self.create_lineEdit2 = QtWidgets.QLineEdit(Form)
        self.create_lineEdit2.setGeometry(QtCore.QRect(110, 110, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.create_lineEdit2.setFont(font)
        self.create_lineEdit2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 0, 0);")
        self.create_lineEdit2.setObjectName("create_lineEdit2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgba(255, 255, 255, 0);")
        self.label_4.setObjectName("label_4")
        self.create_textEdit = QtWidgets.QTextEdit(Form)
        self.create_textEdit.setGeometry(QtCore.QRect(110, 170, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.create_textEdit.setFont(font)
        self.create_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(0, 0, 0);")
        self.create_textEdit.setObjectName("create_textEdit")
        self.create_saveButton = QtWidgets.QPushButton(Form)
        self.create_saveButton.setGeometry(QtCore.QRect(20, 280, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.create_saveButton.setFont(font)
        self.create_saveButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-color: rgb(0, 0, 0);")
        self.create_saveButton.setObjectName("create_saveButton")
        self.create_clearButton = QtWidgets.QPushButton(Form)
        self.create_clearButton.setGeometry(QtCore.QRect(130, 280, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.create_clearButton.setFont(font)
        self.create_clearButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-color: rgb(0, 0, 0);")
        self.create_clearButton.setObjectName("create_clearButton")
        self.create_spinBox = QtWidgets.QSpinBox(Form)
        self.create_spinBox.setGeometry(QtCore.QRect(110, 60, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.create_spinBox.setFont(font)
        self.create_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-color: rgb(0, 0, 0);")
        self.create_spinBox.setMaximum(10000)
        self.create_spinBox.setObjectName("create_spinBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Заметки (создание)"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:16pt;\">Создание новой заметки</span></p></body></html>"))
        self.label_2.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">ID:</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">Заголовок:</span></p></body></html>"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">Текст:</span></p></body></html>"))
        self.create_saveButton.setText(_translate("Form", "Сохранить"))
        self.create_clearButton.setText(_translate("Form", "Очистить"))


class Ui_show(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 358)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.826109, y1:1, x2:0.134348, y2:0.182, stop:0.0945274 rgba(55, 54, 83, 255), stop:1 rgba(134, 65, 80, 255));")
        self.show_textBrowser2 = QtWidgets.QTextBrowser(Form)
        self.show_textBrowser2.setGeometry(QtCore.QRect(20, 50, 251, 291))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.show_textBrowser2.setFont(font)
        self.show_textBrowser2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-color: rgb(0, 0, 0);\n"
                                             "selection-color: rgb(255, 255, 255);")
        self.show_textBrowser2.setObjectName("show_textBrowser2")
        self.show_label = QtWidgets.QLabel(Form)
        self.show_label.setGeometry(QtCore.QRect(20, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.show_label.setFont(font)
        self.show_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgba(255, 255, 255, 0);")
        self.show_label.setObjectName("show_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Заметка"))
        self.show_textBrowser2.setHtml(_translate("Form",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Source Sans Pro\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sssss</p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">eqdqe</p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">eq</p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.show_label.setText(_translate("Form",
                                           "<html><head/><body><p><span style=\" font-size:16pt;\">Title example</span></p></body></html>"))


class Ui_database(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(462, 390)
        widget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.826109, y1:1, x2:0.134348, y2:0.182, stop:0.0945274 rgba(55, 54, 83, 255), stop:1 rgba(134, 65, 80, 255));")
        self.show_tableWidget = QtWidgets.QTableWidget(widget)
        self.show_tableWidget.setGeometry(QtCore.QRect(10, 10, 441, 361))
        self.show_tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 0, 0);")
        self.show_tableWidget.setAutoScroll(True)
        self.show_tableWidget.setTabKeyNavigation(True)
        self.show_tableWidget.setDragEnabled(False)
        self.show_tableWidget.setObjectName("show_tableWidget")
        self.show_tableWidget.setColumnCount(0)
        self.show_tableWidget.setRowCount(0)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "База данных"))
