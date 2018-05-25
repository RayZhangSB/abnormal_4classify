# coding:utf-8
#2018.3.5

import ConfigParser

#在这里载入初始配置文件，包括roi参数以及机器学习模型
class ConfigInjection():
    def __init__(self):

        self.rois=[]  #保存所有摄像头的roi信息--rois[0]=[ [$roi0],[roi1],[roi2] ]
        self.address = None
        self.port = None
        self.streamAddr = None

    def load_configuration(self):
        cf = ConfigParser.ConfigParser()
        cf.read("./res/config.ini")
        cameraCount = cf.getint("BaseInfo","cameraCount")
        self.address = cf.get("BaseInfo", "address")
        self.port = cf.getint("BaseInfo", "port")
        self.streamAddr = cf.get("BaseInfo", "streamAddr")
        for i in range(cameraCount):
            roist = []
            ci = cf.items("Camera"+str(i))
            if ci !=None:
                for tuplei in ci:
                    roi = []
                    nums = str(tuplei[1]).split(",")
                    for num in nums:
                        roi.append(int(num))
                    roist.append(roi) #取到单个摄像头的所有roi信息
            self.rois.append(roist)

