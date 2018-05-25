# coding:utf-8

from PyQt4.QtGui import QPixmap, QImage

import process
import utils
import matplotlib.pyplot as plt
import cv2


class CaculateHandler():
    def __init__(self, config_):
        self._roi_flag = False
        self._part_diff_values = []
        for i in range(16):
            self._part_diff_values.append([])  
        self._processed_img_num = 0
        self.config = config_
        self.ROIs = self.config.rois
        self._base_img = []
        self.clear_candidate()
        self.clear_mark()

    def add_diff_value(self, img):
        for i in range(16):
            self._part_diff_values[i].append(process.pro(img, self.ROIs[0][i]))
            n = len(self._part_diff_values[i])
            if n >= 9:
                tmp = self._part_diff_values[i][n - 9:n]  
                self._part_diff_values[i] = []
                self._part_diff_values[i] = tmp

    def has_abnormal(self):
        abnormal_rois = []
        maxV  = 0
        index = 0
        for i in range(16):
            dif = utils.get_diff_value(4, self._part_diff_values[i])
            if (dif > 20):
                abnormal_rois.append(i)
            if dif>maxV:
                maxV = dif
                index = i


        if len(abnormal_rois) >2:
            self._roi_flag = True
        else:
            self._roi_flag = False

        return self._roi_flag, abnormal_rois,index

    def add_candidate_img(self, img):
        utils.update_list(self._candidate_img, img)

    def save_img(self, img):
        cv2.imwrite("./save/" + str(self._processed_img_num) + ".jpg", img)
        self._processed_img_num += 1

    def img_to_candidate(self):
        image = self._mark_img
        if image != None:
            value = process.process4(image, self._base_img[0])
            if self._better_value == 0:
                self._better_img = image
                self.clear_mark()
                return True
            else:
                if value > self._better_value:
                    self._better_value = value
                    self._better_img = image
                    return True
                self.clear_mark()
                return False
        else:
            return False

    def get_candidate(self):
        res = self._better_img.copy()
        self.clear_candidate()
        return res

    def clear_candidate(self):
        self._better_value = 0
        self._better_img = None

    def candidate_valid(self):
        return self._better_img != None

    def save_img(self, cnt):
        cv2.imwrite("./save/" + str(cnt) + ".jpg", self._better_img)

    def check_bg(self,img):
        v = process.process4(img, self._base_img[0])
        if v > self._mark_value and v > 9:
            self._mark_img = img
            self._mark_value = v

    def clear_mark(self):
        self._mark_value = 0
        self._mark_img = None

    def recs_draw(self,draws, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        for index in draws:
            if index != -1:
                roi = self.ROIs[0][index]
                cv2.rectangle(img,  (roi[1], roi[3]), (roi[0], roi[2]),(255, 0, 0),3)

        image = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
        photo = QPixmap.fromImage(image)
        return photo