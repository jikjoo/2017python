import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from check_mword import *
from ParvisLib import *

class XWindow(Ui_check_mword):
    def __init__(self,window):
        Ui_check_mword.__init__(self)
        self.setupUi(window)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    dialog = QDialog()
    main_window = XWindow(dialog)
    dialog.show()
    app.exec_()
