# encoding:utf-8
import os
import cv2
from Tkinter import *
import tkMessageBox
import sys
from tkFileDialog import askdirectory,askopenfilename
reload(sys)
sys.setdefaultencoding('utf8')


class Convert:
    def c1(self):
        self.photosuffix = '.jpg'
        self.label2["text"] = '存储格式为JEPG'
    def c2(self):
        self.photosuffix = '.tif'
        self.label2["text"] = '存储格式为TIFF'
    def c3(self):
        self.photosuffix = '.png'
        self.label2["text"] = '存储格式为PNG'
    def select_frames_path(self):
        self.frames_save_path = askdirectory(title="Select A FramesSave Folder", mustexist=1,initialdir='G:/lastframes1')
        self.label1["text"] = self.frames_save_path

    def select_video(self):
        self.video_filepath = askopenfilename(title="Please Select A Video", initialdir='G:')
        videoname = str(self.video_filepath).split('/')[-1]
        if not videoname.lower().endswith(('.avi', '.mp4', '.mov', '.flv', '.rmvb', '.wmv')):
            tkMessageBox.askokcancel(title='警告', message='选择的文件不是视频文件,请重新选择')
        self.label0["text"] = self.video_filepath

    def start_convert(self):
        self.video_to_frame()

    def __init__(self):
        self.photosuffix = '.tif'
        self.video_filepath = ''
        self.frames_save_path = ''
        self.frames_num = 0
        self.count = 0
        self.root = Tk()
        self.root.title('视频转帧图像工具')
        self.root.geometry('300x150')
        self.strv = StringVar()
        self.strv.set('.tif')
        self.frame = [Frame(), Frame(), Frame(), Frame()]
        self.video_path = Button(self.frame[0], text='选 择', width=5,height=1, command=self.select_video)
        self.video_path.pack(side =LEFT)
        self.label0 = Label(self.frame[0], text='请选择你要转换的视频', width=50 ,bg='white', fg='green')
        self.label0.pack(side=TOP , fill=X)
        self.frame[0].pack(expand=1, fill=X)
        self.frame_save_path = Button(self.frame[1], text='选 择', width=5, height=1, command=self.select_frames_path)
        self.frame_save_path.pack(side=LEFT)
        self.label1 = Label(self.frame[1], text='请选择你要存储的路径', width=50, bg='white', fg='green')
        self.label1.pack(side=TOP, fill=X)
        self.frame[1].pack(expand=1, fill=X)
        self.label2 = Label(self.frame[2], text='请选择保存的图片格式', width=20, height=1, bg='white', fg='green')
        self.label2.pack(side=LEFT,fill=X)
        self.rb1 = Radiobutton(self.frame[2],text='JEPG',variable=self.strv,value='.jpg',command=self.c1)
        self.rb1.pack(side=LEFT, fill=Y)
        self.rb2 = Radiobutton(self.frame[2],text='TIFF',variable=self.strv,value='.tif',command=self.c2)
        self.rb2.pack(side=LEFT, fill=Y)
        self.rb3 = Radiobutton(self.frame[2], text='PNG', variable=self.strv, value='.png', command=self.c3)
        self.rb3.pack(side=LEFT, fill=Y)
        self.frame[2].pack(expand=1, fill=X)
        self.startb = Button(self.frame[3], text='开始转换', width=10, height=1, command=self.start_convert)
        self.startb.pack(expand=1,fill=BOTH,side=RIGHT,padx=15,pady=2)
        self.label3 = Label(self.frame[3], text='(0/0)', width=25, bg='white', fg='green')
        self.label3.pack(side=LEFT, fill=X)
        self.frame[3].pack(expand=1, fill=X)

    def video_to_frame(self):
        if os.path.isdir(self.frames_save_path) and os.path.isfile(self.video_filepath) :
            success = True
            cap = cv2.VideoCapture(self.video_filepath)
            self.frames_num = int(cap.get(7))
            while success:
                try:
                    success, image = cap.read()
                    if success:
                        cv2.imwrite(os.path.join(self.frames_save_path, '{:05d}'.format(self.count)+self.photosuffix), image)
                        self.count += 1
                        self.label3['text'] = '({}/{})'.format(self.count, self.frames_num)
                        self.label3.update()
                    else:
                        tkMessageBox.askokcancel(title='提示', message='转换完成')
                        cap.release()
                        break
                except IOError, e:
                    print e


def main():
    con = Convert()
    con.root.mainloop()
if __name__ == '__main__':
    main()