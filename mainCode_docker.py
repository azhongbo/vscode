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



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( download command 命令 )"
MyCodeString = '''
###  Docker command 命令 ####
docker pull tomcat:jre-9  ## 下載 tomcat
docker pull ubuntu  ## 下載 ubuntu
docker images ## 列出 images 
docker ps ## 列出執行中的 image

docker run -it --rm ubuntu bash

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( Dockfile 範例 )"
MyCodeString = '''
###  Docker Dockfile ####
Dockfile
FROM tomcat
WORKDIR         /usr/local/tomcat/webapps/
RUN mkdir       /usr/local/tomcat/webapps/ROOT
RUN echo okok > /usr/local/tomcat/webapps/ROOT/index.jsp

docker built -t myshop .
docker images
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( save load images 匯出匯入 )"
MyCodeString = '''
###  Docker save load images 匯出匯入 ####
docker save -o <path for generated tar file> <image name>
docker load -i <path to image tar file>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Docker ( 範例 )"
# MyCodeString = '''
# ###  Docker 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Docker ( 範例 )"
# MyCodeString = '''
# ###  Docker 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)





##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
