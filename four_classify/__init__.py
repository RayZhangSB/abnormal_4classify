# coding:utf-8
#2018.3.5
from PyQt4.QtGui import *

from monitor import MonitorController
from view import mywindow
import sys


def main():
    app = QApplication(sys.argv)
    window = mywindow()
    MonitorController(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
