from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

import caesar_cipher, autokey_cipher, multiplicative_cipher, stream_cipher, transposition_cipher, vigenere_cipher, case_transform, reverse_transform

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.key = 3
        self.input_text = ""
        self.output_text = "jj"
        self.cipher_chosen = "Caesar Cipher"
        self.trans_chosen = "Case Transform"
        self.trans_yes = 0
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-color: #A8CF99;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QtCore.QRect(10, 5, 1910, 1080))
        #self.centralwidget.setStyleSheet("background-color: black;")
        
        # For encryption button
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(1050, 40, 200, 60))
        self.radioButton1.setObjectName("Encrypt")
        
        # For decryption Button
        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(1400, 40, 200, 60))
        self.radioButton2.setObjectName("Decrypt")
        
        
        # For Dropdown Cipher
        cipher_list = ["Caesar Cipher", "Multiplicative Cipher", "Autokey Cipher", "Stream Cipher", "Transposition Cipher", "Vigenere Cipher"]
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1400, 150, 400, 80))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)
        self.comboBox.addItems(cipher_list)
        
        # For Dropdown Transform
        cipher_list = ["Case Transform", "Reverse Transform"]
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(1400, 300, 400, 80))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.setEditable(True)
        self.comboBox1.addItems(cipher_list)
        
        # For input button
        self.inputButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputButton.setGeometry(QtCore.QRect(1050, 150, 200, 80))
        self.inputButton.setObjectName("inputButton")
        
        # Checkbox for Transform
        self.trans_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.trans_checkbox.setGeometry(QtCore.QRect(1050, 310, 200, 60))
        self.trans_checkbox.setObjectName("trans_checkbox")
        
        # For Run button
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(1050, 500, 500, 80))
        self.runButton.setObjectName("runButton")
        
        # For flush Button
        self.flushButton = QtWidgets.QPushButton(self.centralwidget)
        self.flushButton.setGeometry(QtCore.QRect(750, 40, 200, 60))
        self.flushButton.setObjectName("flushButton")
        
        # For open Button
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(20, 40, 200, 60))
        self.openButton.setObjectName("openButton")
        
        #For the list widget input
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 150, 450, 800))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        
        #For the list widget output
        self.listWidget1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget1.setGeometry(QtCore.QRect(500, 150, 450, 800))
        self.listWidget1.setObjectName("listWidget1")
        item = QtWidgets.QListWidgetItem()
        self.listWidget1.addItem(item)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    #----------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cryptography"))
        
        # For encrypt radio button
        self.radioButton1.setText(_translate("centralwidget", "Encrypt"))
        self.radioButton1.setStyleSheet('QRadioButton {background-color: white; color: green; border:3px solid green;}')
        self.radioButton1.setChecked(True)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        self.radioButton1.setFont(font)
        #self.radioButton1.toggled.connect(self.onEncryptButton)
        
        # For decryption Button
        self.radioButton2.setText(_translate("centralwidget", "Decrypt"))
        self.radioButton2.setStyleSheet('QRadioButton {background-color: white; color: green; border:3px solid green;}')
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        self.radioButton2.setFont(font)
        #self.radioButton2.toggled.connect(self.onDecryptButton)
        
        # For the drop down transform
        self.comboBox.setStyleSheet('QComboBox {background-color: white; color: green; border:3px solid green; font-family: Sitka Small; font: 12;} QComboBox::down-arrow {border: 1px dotted green;}')
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(8)
        self.comboBox.setFont(font)
        font = QtGui.QFont("Sitka", 10)
        line_edit = self.comboBox.lineEdit()
        line_edit.setFont(font)
        self.comboBox.activated[str].connect(self.choose_cipher)
        
        # For the drop down transform
        self.comboBox1.setStyleSheet('QComboBox {background-color: white; color: green; border:3px solid green; font-family: Sitka Small; font: 12;} QComboBox::down-arrow {border: 1px dotted green;}')
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(8)
        self.comboBox1.setFont(font)
        font = QtGui.QFont("Sitka", 10)
        line_edit = self.comboBox1.lineEdit()
        line_edit.setFont(font)
        self.comboBox1.activated[str].connect(self.choose_transform)
        
        # For Key input
        self.inputButton.setText(_translate("centralwidget", "Enter the key"))
        self.inputButton.setStyleSheet('QPushButton {background-color: white; color: green; border:4px solid green;}')        
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        self.inputButton.setFont(font)
        self.inputButton.clicked.connect(self.take_input)
        
        # Checkbox for Transform
        self.trans_checkbox.setText(_translate("centralwidget", "Transform"))
        self.trans_checkbox.setStyleSheet('QCheckBox {background-color: white; color: green; border:3px solid green;}')        
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.trans_checkbox.setFont(font)
        self.trans_checkbox.stateChanged.connect(self.transbox)
        
        # For run button
        self.runButton.setText(_translate("centralwidget", "Submit"))
        self.runButton.setStyleSheet('QPushButton {background-color: white; color: green; border:6px solid green;}')        
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(18)
        self.runButton.setFont(font)
        self.runButton.clicked.connect(self.runClicked)
        
        # For flush button
        self.flushButton.setText(_translate("centralwidget", "Save"))
        self.flushButton.setStyleSheet('QPushButton {background-color: white; color: green; border:3px solid green;}')        
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        self.flushButton.setFont(font)
        self.flushButton.clicked.connect(self.flushClicked)
        
        # For open Button
        self.openButton.setText(_translate("centralwidget", "Open"))
        self.openButton.setStyleSheet('QPushButton {background-color: white; color: green; border:3px solid green;}')        
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        self.openButton.setFont(font)
        self.openButton.clicked.connect(self.openClicked)
        
        # For list widget input
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.listWidget.setWordWrap(True)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet('QListWidget {background-color: white; color: green; border:3px solid green;}')        
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", ""))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        
        # For list widget output
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.listWidget1.setWordWrap(True)
        self.listWidget1.setFont(font)
        self.listWidget1.setStyleSheet('QListWidget {background-color: white; color: green; border:3px solid green;}')        
        __sortingEnabled = self.listWidget1.isSortingEnabled()
        self.listWidget1.setSortingEnabled(False)
        item = self.listWidget1.item(0)
        item.setText(_translate("MainWindow", ""))
        self.listWidget1.setSortingEnabled(__sortingEnabled)
        
    
    def onEncryptButton(self):
        if self.trans_yes == 0:
            if (self.cipher_chosen == "Caesar Cipher"):
                self.key = int(self.key)
                self.output_text = caesar_cipher.caesar_encryption(self.input_text, self.key)
            if (self.cipher_chosen == "Multiplicative Cipher"):
                self.key = int(self.key)
                self.output_text = multiplicative_cipher.multi_encrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Autokey Cipher"):
                self.key = str(self.key)
                self.output_text = autokey_cipher.autokey_encrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Stream Cipher"):
                self.key = str(self.key)
                self.output_text = stream_cipher.stream_encrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Transposition Cipher"):
                self.key = str(self.key)
                self.output_text = transposition_cipher.transposition_encrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Vigenere Cipher"):
                self.key = str(self.key)
                self.output_text = vigenere_cipher.vigenere_encrypt(self.input_text, self.key)
        else:
            if (self.trans_chosen == "Case Transform"):
                self.output_text = case_transform.case_transform(self.input_text)
            if (self.trans_chosen == "Reverse Transform"):
                self.output_text = reverse_transform.reverse(self.input_text)
            
    
    def onDecryptButton(self):
        if self.trans_yes == 0:
            if (self.cipher_chosen == "Caesar Cipher"):
                self.key = int(self.key)
                self.output_text = caesar_cipher.caesar_decryption(self.input_text, self.key)
            if (self.cipher_chosen == "Multiplicative Cipher"):
                self.key = int(self.key)
                self.output_text = multiplicative_cipher.multi_decrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Autokey Cipher"):
                self.key = str(self.key)
                self.output_text = autokey_cipher.autokey_decrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Stream Cipher"):
                self.key = str(self.key)
                self.output_text = stream_cipher.stream_decrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Transposition Cipher"):
                self.key = str(self.key)
                self.output_text = transposition_cipher.transposition_decrypt(self.input_text, self.key)
            if (self.cipher_chosen == "Vigenere Cipher"):
                self.key = str(self.key)
                self.output_text = vigenere_cipher.vigenere_decrypt(self.input_text, self.key)
        else:
            if (self.trans_chosen == "Case Transform"):
                self.output_text = case_transform.case_transform(self.input_text)
            if (self.trans_chosen == "Reverse Transform"):
                self.output_text = reverse_transform.reverse(self.input_text)
    
    def choose_cipher(self, text):
        self.listWidget1.clear()
        self.cipher_chosen = text
        
    def choose_transform(self, text):
        self.listWidget1.clear()
        self.trans_chosen = text
    
    def take_input(self):
        self.listWidget1.clear()
        inp, done = QtWidgets.QInputDialog.getText(self.centralwidget, 'Key Input', 'Enter the key:') 
        if done:
            self.key = inp
            
    def transbox(self, checked):
        if checked:
            self.trans_yes = 1
        else:
            self.trans_yes = 0
        
        
    
    def runClicked(self):
        if self.radioButton1.isChecked():
            self.onEncryptButton()
        if self.radioButton2.isChecked():
            self.onDecryptButton()
        self.listWidget1.clear()
        self.listWidget1.addItem(self.output_text)
        return
    
    
    def flushClicked(self):
        filename = QFileDialog.getSaveFileName(MainWindow, "Save File", '.txt')
        path = filename[0]
        if not path:
            return
        file1 = open(path, 'w')
        file1.write(self.output_text)
        file1.close() #Close the output file
        self.listWidget.clear()
        self.listWidget.addItem(self.input_text)
        
    
    def openClicked(self):
        self.listWidget1.clear()
        self.listWidget.clear() #clear the widget
        filename = QFileDialog.getOpenFileName() #open file dialog box
        path = filename[0] #it's address
        if not path:
            return
        file1 = open(path, "r") #open it
        self.input_text = file1.read() #assigning the string value
        self.listWidget.addItem(self.input_text) #showing it on listwidget
        file1.close() #Close the input file
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
