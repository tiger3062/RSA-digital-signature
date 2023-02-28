import re
import math
import random
from Cryptodome.Hash import SHA1
from sympy import isprime

# Qt5 lib
import qtmodern.styles
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 28, 29, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnGen = QtWidgets.QPushButton(self.groupBox)
        self.btnGen.setGeometry(QtCore.QRect(10, 280, 341, 31))
        self.btnGen.setObjectName("btnGen")
        self.btnCalc = QtWidgets.QPushButton(self.groupBox)
        self.btnCalc.setGeometry(QtCore.QRect(10, 200, 341, 31))
        self.btnCalc.setObjectName("btnCalc")
        self.txtp = QtWidgets.QLineEdit(self.groupBox)
        self.txtp.setGeometry(QtCore.QRect(10, 52, 167, 24))
        self.txtp.setObjectName("txtp")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(183, 28, 104, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 82, 29, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtq = QtWidgets.QLineEdit(self.groupBox)
        self.txtq.setGeometry(QtCore.QRect(10, 106, 167, 24))
        self.txtq.setObjectName("txtq")
        self.lble = QtWidgets.QLabel(self.groupBox)
        self.lble.setGeometry(QtCore.QRect(183, 82, 161, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lble.setFont(font)
        self.lble.setObjectName("lble")
        self.txtn = QtWidgets.QLineEdit(self.groupBox)
        self.txtn.setGeometry(QtCore.QRect(183, 52, 167, 24))
        self.txtn.setObjectName("txtn")
        self.txte = QtWidgets.QLineEdit(self.groupBox)
        self.txte.setGeometry(QtCore.QRect(183, 106, 167, 24))
        self.txte.setObjectName("txte")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(183, 136, 113, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtd = QtWidgets.QLineEdit(self.groupBox)
        self.txtd.setGeometry(QtCore.QRect(183, 160, 167, 24))
        self.txtd.setObjectName("txtd")
        self.lblDes = QtWidgets.QLabel(self.groupBox)
        self.lblDes.setGeometry(QtCore.QRect(360, 30, 401, 121))
        self.lblDes.setObjectName("lblDes")
        self.lblWarning = QtWidgets.QLabel(self.groupBox)
        self.lblWarning.setGeometry(QtCore.QRect(360, 170, 401, 71))
        self.lblWarning.setText("")
        self.lblWarning.setObjectName("lblWarning")
        self.btnCheck = QtWidgets.QPushButton(self.groupBox)
        self.btnCheck.setGeometry(QtCore.QRect(10, 240, 341, 31))
        self.btnCheck.setObjectName("btnCheck")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(11, 340, 381, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 81, 21))
        self.label_7.setObjectName("label_7")
        self.senderMsg = QtWidgets.QLineEdit(self.groupBox_2)
        self.senderMsg.setGeometry(QtCore.QRect(10, 60, 361, 61))
        self.senderMsg.setText("")
        self.senderMsg.setReadOnly(True)
        self.senderMsg.setObjectName("senderMsg")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 450, 361, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 310, 141, 21))
        self.label_11.setObjectName("label_11")
        self.senderOpen = QtWidgets.QPushButton(self.groupBox_2)
        self.senderOpen.setGeometry(QtCore.QRect(10, 130, 361, 31))
        self.senderOpen.setObjectName("senderOpen")
        self.MD1 = QtWidgets.QTextEdit(self.groupBox_2)
        self.MD1.setGeometry(QtCore.QRect(10, 200, 361, 101))
        self.MD1.setReadOnly(True)
        self.MD1.setObjectName("MD1")
        self.SIGNATURE1 = QtWidgets.QTextEdit(self.groupBox_2)
        self.SIGNATURE1.setGeometry(QtCore.QRect(10, 340, 361, 101))
        self.SIGNATURE1.setReadOnly(True)
        self.SIGNATURE1.setObjectName("SIGNATURE1")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 340, 381, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 170, 81, 21))
        self.label_9.setObjectName("label_9")
        self.recMsg = QtWidgets.QLineEdit(self.groupBox_3)
        self.recMsg.setGeometry(QtCore.QRect(10, 60, 361, 61))
        self.recMsg.setText("")
        self.recMsg.setReadOnly(True)
        self.recMsg.setObjectName("recMsg")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 310, 131, 21))
        self.label_12.setObjectName("label_12")
        self.recOpen = QtWidgets.QPushButton(self.groupBox_3)
        self.recOpen.setGeometry(QtCore.QRect(10, 130, 361, 31))
        self.recOpen.setObjectName("recOpen")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 450, 361, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.SIGNATURE2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.SIGNATURE2.setGeometry(QtCore.QRect(10, 340, 361, 101))
        self.SIGNATURE2.setReadOnly(True)
        self.SIGNATURE2.setObjectName("SIGNATURE2")
        self.MD2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.MD2.setGeometry(QtCore.QRect(10, 200, 361, 101))
        self.MD2.setReadOnly(True)
        self.MD2.setObjectName("MD2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 840, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Key generation"))
        self.label.setText(_translate("MainWindow", "p = "))
        self.btnGen.setText(_translate("MainWindow", "Generate key"))
        self.btnCalc.setText(_translate("MainWindow", "Calculate key"))
        self.label_4.setText(_translate("MainWindow", "n ="))
        self.label_2.setText(_translate("MainWindow", "q = "))
        self.lble.setText(_translate("MainWindow", "e ="))
        self.label_6.setText(_translate("MainWindow", "d ="))
        self.lblDes.setText(_translate("MainWindow", "- p and q: prime number\n"
"- n: part of public key, calculated by computer\n"
"- e: part of public key, user define, 0 < e < tot(n), \n"
" e and tot(n) are coprime (common choices: 3, 17, 65537)\n"
"- d: private key, calculated by computer, keep secret"))
        self.btnCheck.setText(_translate("MainWindow", "Check e"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sender"))
        self.label_3.setText(_translate("MainWindow", "Message:"))
        self.label_7.setText(_translate("MainWindow", "MD1:"))
        self.pushButton.setText(_translate("MainWindow", "Create digital signature"))
        self.label_11.setText(_translate("MainWindow", "Digital signature:"))
        self.senderOpen.setText(_translate("MainWindow", "Open file"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Receiver"))
        self.label_8.setText(_translate("MainWindow", "Message:"))
        self.label_9.setText(_translate("MainWindow", "MD2:"))
        self.label_12.setText(_translate("MainWindow", "Digital signature:"))
        self.recOpen.setText(_translate("MainWindow", "Open file"))
        self.pushButton_2.setText(_translate("MainWindow", "Check digital signature"))

        #Button
        self.btnCalc.clicked.connect(self.gen_n)
        self.btnCheck.clicked.connect(self.gen_d)
        self.senderOpen.clicked.connect(lambda: self.open_file(self.senderMsg, self.MD1, self.SIGNATURE1))
        self.recOpen.clicked.connect(lambda: self.open_file(self.recMsg, self.MD2, self.SIGNATURE2))
        self.pushButton.clicked.connect(lambda: self.hash_file(flocal, self.MD1, self.SIGNATURE1))
        self.pushButton_2.clicked.connect(lambda: self.hash_file(flocal, self.MD2, self.SIGNATURE2))
        self.btnGen.clicked.connect(self.random_generated)

    def check_prime(self, a, b):
        global tot
        tot = math.lcm(a - 1, b - 1)
        if not isprime(a) and not isprime(b):
            self.lblWarning.setText(f"WARNING: {a} and {b} are not a prime number")
        elif not isprime(a) and isprime(b):
            self.lblWarning.setText(f"WARNING: {a} is not a prime number")
        elif isprime(a) and not isprime(b):
            self.lblWarning.setText(f"WARNING: {b} is not a prime number")
        else:
            return True

    def check_e(self, c):
        if 1 < c < tot:
            if math.gcd(c, tot) == 1:
                self.lblWarning.setText("INFORMATION: e is within parameters, continue")
                return True
            else:
                self.lblWarning.setText(f"WARNING: {c} and {tot} are not coprime")
        else:
            self.lblWarning.setText(f"WARNING: {c} is not in range from 1 to {tot}")

    def gen_n(self):
        if self.txtp.text() == "" or self.txtq.text() == '':
            return
        else:
            p = int(self.txtp.text())
            q = int(self.txtq.text())
            n = p * q
            if not self.check_prime(p, q):
                return
            else:
                g = self.lble.text()
                self.lble.setText(g + f' (tot(n) = {tot})')
                self.txtn.setText(str(n))

    def gen_d(self):
        if self.txte.text() == '':
            return
        p = int(self.txtp.text())
        q = int(self.txtq.text())
        e = int(self.txte.text())
        if not self.check_e(e):
            return
        else:
            d = pow(e, -1, tot)
            self.txtd.setText(str(d))

    def hash_file(self, filename, MD, DS):
        e = self.txte.text()
        n = self.txtn.text()
        if filename == '' or e == '' or n == '':
            return
        h = SHA1.new()
        with open(filename, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        h = h.hexdigest()
        MD.setText(h)
        e = int(self.txte.text())
        n = int(self.txtn.text())
        signature = [pow(ord(c), e, n) for c in h]
        DS.setText(''.join(map(lambda x: str(x), signature)))
        if DS == self.SIGNATURE2:
            sig1 = self.SIGNATURE1.toPlainText()
            sig2 = self.SIGNATURE2.toPlainText()
            if sig1 == sig2:
                self.label_10.setText("Signatures match, content is secured.")
            else:
                self.label_10.setText("Signatures not match, content has been tampered or wrong file.")
        else:
            return

    def open_file(self, msg_box, MD, DS):
        global flocal
        fname = QFileDialog.getOpenFileNames(parent=None, caption="Open file")
        flocal = str(re.sub(r"[\[\]\']", '', str(fname[0])))
        if flocal != '':
            msg_box.setText(flocal)
        DS.setText('')
        MD.setText('')
        return

    def random_generated(self):
        minPrime = 100
        maxPrime = 1000
        cached_primes = [i for i in range(minPrime, maxPrime) if isprime(i)]
        p, q = random.sample(cached_primes, 2)
        n = int(p * q)
        tot = math.lcm(p - 1, q - 1)
        e = random.randrange(1, tot)
        g = math.gcd(e, tot)
        if g == 1:
            d = pow(e, -1, tot)
        while g != 1:
            e = random.randrange(1, tot)
            g = math.gcd(e, tot)
            if g == 1:
                d = pow(e, -1, tot)
                break
        self.txtp.setText(str(p))
        self.txtq.setText(str(q))
        self.txtn.setText(str(n))
        self.txte.setText(str(e))
        self.txtd.setText(str(d))
        del cached_primes


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    qtmodern.styles.dark(app)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

