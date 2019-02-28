import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from parvis_gui import *
from ParvisLib import *

class XWindow(Ui_MainWindow):
    def __init__(self,window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)
        self.edit_PW.returnPressed.connect(self.login)
        self.edit_ID.returnPressed.connect(self.login)

        self.edit_search.returnPressed.connect(lambda : self.search(self.edit_search.text()))

        self.edit_rsearch.returnPressed.connect(lambda : self.search(self.edit_rsearch.text()))
        self.btn_IPC.clicked.connect(self.equation)

        self.window = window
        self.buttons=[]
        self.mids=[]
        self.checkBox = [[]]
        self.dialogs=[]
        self.uis=[]
        self.w_ids = []
        #15 텔레비전, 16 주변, 17 장치, 18 리모콘, 19 스피커
        self.ipc = {15 : ['A63F 13/338'],16:['H04R 7/18'],17:['G06F 9/00'],18:['F21V 21/15'],19:['G11B','H04']}
        self.explain = {15:['텔레비전 네트워크를 이용하는 것'],
            16:['주변부에 있어서의 것'],
            17:['프로그램제어를 위한 장치, 예. 제어장치(주변장치를 위한 프로그램제어 13/10)'],
            18:['전원동작을 위해 특별히 채용된 것, 예. 리모트콘트롤'], 
            19:['기계적 공진 발생기, 예. 현 또는 타격장치를 사용 하여 그들 음을 전기기계변환기에 의하여 픽업하고 그 전기신호를 다시 처리 또는 증폭하고 그 후 스피커 또는 동등의 장치에 의하여 음으로 변환하는 것',
            '원격제어 또는 원격 측정시스템에서 주국에서 제어 신호를 적용하거나 측정값을 획득하는것으로 선택되는 소망 장치인 종국을 선택적으로 호출하기 위한 배치']}
  

    def login(self):
        userid = self.edit_ID.text()
        userpw = self.edit_PW.text()
        if userid and userpw :
            self.stackedWidget.setCurrentIndex(1)
    
    #search
    def search(self,inp):
        #초기화
        self.buttons=[]
        self.mids = []
        self.checkBox =[[]]
        self.dialogs = []
        self.uis = []
        self.w_ids = []
        #inp은 edit에 있는 텍스트
        word_list = inp.split(' ')
        mwords = MainWord(word_list)
        word_ids = mwords.main_id
        self.stackedWidget.setCurrentIndex(2)
        self.edit_rsearch.setText(inp)
        i=0
        j=0
        k=0
        self.w_ids = self.choose(word_ids)
        #버튼들 추가
        for w_id in self.w_ids:
            self.mids.append(MainID(w_id))
            k = i % 10
            if not k:
                j += 1
            self.buttons += [QPushButton(self.mids[i].main_word)]
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            sizePolicy.setHeightForWidth(self.buttons[i].sizePolicy().hasHeightForWidth())
            self.buttons[i].setSizePolicy(sizePolicy)
            font = QFont()
            font.setFamily("Agency FB")
            font.setPointSize(14)
            self.buttons[i].setFont(font)
            self.buttons[i].setAutoRepeatDelay(300)
            self.layout_mword.addWidget(self.buttons[i],j,i%10)
            i += 1
            frame = QFrame()
            self.layout_mword.addWidget(frame,j,10)
        #검색식 업데이트
        self.equation_IPC()
        self.explain_IPC()
        self.create_check()

    def equation(self):   
        subs=[]
        i=0
        for w_id in self.w_ids:
            subs.append('(')
            subs.append('+'.join(self.mids[i].sub_words))
            subs.append(')')
            if i<len(self.w_ids)-1:
                subs.append('*')
            i+=1
        eq = ''.join(subs)
        self.textBrowser.setText(eq)
        return eq
    
    #IPC 검색식
    def equation_IPC(self):   
        subs=[]
        len_wids = len(self.w_ids)
        for i in range(len_wids):  #main word 당 subs
            subs.append('(')
            subs.append('+'.join(self.mids[i].sub_words))
            subs.append(')')
            subs.append('*')
        subs.append('(') #main word 당 ipc
        for i in range(len_wids):
            j=0
            if i:
                subs.append('+')
            for ipc in self.ipc[self.w_ids[i]]:
                if j:
                    subs.append('+')
                subs.append(ipc)
                j+=1
        subs.append(')')
        eq = ''.join(subs)
        self.textBrowser.setText(eq)
        return eq
    #IPC 설명
    def explain_IPC(self):
        len_wids = len(self.w_ids)
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i) 
        self.tableWidget.setRowCount(0)
        j=0
        for i in range(len_wids):
            k=0
            for ipc in self.ipc[self.w_ids[i]]:
                self.tableWidget.insertRow(j)
                self.tableWidget.setItem(j,0,QTableWidgetItem(ipc))
                self.tableWidget.setItem(j,1,QTableWidgetItem(self.explain[self.w_ids[i]][k]))
                j+=1
                k+=1
    def choose(self,word_ids=[]):
        w_ids=[]
        for word_id in word_ids:
            if len(word_id) ==1:
                w_ids.append(word_id[0])
            elif len(word_id) > 1:
                w_ids.append(word_id[0])
            else :
                w_ids.append('')
        return w_ids

    def open_check(self):
        sender = self.window.sender()
        for i in range(len(self.w_ids)):
            if sender == self.buttons[i]:
                button = self.buttons[i]
                dialog = self.dialogs[i]
                break
        x_pos = button.x()
        y_pos = button.y()
        dx = button.width()
        dy = button.height()    
        dialog.move(button.rect().bottomLeft())
        dialog.show()
        subs = self.mids[i].sub_words
        for j in range(len(subs)):
            self.checkBox[i][j].stateChanged.connect(lambda : self.change_check(i))
        
    def change_check(self, i):
        sender = self.window.sender()
        subs = self.mids[i].sub_words
        for j in range(len(subs)):
            if sender == self.checkBox[i][j]:
                checkBox = self.checkBox[i][j]
                break
        print(sender)
        if checkBox.isChecked():
            self.mids[i].sub_words.append(sender.text())
        else:
            self.mids[i].sub_words.remove(sender.text())
        self.equation()

    def create_check(self):
        for i in range(len(self.w_ids)):
            mid = self.mids[i]
            subs = mid.sub_words
            _translate = QtCore.QCoreApplication.translate

            self.dialogs.append(QDialog())
            dialog = self.dialogs[i]
            self.uis.append(Ui_check_mword())
            ui = self.uis[i]
            ui.setupUi(dialog)
            self.checkBox.append([])
            for j in range(len(subs)):
                self.checkBox[i].append(QCheckBox(ui.scrollAreaWidgetContents))
                self.checkBox[i][j].setChecked(True)
                self.checkBox[i][j].setObjectName(subs[j])
                self.checkBox[i][j].setText(_translate("check_mword", subs[j]))
                ui.verticalLayout.addWidget(self.checkBox[i][j])
            self.buttons[i].clicked.connect(self.open_check)
      
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = QMainWindow()
    main_dialog = XWindow(window)
    window.show()
    app.exec_()
