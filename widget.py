from PyQt5 import QtWidgets
from import_assist import Ui_Form
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import xlrd

class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.on_open)
        self.pushButton_switch.clicked.connect(self.on_switch)
        self.pushButton_import.clicked.connect(self.on_import)
        self.pushButton_clear.clicked.connect(self.on_clear)
        self.db = QSqlDatabase.addDatabase("QMYSQL")
    def on_import(self):
        workbook = xlrd.open_workbook(self.lineEdit_file_path.text())
        num_sheets = workbook.nsheets
        for sheet_index in range(4, num_sheets):
            sheet = workbook.sheet_by_index(sheet_index)
            num_rows = sheet.nrows

            i = 4
            j = 0
            k = 0

            while i < num_rows:
                type = sheet.cell_value(i, 0)
                if type == 'T204' or type == 'T205':
                    device_code = sheet.cell_value(i, 2)
                    online_status_pos = sheet.cell_value(i + 1, 17)
                    port_status_pos = sheet.cell_value(i + 2, 17)
                    if type == 'T204':
                        i += 10
                    else:
                        i += 8

                    query = QSqlQuery()
                    query.prepare("INSERT tbl_port_info(device_code,online_status_pos,port_status_pos) VALUES(:device_code,:online_status_pos,:port_status_pos)")
                    query.bindValue(":device_code", 'LN05-' + device_code)
                    query.bindValue(":online_status_pos", float(online_status_pos) * 100)
                    query.bindValue(":port_status_pos", float(port_status_pos) * 100)

                    if query.exec_():
                        j += 1
                    else:
                        k += 1
                        self.textEdit_error_msg.append(query.lastError().text())
                else:
                    device_code = sheet.cell_value(i, 2)
                    online_status_pos = sheet.cell_value(i + 1, 17)
                    alarm_type_pos = sheet.cell_value(i + 2, 17)
                    if type == 'T100' or type == 'T300' or type == 'T302' or type == 'T402':
                        i += 3
                    else:
                        i += 4

                    query = QSqlQuery()
                    query.prepare("INSERT tbl_device_info(device_code,online_status_pos,alarm_type_pos) VALUES(:device_code,:online_status_pos,:alarm_type_pos)")
                    query.bindValue(":device_code", 'LN05-' + device_code)
                    query.bindValue(":online_status_pos", float(online_status_pos) * 100)
                    query.bindValue(":alarm_type_pos", alarm_type_pos)

                    if query.exec_():
                        j += 1
                    else:
                        k += 1
                        self.textEdit_error_msg.append(query.lastError().text())
        self.lineEdit_total.setText(str(j + k))
        self.lineEdit_success.setText(str(j))
        self.lineEdit_fail.setText(str(k))

    def on_open(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("*.xlsx *.xls")

        if file_dialog.exec_() == QtWidgets.QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                self.lineEdit_file_path.setText(file_path)

    def on_switch(self):
        if self.pushButton_switch.text() == 'connect':
            try:
                self.db.setHostName(self.lineEdit_ip.text())
                self.db.setPort(int(self.lineEdit_port.text()))
                self.db.setDatabaseName(self.lineEdit_database_name.text())
                self.db.setUserName(self.lineEdit_user.text())
                self.db.setPassword(self.lineEdit_password.text())
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", str(e))
            if not self.db.open():
                error = self.db.lastError()
                QtWidgets.QMessageBox.critical(self, "Error", error.text())
            else:
                self.pushButton_switch.setText('disconnect')
        else:
            self.db.close()
            QSqlDatabase.removeDatabase("QMYSQL")
            self.pushButton_switch.setText('connect')

    def on_clear(self):
        self.textEdit_error_msg.clear()
        self.lineEdit_total.clear()
        self.lineEdit_success.clear()
        self.lineEdit_fail.clear()