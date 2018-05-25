# coding:utf-8
import tkFileDialog
from Tkinter import *

from fnmatch import fnmatch
from tkFileDialog import askdirectory

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

savepath = os.getcwd() + "/save4"


def savePlotPhoto(list, num):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    else:
        plt.figure(num)
        if num == 20:
            plt.axis([0, 500, -100, 100])
        else:
            plt.axis([0, 500, -100, 100])
        x = np.linspace(1, len(list), len(list))
        plt.scatter(x, list, s=2, c="b", marker=".")
        plt.xlabel("Photo Label")
        plt.ylabel("Value")
        plt.grid(True)
        plt.savefig(savepath + "/" + str(num) + ".png")


ccc = []
for i in range(16):
    ccc.append([])
difs = []
for i in range(16):
    difs.append([])
bk = []
bkdif = []
ss = True
filelist = []
num = 0
videopath = tkFileDialog.askopenfilename(initialdir='/home/zb/myfile/myframes')
save_path = askdirectory(title="Select A Video Frames Folder", mustexist=1, initialdir='/home/zb/myfile/myframes')

cap = cv2.VideoCapture(videopath)
c = configInjection()
c.loadConfiguration()
rois = c.rois[0]
# if (os.path.isdir(dirpath)):
#     for file in os.listdir(dirpath):
#         if fnmatch(file, '*.jpg'):
#             filelist.append(str(os.path.join(dirpath, file)))
while ss:
    ss, image = cap.read()
    if ss and type(image) != NoneType:
        num += 1
        for i in range(16):
            ccc[i].append(process.pro(image, rois[i]))
            if num >= 9:
                difs[i].append(utils1.getDiff(num - 5, ccc[i]))
        bkValue = process.process3(image, [360, 1440, 480, 1440])

        if num >= 9:
            bkdif.append(bkValue - baseBV)
        else:
            baseBV = bkValue
        # cv2.imwrite(save_path + "/" + str(num) + ".jpg", image)
    else:

        for i in range(16):
            savePlotPhoto(difs[i], i)
        savePlotPhoto(bkdif, 20)
