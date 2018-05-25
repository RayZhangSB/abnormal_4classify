# coding:utf-8
#存储一些图像处理方法
import cv2
import numpy as np
videobox1=[1,1,1,1,1]

def process1(image):  # IMG_2710
    #image = image[ videobox1[2]: videobox1[3],  videobox1[0]: videobox1[1]]
    image = cv2.GaussianBlur(image, (5, 5), 0.5)
    # image = cv2.Laplacian(image, -1, ksize=5)
    value = np.sum(image[:]) / videobox1[4]
    return value

def process2(image,roiArea):  # 102302
    sum1 = np.sum(image[:])
    value = sum1 / (roiArea/10)
    return value

def process3( image,roi):  # 101413
    #image = image[ videobox3[2]: videobox3[3],  videobox3[0]: videobox3[1]]
    image = cv2.Laplacian(image, -1, ksize=3)
    sum1 = np.sum(image[roi[2]:roi[3],roi[0]:roi[1]])
    value = 100*sum1 /(roi[3]-roi[2])*(roi[1]-roi[0])
    return value

# 主处理程序
def pro(image,roi):
    img=image[roi[2]:roi[3],roi[0]:roi[1]]#y1:y2,x1:x2
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    value =process2(img2,(roi[3]-roi[2])*(roi[1]-roi[0]))
    return value


def process4(img1,img2):
     bigRoi = [480, 1440, 360, 1080]
     img1 = img1[bigRoi[2]: bigRoi[3],bigRoi[0]: bigRoi[1]]
     img2 = img2[bigRoi[2]: bigRoi[3], bigRoi[0]: bigRoi[1]]
    #背景差分
     resImg = cv2.absdiff(img1,img2)
     return np.sum(resImg[:])/1000000