import sqlite3
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore
from ui_file import Ui_MainWindow, Ui_edit, Ui_create, Ui_show, Ui_database


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createButton.clicked.connect(self.create_note)
        self.editButton.clicked.connect(self.open_edit_widget)
        self.showButton.clicked.connect(self.show_note)
        self.databaseButton.clicked.connect(self.show_database)
        self.setWindowIcon(QtGui.QIcon('icons\icon3.png'))

    def show_database(self):
        self.DatabaseWidget = DatabaseWidget()
        self.DatabaseWidget.show()

    def create_note(self):
        self.Create_widget = CreateWidget()
        self.Create_widget.show()

    def open_edit_widget(self):
        self.Edit_widget = EditWidget()
        self.Edit_widget.show()

    def show_note(self):
        note_id = self.main_spinBox.text()
        self.con = sqlite3.connect("notes.db")
        self.cursor = self.con.cursor()

        check = self.cursor.execute("SELECT EXISTS(SELECT 1 FROM notes WHERE id like ?)",
                                    (note_id,)).fetchall()[0][0]
        if check:
            note_data = self.cursor.execute("SELECT * FROM notes WHERE id like ?", (note_id,)).fetchall()
            self.con.commit()
            title = note_data[0][1]
            text = note_data[0][2]

            self.NoteWidget = NoteWidget(title, text)
            self.NoteWidget.show()
        else:
            QMessageBox.information(self, "Предупреждение",
                                    "Заметки с указанным ID не существует")


class CreateWidget(QMainWindow, Ui_create):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons\icon3.png'))
        self.create_saveButton.clicked.connect(self.save_note)
        self.create_clearButton.clicked.connect(self.clear_elem)

        self.con = sqlite3.connect("notes.db")
        self.cursor = self.con.cursor()

    def save_note(self):
        id = int(self.create_spinBox.text())
        title = str(self.create_lineEdit2.text())
        text = str(self.create_textEdit.toPlainText())

        check = self.cursor.execute("SELECT EXISTS(SELECT 1 FROM notes WHERE id like ?)",
                                    (id,)).fetchall()[0][0]
        if not check:
            self.cursor.execute("insert into notes (id, title, text) values (?, ?, ?)", (id, title, text))
            self.con.commit()
        else:
            QMessageBox.information(self, "Предупреждение",
                                    "Заметка с указанным ID уже существует")

    def clear_elem(self):
        self.create_spinBox.clear()
        self.create_lineEdit2.clear()
        self.create_textEdit.clear()


class EditWidget(QMainWindow, Ui_edit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons\icon3.png'))
        self.con = sqlite3.connect("notes.db")
        self.edit_foundButton.clicked.connect(self.update_result)
        self.edit_tableWidget.itemChanged.connect(self.item_changed)
        self.edit_saveButton.clicked.connect(self.save_result)
        self.edit_deleteButton.clicked.connect(self.delete_elem)

        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("Select * from notes WHERE id=?",
                             (self.edit_spinBox.text(),)).fetchall()

        check = self.con.execute("SELECT EXISTS(SELECT 1 FROM notes WHERE id like ?)",
                                 (self.edit_spinBox.text(),)).fetchall()[0][0]
        if check:
            self.edit_tableWidget.setRowCount(len(result))
            self.edit_tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.edit_tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.modified = {}
        else:
            QMessageBox.information(self, "Предупреждение",
                                    "Заметки с указанным ID не существует")

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_result(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE notes SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE id = ?"
            cur.execute(que, (self.edit_spinBox.text(),))
            self.con.commit()

    def delete_elem(self):
        rows = list(set([i.row() for i in self.edit_tableWidget.selectedItems()]))
        ids = [self.edit_tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(self, '',
                                     "Удалить заметку с id " +
                                     ",".join(ids), QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from notes WHERE ID in (" +
                        ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()


class NoteWidget(QMainWindow, Ui_show):
    def __init__(self, title, text):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons\icon3.png'))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show_label.setText(title)
        self.show_label.setFont(QtGui.QFont('Source sans pro', 15))
        self.show_textBrowser2.setText(text)
        self.show_textBrowser2.setFont(QtGui.QFont('Source sans pro', 12))

    def mousePressEvent(self, event):
        if event.buttons() == Qt.RightButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.RightButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


class DatabaseWidget(QMainWindow, Ui_database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons\icon3.png'))
        self.titles2 = None

        self.con = sqlite3.connect("notes.db")
        cur = self.con.cursor()

        check = self.con.execute("SELECT EXISTS(SELECT * FROM notes)").fetchall()[0][0]

        if check:
            result = cur.execute("SELECT * FROM notes").fetchall()
            self.show_tableWidget.setRowCount(len(result))
            self.show_tableWidget.setColumnCount(len(result[0]))
            self.titles2 = [description[0] for description in cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.show_tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.show_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.exit(app.exec_())
