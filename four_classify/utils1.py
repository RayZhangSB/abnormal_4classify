# coding:utf-8
#2018.3.5
#工具函数类
import time
import os
import numpy as np
import matplotlib.pyplot as plt
#存储图片
def save_pic(save_path,Qpixmapphoto,grabber_num):
    path = save_path+'/'+str(grabber_num)+"-"+str(time.strftime('%m-%d_%H:%M:%S', time.localtime(time.time())))+'.jpg'
    Qpixmapphoto.save(path)

# 保证列表里最多只有3个图像
def update_list(list,obj):
    list.reverse()
    list.append(obj)
    list.reverse()
    list.pop()
	
def save_plot_pic(list,save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    else:
        x = np.linspace(1,len(list),len(list))
        plt.plot(x,list)
        plt.xlabel("Photo Label")
        plt.ylabel("Value")
        plt.grid(True)
        plt.savefig(save_path+"/"+str(time.strftime('%m-%d %H:%M:%S', time.localtime(time.time())))+".jpg")
		
#计算差分值
def get_diff_value(i, _vals):
    return _vals[i - 4] + _vals[i - 3] + _vals[i - 2] + _vals[i - 1] - \
            _vals[i + 1] - _vals[i + 2] - _vals[i + 3] - _vals[i + 4]

#将对象显示到显示框
def set_label_pic(label_name,picture):
    label_name.setPixmap(picture.scaled(label_name.width(),label_name.height()))