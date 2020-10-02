import cv2
import numpy as np

# https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
# https://github.com/murtazahassan
# apt-get install v4l-utils 


# ### 讀取圖片 ###################################################
# img = cv2.imread("test.jpg")
# cv2.imshow("output",img)
# cv2.waitKey(0)


# ### 讀取 鏡頭 ###################################################
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,50) #亮度

# while True:
#     sucess, img = cap.read()
#     img1 = cv2.Canny( img,150,200)                                     ## 邊緣檢測
#     img2 = cv2.dilate( img1 , np.ones((5,5),np.uint8) , iterations=1 ) ## 邊緣檢測-增強
#     cv2.imshow("CAM Test" , img)
#     cv2.imshow("CAM Test1" , img1)
#     cv2.imshow("CAM Test2" , img2)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# ### 讀取影片 ###################################################
# cap = cv2.VideoCapture("test.mp4")
# while True:
#     sucess, img = cap.read()
#     cv2.imshow("video" , img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# ### 濾鏡處理 ###################################################
# img = cv2.imread("test.jpg")

# imgResiz     = cv2.resize( img , (300,200) )          ## 變更大小 
# imgCropped   = img[0:150,0:600]                       ## 剪裁圖片 img[height:width]
# imgGray      = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  ## 轉灰階
# imgBlur      = cv2.GaussianBlur(imgGray, (17,17),0 )  ## 高斯模糊

# imgCanny     = cv2.Canny(img,150,200)                                              ## 邊緣檢測
# imgDialation = cv2.dilate( imgCanny     , np.ones((5,5),np.uint8) , iterations=1 ) ## 邊緣檢測-增強
# imgEroded    = cv2.erode(  imgDialation , np.ones((5,5),np.uint8) , iterations=1 ) ## 邊緣檢測-減弱


# cv2.imshow( "imgGray"      , imgGray      )
# cv2.imshow( "imgBlur"      , imgBlur      )
# cv2.imshow( "imgCanny"     , imgCanny     )
# cv2.imshow( "imgDialation" , imgDialation )
# cv2.imshow( "imgEroded"    , imgEroded    )
# cv2.waitKey(0)


# ### 劃線 寫字 劃圈 ###################################################
# img = np.zeros( (512,512,3) , dtype=np.uint8  )
# img[:]             = 255,0,0   ## 整張變成藍色
# img[10:200,50:200] = 255,0,0   ## [y1:y2,x1:x2] ## 區域變成藍色
# cv2.line(      img , (0,0),(100,300),(0,255,0),5 )  ## 劃直線
# cv2.rectangle( img , (0,0),(100,300),(0,0,255),5 )  ## 劃長方形
# cv2.rectangle( img , (0,0),(100,300),(0,0,255),cv2.FILLED )  ## 劃 長方形+填滿
# cv2.circle( img , (200,300),100, (255,255,0),2 )  ## 劃 圓圈

# cv2.putText( img , "okok" , (200,100) , cv2.FONT_HERSHEY_COMPLEX,2,(0,150,0),1  )  ## 圖片寫字
# cv2.imshow("output1",img)
# cv2.waitKey(0)


### 擷取圖片 ###################################################
# img = cv2.imread("cards.jpg")

# width , height = 200,200 ## 定義輸出後的大小
# pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])     # 定義 擷取的座標點
# pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])   # 定義 輸出後的座標點
# matrix = cv2.getPerspectiveTransform(pts1, pts2)        # 計算轉換後的矩陣
# img2 = cv2.warpPerspective(img,matrix,(width, height))  # 使用透視變換 進行轉換

# cv2.imshow("output1",img)
# cv2.imshow("output2",img2)

# cv2.waitKey(0)


## 合併 堆疊 圖片 ###################################################

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


# img = cv2.imread("test.jpg")

# imgH = np.hstack( (img,img) ) ## 水平合併
# imgV = np.vstack( (img,img) ) ## 垂直合併

# imageStack = stackImages(0.5,([img,img,img],[img,img,img]  ) )
# cv2.imshow("imgH",imgH)
# cv2.imshow("imgV",imgV)
# cv2.imshow("imageStack",imageStack)
# cv2.waitKey(0)






# HSV 去背 圖片 ###################################################
# https://youtu.be/WQeoO7MI0Bs?t=3377

# def empty(a):
#     pass

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar( "Hue Min","TrackBars" ,   0 , 179 , empty )
# cv2.createTrackbar( "Hue Max","TrackBars" ,  19 , 179 , empty )
# cv2.createTrackbar( "Sat Min","TrackBars" , 110 , 255 , empty )
# cv2.createTrackbar( "Sat Max","TrackBars" , 240 , 255 , empty )
# cv2.createTrackbar( "Val Min","TrackBars" , 153 , 255 , empty )
# cv2.createTrackbar( "Val Max","TrackBars" , 255 , 255 , empty )

# while True:
#     img = cv2.imread("test2.png")
#     imgHSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos( "Hue Min","TrackBars" )
#     h_max = cv2.getTrackbarPos( "Hue Max","TrackBars" )
#     s_min = cv2.getTrackbarPos( "Sat Min","TrackBars" )
#     s_max = cv2.getTrackbarPos( "Sat Max","TrackBars" )
#     v_min = cv2.getTrackbarPos( "Val Min","TrackBars" )
#     v_max = cv2.getTrackbarPos( "Val Max","TrackBars" )

#     print(h_min,h_max,s_min,s_max,v_min,v_max    )

#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,upper)
#     imgResult = cv2.bitwise_and(img,img,mask=mask)

#     cv2.imshow("img",stackImages(0.7,([img,imgHSV,mask,imgResult])))
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



### 圖形檢測 ###################################################

# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#     for cnt in contours:
#         area = cv2.contourArea(cnt)        
#         if area>500:

#             cv2.drawContours( imgContour , cnt , -1 ,(255,0,0) ,3  ) ## 畫出外框
#             peri = cv2.arcLength(cnt,True) ## 邊緣長度 - 取得
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)  ## 頂點數量 - 取得
#             x,y,w,h = cv2.boundingRect(approx)  ## 頂點座標 - 取得
            
#             if len(approx) == 3: objectType = "Tri"
#             elif len(approx) == 4:
#                 if w/float(h) > 0.95 and w/float(h) < 1.05 : objectType = "Square"
#                 else: objectType = "Rectangle"
#             elif len(approx) > 5: objectType = "Circles"
#             else: objectType = "None"

            
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2  )  ## 畫出外框框
#             cv2.putText(imgContour,objectType, (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2) ## 標注

#             print(f"{area}\t{len(approx)}\t{peri}")



# img = cv2.imread("shapes.png")
# imgContour = img.copy()

# imgGray  = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY )
# imgBlur  = cv2.GaussianBlur( imgGray , (7,7),1  )
# imgCanny = cv2.Canny( imgBlur,50,50)


# getContours(imgCanny)

# imgStack = np.zeros_like(img)
# cv2.imshow("Original",  stackImages(0.7, ( [img,imgGray,imgBlur], [imgCanny,imgContour,imgStack]  ))  )
# cv2.waitKey(0)



### 圖形檢測 2 ###################################################



cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,50) #亮度

while True:
    sucess, img = cap.read()
    # imgGray  = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY )
    # imgBlur  = cv2.GaussianBlur( imgGray , (7,7),1  )
    # imgCanny = cv2.Canny( imgBlur,50,50)


    cv2.imshow("imgH",img)

    # cv2.imshow("Original",  stackImages(0.7, ( [img,imgGray,imgCanny] )) )


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# img = cv2.imread("shapes.png")
# imgContour = img.copy()

# imgGray  = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY )
# imgBlur  = cv2.GaussianBlur( imgGray , (7,7),1  )
# imgCanny = cv2.Canny( imgBlur,50,50)


# getContours(imgCanny)

# imgStack = np.zeros_like(img)
# cv2.imshow("Original",  stackImages(0.7, ( [img,imgGray,imgBlur], [imgCanny,imgContour,imgStack]  ))  )
# cv2.waitKey(0)








### 臉部檢測 ###################################################

# https://youtu.be/WQeoO7MI0Bs?t=6035
## Chapter9
# freecodecamp.org















