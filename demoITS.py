from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes  # An included library with Python install.
from NhanDang import NhanDang
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import pyodbc
import datetime
from PyQt5.Qt import QTableWidgetItem, QAbstractItemView
class Ui_MainWindow(object):
    def Mbox(self,title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(10, 80, 550, 380))
        self.groupBox1.setTitle("")
        self.groupBox1.setObjectName("groupBox1")
        self.label_Hinh = QtWidgets.QLabel(self.groupBox1)
        self.label_Hinh.setGeometry(QtCore.QRect(0, 0, 550, 380))
        self.label_Hinh.setText("")
        self.label_Hinh.setPixmap(QtGui.QPixmap(""))
        self.label_Hinh.setScaledContents(True)
        self.label_Hinh.setObjectName("label_Hinh")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(600, 72, 550, 391))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_BienSo = QtWidgets.QLabel(self.groupBox)
        self.label_BienSo.setGeometry(QtCore.QRect(40, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_BienSo.setFont(font)
        self.label_BienSo.setObjectName("label_BienSo")
        self.textEdit_BienSo = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_BienSo.setGeometry(QtCore.QRect(160, 40, 351, 31))
        self.textEdit_BienSo.setObjectName("textEdit_BienSo")
        self.label_Ten = QtWidgets.QLabel(self.groupBox)
        self.label_Ten.setGeometry(QtCore.QRect(40, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_Ten.setFont(font)
        self.label_Ten.setObjectName("label_Ten")
        self.textEdit_Ten = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Ten.setGeometry(QtCore.QRect(160, 90, 351, 31))
        self.textEdit_Ten.setObjectName("textEdit_Ten")
        self.textEdit_Ngay = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Ngay.setGeometry(QtCore.QRect(160, 140, 351, 31))
        self.textEdit_Ngay.setObjectName("textEdit_Ngay")
        self.label_Ngay = QtWidgets.QLabel(self.groupBox)
        self.label_Ngay.setGeometry(QtCore.QRect(40, 143, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_Ngay.setFont(font)
        self.label_Ngay.setObjectName("label_Ngay")
        self.textEdit_Gio = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Gio.setGeometry(QtCore.QRect(160, 190, 351, 31))
        self.textEdit_Gio.setObjectName("textEdit_Gio")
        self.label_Gio = QtWidgets.QLabel(self.groupBox)
        self.label_Gio.setGeometry(QtCore.QRect(40, 200, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_Gio.setFont(font)
        self.label_Gio.setObjectName("label_Gio")
        self.textEdit_LoaiXe = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_LoaiXe.setGeometry(QtCore.QRect(160, 240, 351, 31))
        self.textEdit_LoaiXe.setObjectName("textEdit_LoaiXe")
        self.label_LoaiXe = QtWidgets.QLabel(self.groupBox)
        self.label_LoaiXe.setGeometry(QtCore.QRect(40, 250, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_LoaiXe.setFont(font)
        self.label_LoaiXe.setObjectName("label_LoaiXe")
        self.textEdit_DiaChi = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_DiaChi.setGeometry(QtCore.QRect(160, 290, 351, 31))
        self.textEdit_DiaChi.setObjectName("textEdit_DiaChi")
        self.label_DiaChi = QtWidgets.QLabel(self.groupBox)
        self.label_DiaChi.setGeometry(QtCore.QRect(40, 300, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_DiaChi.setFont(font)
        self.label_DiaChi.setObjectName("label_DiaChi")
        self.textEdit_TrangThai = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_TrangThai.setGeometry(QtCore.QRect(160, 340, 351, 31))
        self.textEdit_TrangThai.setReadOnly(True)
        self.textEdit_TrangThai.setObjectName("textEdit_TrangThai")
        self.label_TrangThai = QtWidgets.QLabel(self.groupBox)
        self.label_TrangThai.setGeometry(QtCore.QRect(40, 343, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_TrangThai.setFont(font)
        self.label_TrangThai.setObjectName("label_TrangThai")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(600, 480, 551, 71))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnXemDanhSach = QtWidgets.QPushButton(self.groupBox_2)
        self.btnXemDanhSach.setGeometry(QtCore.QRect(20, 20, 120, 30))
        self.btnXemDanhSach.setObjectName("btnXemDanhSach")
        self.btnXoa = QtWidgets.QPushButton(self.groupBox_2)
        self.btnXoa.setGeometry(QtCore.QRect(280, 20, 120, 30))
        self.btnXoa.setObjectName("btnXoa")
        self.btnsearchKiem = QtWidgets.QPushButton(self.groupBox_2)
        self.btnsearchKiem.setGeometry(QtCore.QRect(410, 20, 120, 30))
        self.btnsearchKiem.setObjectName("btnsearch")
        self.btnThem = QtWidgets.QPushButton(self.groupBox_2)
        self.btnThem.setGeometry(QtCore.QRect(150, 20, 120, 30))
        self.btnThem.setObjectName("btnThem")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 570, 1141, 271))
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(181)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(47)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(14)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 480, 551, 71))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnVideo = QtWidgets.QPushButton(self.groupBox_3)
        self.btnVideo.setGeometry(QtCore.QRect(20, 20, 120, 30))
        self.btnVideo.setObjectName("btnVideo")
        self.btnChupAnh = QtWidgets.QPushButton(self.groupBox_3)
        self.btnChupAnh.setGeometry(QtCore.QRect(220, 20, 120, 30))
        self.btnChupAnh.setAutoFillBackground(False)
        self.btnChupAnh.setObjectName("btnChupAnh")
        self.btnNhanDang = QtWidgets.QPushButton(self.groupBox_3)
        self.btnNhanDang.setGeometry(QtCore.QRect(410, 20, 120, 30))
        self.btnNhanDang.setObjectName("btnNhanDang")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnNhanDang.clicked.connect(self.nhandang)
        self.btnXemDanhSach.clicked.connect(self.loadData)
        self.btnThem.clicked.connect(self.upData)
        self.btnXoa.clicked.connect(self.deledata)
        self.btnsearchKiem.clicked.connect(self.search)
        self.tableWidget.clicked.connect(self.on_Click)
        self.btnChupAnh.clicked.connect(self.chupHinh1)
        self.btnVideo.clicked.connect(self.video)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Thong Tin Xe"))
        self.label_BienSo.setText(_translate("MainWindow", "Bien So:"))
        self.label_Ten.setText(_translate("MainWindow", "Ten:"))
        self.label_Ngay.setText(_translate("MainWindow", "Ngay:"))
        self.label_Gio.setText(_translate("MainWindow", "Gio: "))
        self.label_LoaiXe.setText(_translate("MainWindow", "Loai Xe:"))
        self.label_DiaChi.setText(_translate("MainWindow", "Dia Chi:"))
        self.label_TrangThai.setText(_translate("MainWindow", "Trang Thai"))
        self.btnXemDanhSach.setText(_translate("MainWindow", "Xem danh sach"))
        self.btnXoa.setText(_translate("MainWindow", "Xoa"))
        self.btnsearchKiem.setText(_translate("MainWindow", "Tim Kiem"))
        self.btnThem.setText(_translate("MainWindow", "Them"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bien So"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ten"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngay"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gio"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Loai Xe"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dia Chi"))
        self.btnVideo.setText(_translate("MainWindow", "Video"))
        self.btnChupAnh.setText(_translate("MainWindow", "Chup Anh"))
        self.btnNhanDang.setText(_translate("MainWindow", "Nhan Dang"))
        self.label.setText(_translate("MainWindow", "NHAN DIEN BANG SO XE"))
    def chupHinh1(self):
        a = NhanDang()
        b = a.takePhoto()
        self.label_Hinh.setPixmap(QtGui.QPixmap(r"E:\S5\CD_HeThongGiaoThongTM\BTL\license-plate-recognition-master\license-plate-recognition\Cropped Images-Text\fileXuLy.png"))
        c = a.xuly(r"E:\S5\CD_HeThongGiaoThongTM\BTL\license-plate-recognition-master\license-plate-recognition\Cropped Images-Text\fileXuLy.png")
        self.textEdit_BienSo.setText(c)
        if self.exist() == 1:
            self.textEdit_Ten.setText("Đã Đăng Ký")
        else:   
            self.textEdit_Ten.setText("Không xác định")
            self.textEdit_DiaChi.setText("Không xác định")
            self.textEdit_LoaiXe.setText("Không xác định")
        
        self.loadTime()
    def video(self):
        a = NhanDang()
        b=  a.chuongTrinhNhanDienXe()
 

    def nhandang(self):
        self.textEdit_BienSo.setText("")
        self.textEdit_Ten.setText("")
        self.textEdit_Ngay.setText("")
        self.textEdit_Gio.setText("")
        self.textEdit_DiaChi.setText("")
        self.textEdit_LoaiXe.setText("")
        hinh1 = ""
        a = NhanDang()
        hinh1 = self.browser()
        if(len(hinh1)==0):
            return
        else:
            b = a.xuly1(hinh1)
            if(type(b)==type(None)):
                self.Mbox('Error','Không nhận diện được biển số xe',1)
                return
            if(len(b)<6):
                self.Mbox('Error', 'Không nhận diện được biển số xe', 1)
                return
            b=b.replace(' ','')
            self.textEdit_BienSo.setText(b)
            data = self.exist();
            print(data)
            print(type(data))
            if len(data) > 0:
                self.textEdit_Ten.setText(data[1])
                self.textEdit_Ngay.setText(data[2])
                self.textEdit_Ngay.setText(data[3])
                self.textEdit_DiaChi.setText(data[4])
                self.textEdit_LoaiXe.setText(data[5])
                self.textEdit_TrangThai.setText("Đã đăng ký")
            else:
                self.textEdit_Ten.setText("Không xác định")
                self.textEdit_DiaChi.setText(self.PhanLoai(str(b[0:2])))
                self.textEdit_LoaiXe.setText("Không xác định")
                self.textEdit_TrangThai.setText("Chưa đăng ký")
            self.loadTime()


    def PhanLoai(self,x):
        switcher={
            '11': 'Cao Bang',
            '12': 'Lang Son',
            '14': 'Quang Ninh',
            '15': 'Hai Phong',
            '16': 'Hai Phong',
            '17':'Thai Binh',
            '18':'Nam Dinh',
            '19':'Phu Tho',
            '20':'Thai Nguyen',
            '21':'Yen Bai',
            '23':'Ha Giang',
            '24':'Lao Cai',
            '25':'Lai Lai',
            '26':'Son La',
            '27':'Đien Bien',
            '28':'Hòa Bình',
            '29':'Ha Noi',
            '30':'Ha Noi',
            '31':'Ha Noi',
            '32':'Ha Noi',
            '33':'Ha Noi',
            '34':'Hải Dương',
            '35':'Ninh Bình',
            '36':'Thanh Hóa',
            '37':'Nghệ An',
            '38':'Hà Tĩnh',
            '43':'Đà Nẵng',

            '47':'Đắk Lắk',
            '48':'Đắk Nông',
            '49':'Lâm Đồng',
            '50':'Hồ Chí Minh',
            '51': 'Hồ Chí Minh',
            '52': 'Hồ Chí Minh',
            '53': 'Hồ Chí Minh',
            '54': 'Hồ Chí Minh',
            '55': 'Hồ Chí Minh',
            '56': 'Hồ Chí Minh',
            '57': 'Hồ Chí Minh',
            '58': 'Hồ Chí Minh',
            '59': 'Hồ Chí Minh',
            '60':'Đồng Nai',
            '61':'Bình Dương',
            '62':'Long An',
            '63':'Tiền Giang',
            '64':'Vĩnh Long',
            '65':'Cần Thơ',
            '66':'Đồng Tháp',
            '67':'An Giang',
            '68':'Kiên Giang',
            '69':'Cà Mau',
            '70':'Tây Ninh',
            '71':'Bến Tre',
            '72':'Bà Rịa – Vũng Tàu',
            '73':'Quảng Bình',
            '74':'Quảng Trị',
            '75':'Huế',
            '76':'Quảng Ngãi',

            '77':'Bình Định',
            '78':'Phú Yên',
            '79':'Khánh Hòa',
            '80':'Các đơn vị kinh tế thuộc TW (hàng không)',
            '81':'Gia Lai',
            '82':'Kon Tum',
            '83':'Sóc Trăng',
            '84':'Trà Vinh',
            '85':'Ninh Thuận',
            '86':'Bình Thuận',
            '88':'Vĩnh Phúc',
            '89':'Hưng Yên',
            '90':'Hà Nam',
            '92':'Quảng Nam',
            '93':'Bình Phước',
            '94':'Bạc Liêu',
            '95':'Hậu Giang',
            '97':'Bắc Cạn',
            '98':'Bắc Giang',
            '99':'Bắc Ninh',
        }
        return switcher.get(x, "Không xác định")
    def loadTime(self):
        DateTime = datetime.datetime.now()
        self.textEdit_Ngay.setText('%s-%s-%s'%(DateTime.year,DateTime.month,DateTime.day))
        self.textEdit_Gio.setText('%s:%s:%s'%(DateTime.hour,DateTime.minute,DateTime.second))

    def loadData(self):
        SQL_STATEMENT = 'SELECT * FROM dbo.BienSo'
        SERVER_NAME = "LAPTOP-CD3OO2KS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute(SQL_STATEMENT)
        self.tableWidget.setRowCount(0)
        for row_number, rown_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number , data in enumerate(rown_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
    def upData(self):
        SERVER_NAME = "LAPTOP-CD3OO2KS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        bienso=self.textEdit_BienSo.toPlainText().replace(' ','');
        ten=self.textEdit_Ten.toPlainText();
        ngay=format(datetime.datetime.now().date())
        gio=format(datetime.datetime.now().time())
        diachi=self.textEdit_DiaChi.toPlainText()
        loaixe=self.textEdit_LoaiXe.toPlainText();

        result = cursor.execute('INSERT INTO dbo.BienSo ( BienSo ,Ten ,Ngay ,Gio ,DiaChi ,LoaiXe) VALUES  (?,?,?,?,?,?)',
                                (bienso,ten,ngay,gio,diachi,loaixe)
            )
        conn.commit()
        self.loadData()

        a = NhanDang()
        a.luuAnh(self.textEdit_Ten.toPlainText())

    def deledata(self):
        SERVER_NAME = "LAPTOP-CD3OO2KS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute("DELETE FROM dbo.BienSo WHERE BienSo=?",(self.textEdit_BienSo.toPlainText())    )
        conn.commit()
        a = NhanDang()
        b = a.xoaAnh(self.textEdit_Ten.toPlainText())
        self.loadData()
    def search(self):
        SERVER_NAME = "LAPTOP-CD3OO2KS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute(" SELECT * FROM dbo.BienSo WHERE BienSo=?",(self.textEdit_BienSo.toPlainText()))
        #conn.commit()
        self.tableWidget.setRowCount(0)
        for row_number, rown_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number , data in enumerate(rown_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))

    def exist(self):
        SERVER_NAME = "LAPTOP-CD3OO2KS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        cursor.execute(" SELECT * FROM dbo.BienSo WHERE BienSo=?",(self.textEdit_BienSo.toPlainText()))
        result_set = cursor.fetchall()
        data=[]
        for row in result_set:
            for column in row:
                    data.append(column)
        return data

    def  on_Click(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        ax = (self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows))
        indexes = self.tableWidget.selectionModel().selectedRows()
        for index1 in sorted(indexes):
            self.textEdit_BienSo.setText(index1.sibling(index1.row(),0).data())
            self.textEdit_Ten.setText(index1.sibling(index1.row(),1).data())
            self.textEdit_Ngay.setText(index1.sibling(index1.row(),2).data())
            self.textEdit_Gio.setText(index1.sibling(index1.row(),3).data())
            self.textEdit_DiaChi.setText(index1.sibling(index1.row(),4).data())
            self.textEdit_LoaiXe.setText(index1.sibling(index1.row(),5).data())

    def browser(self):
        try:
            file_name,_ = QFileDialog.getOpenFileName(None,"Open Image File",r"CarImages")
            self.label_Hinh.setPixmap(QtGui.QPixmap(file_name))
        except:
            file_name=""

        return file_name


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


