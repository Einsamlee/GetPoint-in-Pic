#!/usr/bin/env python
# coding: utf-8

# 载入基础的包，使用cv在图层上画线和画点

# In[1]:


import numpy as np
import cv2


# 这里放图片的路径，建议文件夹都用英文命名

# In[2]:


img_path = "C:/Users/li_x/Desktop/1.png"


# cv2.imread()有两个参数，第一个参数filename是图片路径，第二个参数flag表示图片读取模式
# 参数flag共有三种：
# cv2.IMREAD_COLOR：加载彩色图片，这个是默认参数，可以直接写1
# cv2.IMREAD_GRAYSCALE：以灰度模式加载图片，可以直接写0
# cv2.IMREAD_UNCHANGED：包括alpha(包括透明度通道)，可以直接写-1

# 读取图片

# In[3]:


img = cv2.imread(img_path,1)


# 显示像素点坐标

# In[4]:


tpPointsChoose = []
pointsCount = 0
count = 0
pointsMax = 50
size = img.shape
def on_mouse(event, x, y, flags, param):
    global img, point1, point2, count, pointsMax
    global  tpPointsChoose  # 存入选择的点
    global pointsCount  # 对鼠标按下的点计数
    global img2
    global size
    img2 = img.copy()# 此行代码保证每次都重新再原图画  避免画多了
    img3 = img.copy()
    h=size[0]
    w=size[1]
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        h=size[0]
        w=size[1]
        pointsCount = pointsCount + 1
        #print('pointsCount:', pointsCount)
        point1 = (x, y)
        #归一化
        textx = round(x/w, 3)
        texty = round(y/h, 3)
        text1 = "%.3f,%.3f" % (textx, texty)
        print(text1)
        cv2.circle(img2, point1, 10, (0, 255, 0), 2)
        cv2.putText(img2, text1, point1, cv2.FONT_HERSHEY_PLAIN,1.5, (0,0,255),2)
        # 将选取的点保存到list列表里
        tpPointsChoose.append((x, y))  # 用于画点
        # 将鼠标选的点用直线连起来
        for i in range(len(tpPointsChoose) - 1):
            #print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
        cv2.imshow('src', img2)
    # -------------------------右键按下清除轨迹-----------------------------
    if event == cv2.EVENT_RBUTTONDOWN:  # 右键点击
        print("clear lines")
        pointsCount = 0
        tpPointsChoose = []
        text1=""
        print(len(tpPointsChoose))
        for i in range(len(tpPointsChoose) - 1):
            print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
        cv2.imshow('src', img2)


# 显示归一化的像素点坐标

# In[6]:


def on_mouse(event, x, y, flags, param):
    global point1, count, pointsMax
    global tpPointsChoose  # 存入选择的点
    global pointsCount  # 对鼠标按下的点计数
    global size
    img2 = img.copy()  # 此行代码保证每次都重新再原图画  避免画多了
    h = size[0]
    w = size[1]
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        h = size[0]
        w = size[1]
        pointsCount = pointsCount + 1
        point1 = (x, y)
        textx = round(x / w, 3)
        texty = round(y / h, 3)
        text1 = "%.3f,%.3f" % (textx, texty)
        print(text1)
        cv2.circle(img2, point1, 10, (0, 255, 0), 2)
        cv2.putText(img2, text1, point1, cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
        tpPointsChoose.append((x, y))  # 用于画点
        for i in range(len(tpPointsChoose) - 1):
            # print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
        cv2.imshow('src', img2)
    if event == cv2.EVENT_RBUTTONDOWN:  # 右键点击
        print("clear lines")
        pointsCount = 0
        tpPointsChoose = []
        text1 = ""
        print(len(tpPointsChoose))
        for i in range(len(tpPointsChoose) - 1):
            print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
        cv2.imshow('src', img2)


# In[7]:


img_path = "C:/Users/li_x/Desktop/1.png"
img = cv2.imread(img_path,1)
cv2.namedWindow('src')
cv2.setMouseCallback('src', on_mouse)
cv2.imshow('src', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

