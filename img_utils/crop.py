# coding:utf-8
from fnmatch import fnmatch
#裁剪图片
import cv2
from PIL import Image
import os
import os.path
from tkFileDialog import askdirectory
filelist = []
dirpath = askdirectory(title="Select A Video Frames Folder", mustexist=1, initialdir='/home/zb/tmp')
if (os.path.isdir(dirpath)):
    for file in os.listdir(dirpath):
        if fnmatch(file, '*.jpg'):
            filelist.append(str(os.path.join(dirpath, file)))

for file in filelist:
    filename = str(file).split("/")[-1].split(".")[0]
    im = cv2.imread(file)
    out = im[90:180,0:240]
    newname = dirpath +"/save"+ "/" + filename + "(2).jpg"
    cv2.imwrite(newname,out)
