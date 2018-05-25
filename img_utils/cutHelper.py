# coding:utf-8
# 将图片以小分片的形式裁剪下来
import tkFileDialog
import cv2
from configurationInjection import configInjection
import os

config = configInjection()
config.loadConfiguration()

rois = config.rois[0]

flag = True
videopath = tkFileDialog.askopenfilename(initialdir="/home/zb/myfile/cutSave")
count = 0
cap = cv2.VideoCapture(videopath)
while flag:
    flag, img = cap.read()

    basePath = "/home/zb/myfile/cutSave/1-1"
    framesBasePath = "/home/zb/myfile/cutSave/1-1/frames7"
    if not os.path.exists(basePath):
        os.mkdir(basePath)
    if not os.path.exists(framesBasePath):
        os.mkdir(framesBasePath)
    bigSlice = img[360:1080, 480:1440]
    # cv2.imwrite(basePath + "/" + str(count) + ".jpg", bigSlice)

    for roi in rois:
        slice = img[roi[2]:roi[3], roi[0]:roi[1]]
        count += 1
        cv2.imwrite(framesBasePath + "/" + str(count) + ".jpg", slice)

cap.release()
