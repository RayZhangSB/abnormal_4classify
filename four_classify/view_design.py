# -*- coding: utf-8 -*-

#

from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPalette, QFont

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1700,1080)
       #
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.start = QtGui.QPushButton(Form)
        self.start.setObjectName(_fromUtf8("start"))
        self.start.setStyleSheet(_fromUtf8("border:2px solid gray;""font: 11pt;""border-radius:10px;""color:white"))
        self.start.setSizePolicy(sizePolicy)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet(_fromUtf8("border:2px solid gray;""font: 11pt;""border-radius:10px;""color:white"))
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_3 = QtGui.QPushButton(Form)
       
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet(_fromUtf8("border:2px solid gray;""font: 11pt;""border-radius:10px;""color:white"))
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet(_fromUtf8("border:2px solid gray;""font: 11pt;""border-radius:10px;""color:white"))
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet(_fromUtf8("border:2px solid gray;""font: 10pt;""border-radius:10px;""color:white"))
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.logoff = QtGui.QPushButton(Form)
        self.logoff.setObjectName(_fromUtf8("logoff"))
        self.logoff.setStyleSheet(_fromUtf8("border:2px solid gray;""font: 11pt;""border-radius:10px;"
                                                  "color:white"))
        self.logoff.setSizePolicy(sizePolicy)
        self.logo1 = QtGui.QLabel(Form)
        self.logo1.setText(_fromUtf8(""))
        self.logo1.setObjectName(_fromUtf8("logo1"))
        self.logo1.setSizePolicy(sizePolicy)
        self.logo2 = QtGui.QLabel(Form)

        self.logo2.setText(_fromUtf8(""))
        self.logo2.setObjectName(_fromUtf8("logo2"))
        self.logo2.setSizePolicy(sizePolicy)

        self.video = QtGui.QLabel(Form)
        self.video.setScaledContents(True)

        self.video.setText(_fromUtf8(""))
        self.video.setObjectName(_fromUtf8("video"))

        self.ablabel1 = QtGui.QLabel(Form)

        self.ablabel1.setText(_fromUtf8(""))
        self.ablabel1.setObjectName(_fromUtf8("ablabel1"))
        self.ablabel1.setSizePolicy(sizePolicy)

        self.ablabel2 = QtGui.QLabel(Form)

        self.ablabel2.setText(_fromUtf8(""))
        self.ablabel2.setObjectName(_fromUtf8("ablabel2"))
        self.ablabel2.setSizePolicy(sizePolicy)

        self.ablabel3= QtGui.QLabel(Form)
        self.ablabel3.setText(_fromUtf8(""))
        self.ablabel3.setObjectName(_fromUtf8("ablabel3"))
        self.ablabel3.setSizePolicy(sizePolicy)
        self.ablabel3.setText(_translate("Form", " \n无异常　", None))
        self.ablabel3.setAlignment(Qt.AlignHCenter)
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.red)
        self.ablabel3.setPalette(pa)

        ft = QFont()
        ft.setPointSize(35)
        self.ablabel3.setFont(ft)

        self.ablabel4 = QtGui.QLabel(Form)
        self.ablabel4.setObjectName(_fromUtf8("ablabel4"))
        self.ablabel4.setSizePolicy(sizePolicy)

        self.Rectlabel1 = QtGui.QLabel(Form)

        self.Rectlabel1.setObjectName(_fromUtf8("Rectlabel1"))
        self.Rectlabel1.setStyleSheet(_fromUtf8("border:2px solid red;"))
        self.Rectlabel1.hide()
        self.Rectlabel2 = QtGui.QLabel(Form)

        self.Rectlabel2.setObjectName(_fromUtf8("Rectlabel1"))
        self.Rectlabel2.setStyleSheet(_fromUtf8("border:2px solid red;"))
        self.Rectlabel2.hide()
        self.Rectlabel3 = QtGui.QLabel(Form)

        self.Rectlabel3.setObjectName(_fromUtf8("Rectlabel1"))
        self.Rectlabel3.setStyleSheet(_fromUtf8("border:2px solid red;"))
        self.Rectlabel3.hide()
        self.peopleRect = QtGui.QLabel(Form)
        self.peopleRect.setObjectName(_fromUtf8("peopleRect"))


        #布局
        mainLayout = QtGui.QVBoxLayout()#垂直 main沿丨线放东西
        upLayout = QtGui.QHBoxLayout()
        downLayout =QtGui.QHBoxLayout()
        downLayout.addWidget(self.start)
        downLayout.addStretch()
        downLayout.addWidget(self.pushButton_2)
        downLayout.addStretch()
        downLayout.addWidget(self.pushButton_3)
        downLayout.addStretch()
        downLayout.addWidget(self.pushButton_4)
        downLayout.addStretch()
        downLayout.addWidget(self.pushButton_5)
        downLayout.addStretch()
        downLayout.addWidget(self.logoff)

        up_leftLayout = QtGui.QVBoxLayout()
        up_rightLayout = QtGui.QVBoxLayout()
        up_rightLayout.addWidget(self.ablabel4)
        up_rightLayout.addWidget(self.ablabel1)
        up_rightLayout.addWidget(self.ablabel2)
        #
        up_rightLayout.addWidget(self.ablabel3)
        up_rightLayout.setStretchFactor(self.ablabel4, 1)
        up_rightLayout.setStretchFactor(self.ablabel1,4)
        up_rightLayout.setStretchFactor(self.ablabel2, 4)

        up_rightLayout.setStretchFactor(self.ablabel3, 3)

        up_left_upLayout = QtGui.QHBoxLayout()
        up_left_upLayout.addWidget(self.logo1)
        up_left_upLayout.addWidget(self.logo2)
        up_left_upLayout.setStretchFactor(self.logo1,3)
        up_left_upLayout.setStretchFactor(self.logo2,7)
        up_left_upLayout.setSpacing(1)
        up_left_downLayout = QtGui.QHBoxLayout()
        up_left_downLayout.addWidget(self.video)
        up_left_downLayout.addStretch(5)

        up_left_downLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        up_leftLayout.addLayout(up_left_upLayout)
        up_leftLayout.addLayout(up_left_downLayout)
        up_leftLayout.setStretchFactor(up_left_upLayout,1)
        up_leftLayout.setStretchFactor(up_left_downLayout, 10)
        upLayout.addLayout(up_leftLayout)
        upLayout.addLayout(up_rightLayout)
        upLayout.setStretchFactor(up_leftLayout,60)
        upLayout.setStretchFactor(up_rightLayout,45)
        mainLayout.addLayout(upLayout)
        mainLayout.addLayout(downLayout)
        mainLayout.setStretchFactor(upLayout, 18)
        mainLayout.setStretchFactor(downLayout,3)

        Form.setLayout(mainLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.start.setText(_translate("Form", "Start", None))
        self.pushButton_2.setText(_translate("Form", "Admin", None))
        self.pushButton_3.setText(_translate("Form", "StopISAS", None))
        self.pushButton_4.setText(_translate("Form", "Mask", None))
        self.pushButton_5.setText(_translate("Form", "Simulate", None))
        self.logoff.setText(_translate("Form", "Log Off", None))


