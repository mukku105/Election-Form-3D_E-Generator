# Form implementation generated from reading ui file 'c:\Python\mukku_workspace\Election Form 3D_E Generator\ui\main_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(672, 515)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 541, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.selectFormTypeLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectFormTypeLabel.setFont(font)
        self.selectFormTypeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.selectFormTypeLabel.setObjectName("selectFormTypeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.selectFormTypeLabel)
        self.formTypeComboBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formTypeComboBox.sizePolicy().hasHeightForWidth())
        self.formTypeComboBox.setSizePolicy(sizePolicy)
        self.formTypeComboBox.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.formTypeComboBox.setFont(font)
        self.formTypeComboBox.setStyleSheet("QComboBox {\n"
"    padding: 5px 10px;\n"
"}\n"
"")
        self.formTypeComboBox.setObjectName("formTypeComboBox")
        self.formTypeComboBox.addItem("")
        self.formTypeComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.formTypeComboBox)
        self.comboBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.comboBox)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(85, 255, 255);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 15px 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 255, 127);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.selectFormTypeLabel.setText(_translate("Form", "Select Form Type : "))
        self.formTypeComboBox.setItemText(0, _translate("Form", "Form 3D"))
        self.formTypeComboBox.setItemText(1, _translate("Form", "Form 3E"))
        self.comboBox.setItemText(0, _translate("Form", "-- Select Constituency --"))
        self.comboBox.setItemText(1, _translate("Form", "9-Barfung"))
        self.comboBox.setItemText(2, _translate("Form", "10-Poklok-Kamrang"))
        self.comboBox.setItemText(3, _translate("Form", "11-Namchi-Singhithang"))
        self.comboBox.setItemText(4, _translate("Form", "12-Melli"))
        self.comboBox.setItemText(5, _translate("Form", "13-Namthang-Rateypanni"))
        self.comboBox.setItemText(6, _translate("Form", "14-Temi-Namphing"))
        self.comboBox.setItemText(7, _translate("Form", "15-Rangang-Yangang"))
        self.pushButton.setText(_translate("Form", "Save Configuration"))