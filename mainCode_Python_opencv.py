#!/usr/bin/python3
import sys
from __save__ import *

########################################################
def runAllData(MyCodeTitle,MyCodeString,MyCodeName):
    global package1,package2,extension,count

    count = count + 1    

    (data1,data2,data3) = makeCode(MyCodeTitle,MyCodeString,MyCodeName+str(count))

    package1  = package1  + data1
    package2  = package2  + data2
    extension = extension + data3
########################################################


package1   = ""
package2   = ""
extension  = ""
count      = 0
MyCodeName = sys.argv[2]





# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python opencv ( 範例 )"
# MyCodeString = '''
# ###  Python opencv 範例程式 ####
# ### file: mainCode_Python_opencv
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python opencv ( 範例 )"
# MyCodeString = '''
# ###  Python opencv 範例程式 ####
# ### file: mainCode_Python_opencv
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python opencv ( 範例 )"
# MyCodeString = '''
# ###  Python opencv 範例程式 ####
# ### file: mainCode_Python_opencv
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( cv2 人臉辨識 Video)"
MyCodeString = '''
###  Python opencv cv2 人臉辨識 Video ####
### file: mainCode_Python_opencv
import numpy as np
import cv2

## 參數0是鏡頭
## cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('video2.mp4')
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

## 連續讀取每一個 frame
while cap.isOpened():
    
    ## 讀取一個 frame
    flag,frame = cap.read()
    
    ## 讀取最後一個 frame 後，結束
    if flag == False:
        break
    
    ## 人臉識別，畫圈圈
    gray = cv2.cvtColor(frame,code = cv2.COLOR_BGR2GRAY)
    face_zone = detector.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors = 5)
    for x,y,w,h in face_zone:
        cv2.circle(frame,center = (x + w//2,y + h//2),radius = w//2,color = [0,0,255],thickness = 2)
    
    ## 顯示 frame
    cv2.imshow('test',frame)
    
    if ord('q') == cv2.waitKey(20):
        break
        
cv2.destroyAllWindows()
cap.release();
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( cv2 人臉辨識 )"
MyCodeString = '''
###  Python opencv cv2 人臉辨識 ####
### file: mainCode_Python_opencv

import numpy as np
import cv2

myImg = cv2.imread('star.jpg')

## 重新轉換圖片大小
# myImg2 = cv2.resize(myImg,dsize = (1200,800))

# 轉成黑白，尺寸維持
gray = cv2.cvtColor(myImg,code = cv2.COLOR_BGR2GRAY)

## 使用人臉數據 xml ，Google haarcascade_frontalface_default.xml
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# ScaleFactor：每次搜尋方塊減少的比例
# minNeighbers：每個目標至少檢測到幾次以上，才可被認定是真數據。
# minSize：設定數據搜尋的最小尺寸 ，如 minSize=(40,40)
# maxSize：設定數據搜尋的最大尺寸 ，如 maxSize=(150,150)

face_zone = detector.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 7 ,minSize = (50,50),maxSize = (150,150))

# 偵測人臉，畫框框
for x,y,w,h in face_zone:    
    ## 方框框
    #cv2.rectangle(myImg,pt1 = (x,y),pt2 = (x + w,y + h),color = [0,255,0],thickness = 2)
    
    ## 圓框框
    #cv2.circle(myImg,center = (x + w//2,y + h//2),radius = w//2, color = color.tolist(), thickness = 2)

cv2.imshow('myImg',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( cv2 圖片操作 )"
MyCodeString = '''
###  Python opencv  cv2 圖片操作 ####
### file: mainCode_Python_opencv

import numpy as np
import cv2

### 顯示陣列的大小
myImg.shape

### 顯示圖檔
cv2.imshow('myImg',myImg)
# 等待鍵盤輸入，0毫秒，無限等待
cv2.waitKey(0)
cv2.destroyAllWindows()

### 轉成灰階
# cv2 讀取圖片，顏色通道是 BGR 藍綠紅
# PIL 2讀取圖片，顏色通道是 RGB

myImg2 = cv2.cvtColor(myImg,code = cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',myImg2)
cv2.waitKey(0)
cv2.destroyAllWindows()

### 寫入圖片
cv2.imwrite('star2.jpg',myImg2)

### 顯示陣列的大小
myImg2.shape

### 重新 resize 圖片
myImg3 = cv2.resize(myImg,dsize = (440,666))
myImg3.shape

### 顯示圖檔
cv2.imshow('gray',myImg3)
while True:
    if ord('q') == cv2.waitKey(1000):
        break
cv2.destroyAllWindows()
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)












##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
