# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_assist.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 101)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_ip = QtWidgets.QLineEdit(Form)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.horizontalLayout.addWidget(self.lineEdit_ip)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_port = QtWidgets.QLineEdit(Form)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout.addWidget(self.lineEdit_port)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_user = QtWidgets.QLineEdit(Form)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.horizontalLayout_2.addWidget(self.lineEdit_user)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_database_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_database_name.setObjectName("lineEdit_database_name")
        self.horizontalLayout_2.addWidget(self.lineEdit_database_name)
        self.pushButton_switch = QtWidgets.QPushButton(Form)
        self.pushButton_switch.setObjectName("pushButton_switch")
        self.horizontalLayout_2.addWidget(self.pushButton_switch)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_file_path = QtWidgets.QLineEdit(Form)
        self.lineEdit_file_path.setEnabled(True)
        self.lineEdit_file_path.setReadOnly(True)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_file_path)
        self.pushButton_open = QtWidgets.QPushButton(Form)
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout_3.addWidget(self.pushButton_open)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ip:"))
        self.label_2.setText(_translate("Form", "port:"))
        self.label_3.setText(_translate("Form", "user:"))
        self.label_4.setText(_translate("Form", "password:"))
        self.label_5.setText(_translate("Form", "database name:"))
        self.pushButton_switch.setText(_translate("Form", "connect"))
        self.label_6.setText(_translate("Form", "file path:"))
        self.pushButton_open.setText(_translate("Form", "open"))
        self.pushButton_2.setText(_translate("Form", "import"))
