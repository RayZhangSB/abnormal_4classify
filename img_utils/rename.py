# coding:utf-8
import cv2
import os
import numpy as np
from tkFileDialog import askdirectory
from fnmatch import fnmatch

filelist = []
dirpath = askdirectory(title="Select A Video Frames Folder", mustexist=1,initialdir='/home/zb/myfile/cutSave/1-1')

count = 90000

if (os.path.isdir(dirpath)):
    for file in os.listdir(dirpath):
        if fnmatch(file, '*.jpg'):
            filelist.append(str(os.path.join(dirpath, file)))

for path in filelist:

    os.rename(path,dirpath+"/"+str(count)+".jpg")
    count+=1
    # basePath  = str(path).split("/")[-2]
    # image = cv2.imread(path)
    # cv2.imwrite(dirpath+"/"+str(count)+".jpg",image)
    # img1 = np.rot90(image)
    # cv2.imwrite(basePath+"0.5pi"+".jpg",img1)
    #
    # img2 = np.rot90(img1)
    # cv2.imwrite(basePath + "pi" + ".jpg", img2)
    # img3 = np.rot90(img2)
    # cv2.imwrite(basePath + "-0.5pi" + ".jpg", img3)