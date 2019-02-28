
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_mword(object):
    def setupUi(self, check_mword):
        check_mword.setObjectName("check_mword")
        check_mword.setMaximumSize(QtCore.QSize(150, 200))
        self.horizontalLayout = QtWidgets.QHBoxLayout(check_mword)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(check_mword)
        self.scrollArea.setMinimumSize(QtCore.QSize(1, 1))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 123, 168))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(check_mword)
        QtCore.QMetaObject.connectSlotsByName(check_mword)

    def retranslateUi(self, check_mword):
        _translate = QtCore.QCoreApplication.translate
        check_mword.setWindowTitle(_translate("check_mword", "Form"))


