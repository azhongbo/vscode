#!/usr/bin/python3
import cv2
import numpy as np
import time

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver





# HSV 去背 圖片 ###################################################
# https://youtu.be/WQeoO7MI0Bs?t=3377
#7,调整图片对比度和亮度


 
def contrast_Ratio_brightness(arg):
    #arg参数：为接收新变量地址
    #a为对比度，g为亮度
    #cv2.getTrackbarPos获取滑动条位置处的值
    #第一个参数为滑动条1的名称，第二个参数为窗口的名称。
    a = cv2.getTrackbarPos(trackbarName1, windowName)
    g = cv2.getTrackbarPos(trackbarName2, windowName)
    h,w,c=image.shape
    mask=np.zeros([h,w,c],image.dtype)
    #cv2.addWeighted函数对两张图片线性加权叠加
    dstImage=cv2.addWeighted(image,a,mask,1-a,g)
    cv2.imshow("dstImage",dstImage)

image = cv2.imread("test2.png")

cv2.imshow("Saber",image)
trackbarName1="Ratio_a"
trackbarName2="Bright_g"
windowName="dstImage"
a=1#设置a的初值。
g=10#设置g的初值。
count1=20#设置a的最大值
count2=50#设置g的最大值
#给滑动窗口命名，该步骤不能缺少！而且必须和需要显示的滑动条窗口名称一致。
cv2.namedWindow(windowName)
 
#第一个参数为滑动条名称，第二个参数为窗口名称，
#第三个参数为滑动条参数，第四个为其最大值，第五个为需要调用的函数名称。
cv2.createTrackbar(trackbarName1, windowName,a,count1,contrast_Ratio_brightness)
cv2.createTrackbar(trackbarName2, windowName,g,count2,contrast_Ratio_brightness)
#下面这步调用函数，也不能缺少。
contrast_Ratio_brightness(0)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
