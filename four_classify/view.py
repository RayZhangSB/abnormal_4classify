# coding:utf-8
#2018.3.5
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from view_design import Ui_Form
import os
from utils import setPicture

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class mywindow(QWidget,Ui_Form):
    def __init__(self):
        #界面初始化．start
        super(_windowdow, self).__init__()
        self.setupUi(self)
        self.showFullScreen()
        W = self.width()
        H = self.height()
        self.video.setFixedWidth(int(0.75*W))#视频
        self.video.setFixedHeight(int(195*H/231.0))
        self.video.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.Rectlabel1.setGeometry(int(489*W/1366.0),int(274*H/768.0),int(399*W/1366.0),int(168*H/768.0))
        self.Rectlabel2.setGeometry(int(482*W/1366.0),int(110*H/768.0),int(110*W/1366.0),int(139*H/768.0))
        self.Rectlabel3.setGeometry(int(616* W / 1366.0), int(73 * H / 768.0), int(120 * W / 1366.0),
                                    int(120 * H / 768.0))
        self.ABSPATH = str(os.getcwd())
        log1 = QImage()
        log1.load(os.path.join(self.ABSPATH, '_images/log1.png'))
        setPicture(self.logo1, QPixmap.fromImage(log1))
        log2 = QImage()
        log2.load(os.path.join(self.ABSPATH, '_images/log2.png'))
        setPicture(self.logo2, QPixmap.fromImage(log2))
        pa = QPalette()
        pa.setColor(QPalette.Background, Qt.black)
        self.setPalette(pa)
        ##界面初始化．end


