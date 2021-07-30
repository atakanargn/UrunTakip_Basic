# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 461)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(553, 323))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 291, 441))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 269, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtID = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtID.setEnabled(False)
        self.txtID.setAlignment(QtCore.Qt.AlignCenter)
        self.txtID.setObjectName("txtID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtID)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtAd = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtAd.setText("")
        self.txtAd.setAlignment(QtCore.Qt.AlignCenter)
        self.txtAd.setObjectName("txtAd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtAd)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spnStok = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnStok.setAlignment(QtCore.Qt.AlignCenter)
        self.spnStok.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnStok.setMaximum(999999999)
        self.spnStok.setObjectName("spnStok")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spnStok)
        self.btnKaydet = QtWidgets.QPushButton(self.groupBox)
        self.btnKaydet.setGeometry(QtCore.QRect(144, 220, 131, 33))
        self.btnKaydet.setObjectName("btnKaydet")
        self.btnSil = QtWidgets.QPushButton(self.groupBox)
        self.btnSil.setGeometry(QtCore.QRect(144, 257, 131, 33))
        self.btnSil.setObjectName("btnSil")
        self.btnYeni = QtWidgets.QPushButton(self.groupBox)
        self.btnYeni.setGeometry(QtCore.QRect(10, 220, 131, 71))
        self.btnYeni.setObjectName("btnYeni")
        self.lblBilgi = QtWidgets.QLabel(self.groupBox)
        self.lblBilgi.setGeometry(QtCore.QRect(20, 310, 251, 121))
        self.lblBilgi.setObjectName("lblBilgi")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 10, 401, 441))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.listUrunler = QtWidgets.QListWidget(self.groupBox_2)
        self.listUrunler.setGeometry(QtCore.QRect(10, 70, 381, 361))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.listUrunler.setFont(font)
        self.listUrunler.setObjectName("listUrunler")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 381, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtAra = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txtAra.setObjectName("txtAra")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtAra)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.txtAra.textChanged['QString'].connect(self.arama)
        self.btnYeni.clicked.connect(self.yeni)
        self.btnSil.clicked.connect(self.sil)
        self.btnKaydet.clicked.connect(self.kaydet)
        self.listUrunler.itemClicked['QListWidgetItem*'].connect(self.secim)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        tabloOlustur = """CREATE TABLE IF NOT EXISTS urunler (
	                        id	INTEGER UNIQUE,
	                        ad	TEXT UNIQUE,
	                        stok	INTEGER,
	                        PRIMARY KEY(id AUTOINCREMENT)
                        );"""
        self.vt  = sql.connect('./urunler.db')
        self.cur = self.vt.cursor()
        try:
            self.cur.execute(tabloOlustur)
        except:
            pass
        
        self.listele()
        self.sonuncuyuSec()
        self.secimID = 0

    def sonuncuyuSec(self):
        try:
            self.secimID = self.urunler[-1][0]
            self.txtID.setText(str(self.urunler[-1][0]))
            self.txtAd.setText(str(self.urunler[-1][1]))
            self.spnStok.setValue(self.urunler[-1][2])
            self.yeniKayit = False
        except:
            self.yeni()

    def listele(self):
        self.cur.execute("SELECT * FROM urunler ORDER BY id ASC;")
        self.urunler = self.cur.fetchall()
        self.listUrunler.clear()
        for urun in self.urunler:
            self.listUrunler.addItem("{} | {} | {}".format(urun[0],urun[1],urun[2]))
        try:
            self.lblBilgi.setText("Toplam Ürün : "+str(len(self.urunler))+"\n"
"Son Ürün;\n"
"ID : "+str(self.urunler[-1][0])+"\n"
"Ad : "+str(self.urunler[-1][1])+"\n"
"STOK : "+str(self.urunler[-1][2])+"")
        except:
            self.lblBilgi.setText("Toplam Ürün : 0\n"
"Son Ürün;\n"
"ID : -\n"
"Ad : -\n"
"STOK : -")

        
    def arama(self,kelime):
        sorgu = "SELECT * FROM urunler WHERE (ad LIKE '%{}%')".format(kelime)
        if(kelime.isnumeric()):
            sorgu = sorgu + "OR id={}".format(kelime)
        self.cur.execute(sorgu)
        self.urunler = self.cur.fetchall()
        self.listUrunler.clear()
        for urun in self.urunler:
            self.listUrunler.addItem("{} | {} | {}".format(urun[0],urun[1],urun[2]))

    def yeni(self):
        self.cur.execute("select seq from sqlite_sequence where name='urunler'")
        sonID = int(self.cur.fetchall()[0][0])+1
        self.txtID.setText(str(sonID))
        self.txtAd.setText("")
        self.spnStok.setValue(0)
        self.yeniKayit = True

    def kaydet(self):
        if(self.yeniKayit):
            self.cur.execute("INSERT INTO urunler (id,ad,stok) VALUES ({},'{}',{})".format(self.txtID.text(),self.txtAd.text(),self.spnStok.value()))
            self.vt.commit()
            self.listele()
            self.sonuncuyuSec()
        else:
            self.cur.execute("UPDATE urunler SET ad='{}',stok={} WHERE id={}".format(self.txtAd.text(),str(self.spnStok.value()),self.txtID.text()))
            self.vt.commit()
            self.listele()

    def sil(self):
        self.cur.execute("DELETE FROM urunler WHERE id={}".format(self.secimID))
        self.vt.commit()
        self.listele()
        self.sonuncuyuSec()
        
    def secim(self,item):
        self.secimID = item.text().split(" ")[0]
        self.cur.execute("SELECT * FROM urunler WHERE id={}".format(self.secimID))
        idd, ad, stok = self.cur.fetchone()
        self.txtID.setText(str(idd))
        self.txtAd.setText(str(ad))
        self.spnStok.setValue(stok)
        self.yeniKayit = False
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stok Takip"))
        self.groupBox.setTitle(_translate("MainWindow", "Ürün"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.txtID.setText(_translate("MainWindow", "000"))
        self.label_2.setText(_translate("MainWindow", "ÜRÜN ADI"))
        self.label_3.setText(_translate("MainWindow", "STOK"))
        self.btnKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.btnSil.setText(_translate("MainWindow", "Sil"))
        self.btnYeni.setText(_translate("MainWindow", "Yeni"))
        self.lblBilgi.setText(_translate("MainWindow", "Toplam Ürün : \n"
"Son Ürün;\n"
"ID : 000\n"
"Ad : TEST\n"
"STOK : 0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ürünler"))
        self.label_4.setText(_translate("MainWindow", "Ara"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
