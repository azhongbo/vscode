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
MyCodeTitle  = "RyanCode DOS ( 命令提示輸入 )"
MyCodeString = '''
:: ### 命令提示輸入 ##
ECHO 電腦名稱
SET /P myhost= # 
ECHO 輸入帳號
SET /P username= # 
echo net localgroup administrators "win\%username%" /add
psexec \\%myhost% net localgroup administrators "win\%username%" /add
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DOS ( 日期時間 )"
MyCodeString = '''
:: ### 日期-時間 ##
%date:~-13,4%-%date:~-8,2%-%date:~-5,2% %time:~-11,8%
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DOS ( 副程式 )"
MyCodeString = '''
:: ### DOS Function 副程式 ##
call:myDosFunc 100 YeePEE
call:myDosFunc 100,for me
echo.&pause&goto:eof

:myDosFunc
echo. it could do %~1 of things %~2.
goto:eof
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DOS ( 亂數暫停 )"
MyCodeString = '''
:: ### 亂數暫停 ##
set /a num=%random% %%10 +1
ping -n %num% 127.0.0.1 > NUL
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DOS ( ping 主機返回結果 )"
MyCodeString = '''
:: ###  DOS ping 主機返回結果  ####
set ip=%1
ping -n 1 %ip% | find "TTL"
if not errorlevel 1 set error=win
if     errorlevel 1 set error=fail
cls
echo Result: %error%
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode DOS ( 範例 )"
# MyCodeString = '''
# ###  DOS 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode DOS ( 範例 )"
# MyCodeString = '''
# ###  DOS 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)





##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
