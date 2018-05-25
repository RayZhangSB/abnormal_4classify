# coding:utf-8
#左右翻转
from PIL import Image
import os
import os.path
from tkFileDialog import askdirectory

rootdir = askdirectory(title="Select A Video Frames Folder", mustexist=1, initialdir='/home/zb/tmpp/fire')

for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        currentPath = os.path.join(parent, filename)

        im = Image.open(currentPath)
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
        newname = rootdir + "/" + filename + "(3).jpg"
        out.save(newname)
# im = Image.open(r'C:\Users\Administrator\Desktop\新建文件夹 (2)\1.jpg')