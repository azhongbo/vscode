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
# MyCodeTitle  = "RyanCode WebUrl ( 範例 )"
# MyCodeString = '''
# ###  WebUrl ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode WebUrl ( Docker url )"
MyCodeString = '''
###  Docker url ####
千锋Java教程：36 Docker 镜像 Dockerfile 定制镜像
https://www.youtube.com/watch?v=xvtzu16n6lU&list=PLwDQt7s1o9J55UmZFIk6w16k3Kz0ke8x5&index=37
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)










##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################