# coding:utf-8
# 2018.3.5
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pojo import POJO
import os
import utils
import cv2
import socket
import numpy as np
from configuration import ConfigInjection
from threading import Event, Thread
import time
from caculate_handler import CaculateHandler

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


# 用于控制处理流程，获取到_windowdow的一个实例以控制
class MonitorController():
    def __init__(self, _window):
        self._window = _window
        self._window.connect(self._window.start, SIGNAL("clicked()"), self.start_spy)
        self._window.connect(self._window.logout, SIGNAL("clicked()"), self.close_window)
        self.load_config()  # 加载配置文件
        self.load_socket_config()
        self._cap = cv2.VideoCapture(self.streamAddr)  # self.config.streamAddr

        self._abnormal_type = ["\n明火识别", "\n煤粉、煤灰\n 或粉尘识别", "\n液体(水、油) \n识别", "\n气体、蒸汽 \n识别", "\n无异常"]
        self._abnormal_index = 4

        self._main_timer = QTimer()
        self._main_timer.timeout.connect(self.monitor)  # slot 与槽链接(main)
        self._warning_timer = QTimer()
        self._warning_timer.timeout.connect(self.warning)  # 预警闪烁功能

        self._abnormal_labels = [self._window.ablabel1, self._window.ablabel2]  # 异常图片显示框初始化
        self._abnormal_pics = [None, None]  # 异常图片对象初始化
        self.ABSPATH = str(os.getcwd())
        self._pic_save_path = os.path.join(self.ABSPATH, 'save')
        if not os.path.exists(self._pic_save_path):
            os.mkdir(self._pic_save_path)

        self.eles_init()
        self._notify_event = Event()
        self._send_thread = Thread(target=self.send_msg)
        self._send_thread.setDaemon(True)
        self._send_thread.start()

    # 执行程序的主入口
    def start_spy(self):
        self._main_timer.start(40)

        if self._click_flag:
            self._window.start.setText(_translate("Form", "Pause", None))
            self._click_flag = not self._click_flag
        else:
            self._window.start.setText(_translate("Form", "Start", None))
            self._click_flag = not self._click_flag
            self._main_timer.stop()
            
    def monitor(self):
        success, image = self.cap.read()
        if not self.cap.isOpened():
            self.cap = cv2.Videocapture(self.streamAddr)
            success, image = self.cap.read()
        if image != None:
            image_copy = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if success:
            self._cnt += 1
            if self._cnt == 10:
                self._handler.baseImg.append(image_copy)
            self._handler.add_diff_value(image_copy)
            # self._handler.add_candidate_img(image_copy)
            # cv2.rectangle(image, (480, 360), (1440, 900), (255, 0, 0))
            show_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
            photo = QPixmap.fromImage(show_img)
            self._images.append(photo)
            n = len(self._images)
            if n >= 9:
                tmp = self._images[n - 9:n]  # 优化缓存qpixmap的list
                del self._images
                self._images = tmp

            if len(self._images) >= 9:
                flag, self._abnormal_rois ,self._draw_index= self._handler.hasAbnormal()
                if flag or self._is_real_normal:
                    if self._cnt_flag < 8:
                        self._handler.check_bg(image_copy)
                        self._is_real_normal = True
                        self._cnt_flag += 1
                    else:
                        self._is_real_normal = False
                        print "现在可能有异常了，前面的处理完了没－－"
                        ab_pixmap = self._images[4]
                        updated_candidate = self._handler.img_to_candidate()
                        self._cnt_flag = 0

                        if self._step2_processed:  # second process finish
                            print "可以处理新的数据了--------"
                            if self._handler.candidate_valid():
                                self._step2_processed = False
                                if updated_candidate:
                                    self._handler.saveImg(self._cnt)
                                self._buffers[0] = POJO(ab_pixmap, self._handler.get_candidate())

                                self._notify_event.set()
                            else:
                                print "没有被判定可用的图像－－"
                        else:
                            print "还没处理完，你再等会儿－－－－"

            utils.set_label_pic(self._window.video, photo)
            if self._updated_abnormal_pic:
                self._updated_abnormal_pic = False
                self.update_show()
            else:
                self._warning_timer.stop()
        else:
            self.cap.release()

    def load_config(self):
        self.config = configInjection()  # 加载配置文件获取流地址＝＝
        self.config.load_configuration()
        self.streamAddr = self.config.streamAddr

    def load_socket_config(self):
        address = (self.config.address, self.config.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(address)

    # 更新异常图片显示
    def update_show(self):
        for i in range(2):
            if self._abnormal_pics[i] != None:
                utils.set_label_pic(self._abnormal_labels[i], self._abnormal_pics[i])
        # 更新文本显示self._window.ablabel3
        self._window.ablabel3.setText(_translate("Form",
                                               self._abnormal_type[self._abnormal_index], None))
        # self._warning_timer.start(500)

    # 一些成员变量初始化设置
    def eles_init(self):
        self._images = []
        self._step2_processed = True  # 第二步做完的标志
        self._pojo_changed = False
        self._click_flag = False  # 用于改变开始键的文本变化
        self._vals = []  # 用于存储每张图片处理输出值
        self._buffers = []
        self._buffers.append(None)
        self._handler = CaculateHandler(self.config)  # 第一步图像处理器对象
        self._cnt = 0
        self._abnormal_rois = None
        self._updated_abnormal_pic = False
        self._is_real_normal = False
        self._cnt_flag = 0
        self._draw_index = 0

    def warning(self):
        if self._window.ablabel3.styleSheet().isEmpty():
            self._window.ablabel3.setStyleSheet(_fromUtf8("border:5px solid red;"))
        else:
            self._window.ablabel3.setStyleSheet(_fromUtf8(""))

    def send_msg(self):
        while True:
            self._notify_event.wait()
            print "我要开始处理啦-----"
            self._pojo_changed = False
            self._save_obj = self._buffers[0]

            # 向服务器端发送图片
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, img_encode = cv2.imencode('.jpg', self._save_obj.img, encode_param)
            data = np.array(img_encode)
            send_data = data.tostring()

            self.sock.send(str(len(send_data)).ljust(16))
            self.sock.send(send_data)
            # 发送相应的问题roi区域标记
            if len(self._abnormal_rois) == 0:
                for j in range(16):
                    self._abnormal_rois.append(j)
            list = [str(i) for i in self._abnormal_rois]
            tmp_str = ",".join(list)  # "1,2,3,4"
            self.sock.sendall(str(len(tmp_str)).ljust(16))
            self.sock.send(tmp_str)
            self.rece_msg()

        print "数据发送失败，请重新开始发送"
        self.sock.close()

    def rece_msg(self):
        ss = self.sock.recv(32)
        print "返回的结果－－－", ss
        rec_data=str(ss).split("/")
        index = int(rec_data[1])
        if 4 != index:
            self._abnormal_index = index
            #utils.update_list(self._abnormal_pics, self._save_obj.ab_pixmap)  # 更新异常列表
            draws = rec_data[2:]
            draws = [int(i) for i in draws]
            print "需要画出的区域有－－",draws
            utils.update_list(self._abnormal_pics, self._handler.recs_draw(draws,self._save_obj.img))
            self._updated_abnormal_pic = True
        else:
            self._updated_abnormal_pic = False
        self._step2_processed = True
        self._notify_event.clear()

    def checkIsBackGround(self):
        self._handler.check_bg()
        self.postImgs = []

    # window close
    def close_window(self):
        self.sock.close()
        self._main_timer.stop()
        self._window.close()

