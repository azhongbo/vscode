#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,time,datetime,time,re
from tkinter import *

root_fold = 'ubuntu-mate-16.04'
iso_name  = 'ubuntu-mate-16.04.3-desktop-amd64.iso'
vdi_file  = 'ubuntu-16.04-amd64.vdi'
iso_file  = '/sda3/VirtualBoxVMs/' + iso_name

# 使用 時間日期格式當作版本 ver 
ver = time.strftime('%Y%m%d.%H%M',time.localtime(time.time() - 0*60*60) )
out_iso   = '/sda3/VirtualBoxVMs/ubuntu-mate-' + ver + '.iso'


window = Tk()
#window.title('DIY ubuntu-mate-16.04.3-desktop-amd64')
window.title( "Diy ubuntu-mate 16.04")
window.geometry('800x480')

sButton = [None] *  500
cButton = [None] *  500
sLabel  = [None] *  500


os.popen("mkdir -p tmp")
os.popen("mkdir -p " + root_fold + "/bin")
os.popen("mkdir -p " + root_fold + "/etc/apt")
os.popen("mkdir -p " + root_fold + "/etc/xdg/autostart")
os.popen("mkdir -p " + root_fold + "/root")
os.popen("mkdir -p " + root_fold + "/usr/bin")
os.popen("mkdir -p " + root_fold + "/usr/local/bin")
os.popen("mkdir -p " + root_fold + "/usr/local/lib/python3.5")
os.popen("mkdir -p " + root_fold + "/usr/share/backgrounds/mate/nature")

def get_flag_id(id):
    return "tmp/chk_flag_id_" + str(id)

def hit_me(id,runCommand):
    global sLabel
    sLabel[id].config(fg="red")
    os.popen("touch " + get_flag_id(id) )

    file_name = "CommandLine_" + str(id) + ".sh"

    f = open( "tmp/" + file_name , 'w', encoding = 'UTF-8')
    f.write(runCommand)
    f.close()

    os.popen("chmod 755 tmp/" + file_name)
    os.popen("sudo mate-terminal -x bash -c 'sh tmp/" + file_name + "' ")




### 開始 chroot 安裝
def hit_chroot(id,runCommand):
    global sLabel,root_fold
    sLabel[id].config(fg="red")
    os.popen("touch " + get_flag_id(id) )

    # sourceslist = """
    # deb http://tw.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
    # deb http://security.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
    # deb http://tw.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
    # """.replace("    ","")
    # f = open( "tmp/sources.list" , 'w', encoding = 'UTF-8')
    # f.write(sourceslist)
    # f.close()
    # os.popen("sudo cp tmp/sources.list /livecd/isonew/custom/etc/apt")

    # resolvconf = "nameserver 168.95.1.1"
    # f = open( "tmp/resolv.conf" , 'w', encoding = 'UTF-8')
    # f.write(resolvconf)
    # f.close()
    # os.popen("sudo cp tmp/resolv.conf /livecd/isonew/custom/etc")

    os.popen("sudo cp -R " + root_fold + "/* /livecd/isonew/custom")

    install_code = """#!/bin/bash
        mount -t proc none /proc
        mount -t sysfs none /sys
        export HOME=/root
        cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime

        chmod 755 /bin/chewing
        chmod 755 /usr/bin/phantomjs
        chmod 755 /usr/local/bin/geckodriver

        apt-get update

        %s

        rm -f /root/*
        apt --fix-broken -y install
        apt-get clean
        rm -rf /tmp/*
        sync
        umount /proc /sys
        rm /install.code.sh        
    """ %(runCommand)
    install_code = install_code.replace("        ","")

    f = open( "tmp/install.code.sh" , 'w', encoding = 'UTF-8')
    f.write(install_code)
    f.close()

    os.popen("sudo cp tmp/install.code.sh /livecd/isonew/custom")
    time.sleep(1)    
    os.popen("sudo chmod 755 /livecd/isonew/custom/install.code.sh")

    ## chroot 自動安裝
    execCommand = """#!/bin/bash
    echo ./install.code.sh | chroot /livecd/isonew/custom
    #chroot /livecd/isonew/custom

    sleep 5
    """

    ### chroot 後手動安裝，如果搜尋到字串有 VMware 時候
    if re.search( "VMware-Workstation-Full-14.1.1-7528167.x86_64" , runCommand ):
        execCommand = """#!/bin/bash
        #echo ./install.code.sh | chroot /livecd/isonew/custom
        chroot /livecd/isonew/custom

        sleep 5
        """


    file_name = "CommandLine_" + str(id) + ".sh"

    f = open( "tmp/" + file_name , 'w', encoding = 'UTF-8')
    f.write(execCommand)
    f.close()

    os.popen("chmod 755 tmp/" + file_name)
    os.popen("sudo mate-terminal -x bash -c 'sh tmp/" + file_name + "' ")



def clean_me(id):
    global sLabel
    sLabel[id].config(fg="black")
    os.popen("rm -f " + get_flag_id(id) )


def layButton(id,xx,yy,actionText,runCommand):
    global sButton,sLabel

    sButton[id] = Button( window, text='安裝'      , font=( "Arial", 12) , command=lambda:hit_me(id,runCommand) )
    sButton[id].place( x=xx     , y=yy   , anchor=NW , width=40,height=25)

    cButton[id] = Button( window, text='清除'      , font=( "Arial", 12) , command=lambda:clean_me(id) )
    cButton[id].place( x=xx+45  , y=yy   , anchor=NW , width=40,height=25)

    sLabel[id]  = Label(  window, text=actionText , font=( "Arial", 12) , fg="black")
    sLabel[id].place(  x=xx+90  , y=yy+2 , anchor=NW )

    if os.path.isfile( get_flag_id(id) ):
        sLabel[id].config(fg="red")




def chrootButton(id,xx,yy,actionText,runCommand):
    global sButton,sLabel

    sButton[id] = Button( window, text='安裝'      , font=( "Arial", 12) , command=lambda:hit_chroot(id,runCommand) )
    sButton[id].place( x=xx     , y=yy   , anchor=NW , width=40,height=25)

    cButton[id] = Button( window, text='清除'      , font=( "Arial", 12) , command=lambda:clean_me(id) )
    cButton[id].place( x=xx+45  , y=yy   , anchor=NW , width=40,height=25)

    sLabel[id]  = Label(  window, text=actionText , font=( "Arial", 12) , fg="black")
    sLabel[id].place(  x=xx+90  , y=yy+2 , anchor=NW )

    if os.path.isfile( get_flag_id(id) ):
        sLabel[id].config(fg="red")




#########################################################
### 基本區 1) 建立 VDI 檔案
#########################################################

xx = 20
yy = 20
id = 0
actionText = "1) 建立 VDI 檔案"
runCommand = """#!/bin/bash
#### 建立基本 VDI 檔案 ####
pwd

umount /dev/nbd0p1
umount /dev/nbd0p1

rm -f VDI_FILE
VBoxManage createhd --filename VDI_FILE --size 81920
chmod a+rw VDI_FILE

modprobe nbd
qemu-nbd -c /dev/nbd0 VDI_FILE

echo "d
n
p
1


w
" | fdisk /dev/nbd0
mkfs.ext4 -F /dev/nbd0p1

sleep 5
exit
""".replace("VDI_FILE",vdi_file) 
layButton(id,xx,yy,actionText,runCommand)




#########################################################
### 基本區 2) 建立目錄，掛載 VDI 檔案 
#########################################################

xx = 20
yy = yy + 35
id = id + 1
actionText = "2) 建立目錄，掛載 VDI 檔案 "
runCommand = """#!/bin/bash
#### 建立目錄，掛載 VDI 檔案 ####

mkdir -p /livecd/isomount /livecd/isonew/squashfs
mkdir -p /livecd/isomount /livecd/isonew/cd
mkdir -p /livecd/isomount /livecd/isonew/custom

umount /dev/nbd0p1
sleep 1
umount /dev/nbd0p1
sleep 1
umount /dev/nbd0p1
sleep 2

modprobe nbd
qemu-nbd -c /dev/nbd0 %s

mount /dev/nbd0p1 /livecd

df -k

""" %(vdi_file)
layButton(id,xx,yy,actionText,runCommand)




#########################################################
### 基本區 3) 建立目錄，掛載 VDI 檔案 
#########################################################

xx = 20
yy = yy + 35
id = id + 1
actionText = "3) 解開 ISO 檔案至 LiveCD  "
runCommand = """#!/bin/bash
#### 解開 ISO 檔案至 LiveCD ####

cd /livecd
mount -o loop,ro  %s isomount
#mount -t tmpfs -o size=6656M tmpfs /livecd/isonew/custom/

rsync --exclude=/casper/filesystem.squashfs -a isomount/ isonew/cd/

modprobe squashfs

mount -t squashfs -o loop isomount/casper/filesystem.squashfs isonew/squashfs

rsync -a isonew/squashfs/ isonew/custom/

umount isonew/squashfs
umount isomount

sync;sync;sync;

sleep 3
""" %(iso_file)
layButton(id,xx,yy,actionText,runCommand)


#########################################################
### 基本區 4) 封裝 ISO 檔案
#########################################################

xx = 20
yy = yy + 35
id = id + 1
actionText = "4) 封裝 ISO 檔案"
runCommand = """#!/bin/bash
#### 解開 ISO 檔案至 LiveCD ####
cd /livecd
rm /livecd/isonew/cd/casper/filesystem.squashfs

cd /livecd
chmod +w isonew/cd/casper/filesystem.manifest
mksquashfs isonew/custom isonew/cd/casper/filesystem.squashfs

cd /livecd
cd isonew/cd
mkisofs -r -V "UbuntuLiveCD" -b isolinux/isolinux.bin -c isolinux/boot.cat -cache-inodes -J -l -no-emul-boot -boot-load-size 4 -boot-info-table -o %s .

sync;sync;sync;
sleep 1
""" %(out_iso)
layButton(id,xx,yy,actionText,runCommand)









yy = 300
#########################################################
### 工具區 97) nmon
#########################################################

xx = 20
yy = yy + 35
id = id + 1
actionText = "97) nmon"
runCommand = """#!/bin/bash
nmon
"""
layButton(id,xx,yy,actionText,runCommand)




#########################################################
### 工具區 98) df -m
#########################################################

xx = 20
yy = yy + 35
id = id + 1
actionText = "98) df -m"
runCommand = """#!/bin/bash
watch -n 2 df -m
"""
layButton(id,xx,yy,actionText,runCommand)



#########################################################
### 工具區 99) Reboot
#########################################################

xx = 20
yy = yy + 35
id = id + 1
actionText = "99) reboot"
runCommand = """#!/bin/bash
sync;sync;sync;reboot
"""
layButton(id,xx,yy,actionText,runCommand)







#########################################################
### 安裝區 1) 安裝 VirtualBox 相關
#########################################################

xx = 380
yy = -15
yy = yy + 35
id = id + 1
actionText = "1) 安裝 VirtualBox 所有工具"
runCommand = """
apt-get -y install virtualbox virtualbox-guest-utils virtualbox-guest-additions-iso  virtualbox-qt qemu qemu-kvm squashfs-tools
"""
chrootButton(id,xx,yy,actionText,runCommand)


#########################################################
### 安裝區 2) 安裝 網路工具
#########################################################

yy = yy + 35
id = id + 1
actionText = "2) 安裝 網路工具"
runCommand = """
apt-get -y install firefox uget curl remmina remmina-plugin-rdp remmina-plugin-vnc etherape lynx nbtscan net-tools nmap putty
"""
chrootButton(id,xx,yy,actionText,runCommand)


#########################################################
### 安裝區 3) 安裝 一般工具
#########################################################

yy = yy + 35
id = id + 1
actionText = "3) 安裝 一般工具"
runCommand = """
apt-get -y install ubuntu-restricted-extras winff grsync clonezilla gstm kazam mdadm shutter gnome-raw-thumbnailer ufraw-batch encfs k4dirstat nmon language-pack-zh-hant expect gimp git ibus ibus-chewing ibus-table-cangjie libreoffice-l10n-zh-tw libreoffice-pdfimport p7zip p7zip-full p7zip-rar libjpeg62 smplayer
"""
chrootButton(id,xx,yy,actionText,runCommand)



#########################################################
### 安裝區 4) 更新 python
#########################################################

yy = yy + 35
id = id + 1
actionText = "4) 更新 python"
runCommand = """
apt-get -y install python3-pip python3-tk python3-dev scrot python-pip  python-tk  python3-dev         

python3 -m pip install --upgrade pip
python3 -m pip install selenium
python3 -m pip install python3-xlib
python3 -m pip install pymongo
python3 -m pip install beautifulsoup4

python -m pip install --upgrade pip
python -m pip install selenium
python -m pip install python-xlib
python -m pip install pymongo
"""
chrootButton(id,xx,yy,actionText,runCommand)


#########################################################
### 安裝區 5) 安裝 ssh-server samba lamp
#########################################################

yy = yy + 35
id = id + 1
actionText = "5) 安裝 ssh-server samba lamp"
runCommand = """
apt-get -y install tasksel openssh-server samba system-config-samba
tasksel install lamp-server

apt-get -y install php7.0-sqlite3 sqlite3 php7.0-mysql apache2-dev 
apt-get -y install php-mongodb mongodb php-mongodb mongodb
"""
chrootButton(id,xx,yy,actionText,runCommand)




#########################################################
### 安裝區 6) 安裝 模擬器
#########################################################

yy = yy + 35
id = id + 1
actionText = "6) 安裝 模擬器"
runCommand = """
apt-get -y install mednafen gameconqueror

cd /tmp
wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mednafen/mednafen_0.9.48+dfsg-1_amd64.deb
dpkg -i mednafen_0.9.48+dfsg-1_amd64.deb

cd /tmp
wget http://kr.archive.ubuntu.com/ubuntu/pool/universe/m/mednaffe/mednaffe_0.8.6-1_amd64.deb
dpkg -i mednaffe_0.8.6-1_amd64.deb
"""
chrootButton(id,xx,yy,actionText,runCommand)




#########################################################
### 安裝區 7) 安裝 Sublime/MS sqlcmd/Chrome/H264
#########################################################

yy = yy + 35
id = id + 1
actionText = "7) 安裝 Sublime/MS sqlcmd/Chrome/H264"
runCommand = """
cd /tmp

## Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb

## Sublime
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | apt-key add -
apt-get -y install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | tee /etc/apt/sources.list.d/sublime-text.list
apt-get update
apt-get -y install sublime-text

## MS sqlcmd
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list
apt-get update 
apt-get -y install mssql-tools unixodbc-dev

ln -s /opt/mssql-tools/bin/sqlcmd /usr/bin/sqlcmd
ln -s /opt/mssql-tools/bin/bcp /usr/bin/bcp


## H264
wget http://h264.code-shop.com/download/apache_mod_h264_streaming-2.2.7.tar.gz
tar -zxvf apache_mod_h264_streaming-2.2.7.tar.gz

cd mod_h264_streaming-2.2.7
./configure --with-apxs=`which apxs2`
make
make install
echo 'LoadModule h264_streaming_module /usr/lib/apache2/modules/mod_h264_streaming.so' >> /etc/apache2/apache2.conf
echo 'AddHandler h264-streaming.extensions .mp4' >> /etc/apache2/apache2.conf
"""
chrootButton(id,xx,yy,actionText,runCommand)




#########################################################
### 安裝區 8) 安裝 root/*.deb
#########################################################

yy = yy + 35
id = id + 1
actionText = "8) 安裝 root/*.deb"
runCommand = """
cd /root
dpkg -i *.deb
"""
chrootButton(id,xx,yy,actionText,runCommand)



#########################################################
### 安裝區 9) 安裝 VMWare
#########################################################

yy = yy + 35
id = id + 1
actionText = "9) 安裝 VMWare"
runCommand = """
cd /root
chmod 755 VMware-Workstation-Full-14.1.1-7528167.x86_64.bundle
./VMware-Workstation-Full-14.1.1-7528167.x86_64.bundle --custom
"""
chrootButton(id,xx,yy,actionText,runCommand)



#########################################################
### 安裝區 10) 安裝 Horizon-Client
#########################################################

yy = yy + 35
id = id + 1
actionText = "10) 安裝 Horizon-Client"
runCommand = """
cd /root
chmod 755 VMware-Horizon-Client-4.8.0-8518891.x64.bundle
./VMware-Horizon-Client-4.8.0-8518891.x64.bundle --console
"""
chrootButton(id,xx,yy,actionText,runCommand)



#########################################################
### 安裝區 11) 安裝 joystick keyboard 對應
#########################################################

yy = yy + 35
id = id + 1
actionText = "11) 安裝 joystick keyboard 對應"
runCommand = """
add-apt-repository ppa:mdeguzis/libregeek
apt-get update
apt-get install antimicro
"""
chrootButton(id,xx,yy,actionText,runCommand)



#########################################################
### 安裝區 12) 安裝 TeamView (最後安裝)
#########################################################

yy = yy + 35
id = id + 1
actionText = "12) 安裝 TeamView (最後安裝)"
runCommand = """
cd /root
apt-get -y install libqt5qml5
apt-get -f install
dpkg -i teamviewer_13.2.13582_amd64.deb
"""

chrootButton(id,xx,yy,actionText,runCommand)














window.mainloop()






# chrome





# lb.place(relx = 1,rely = 0.5,anchor = CENTER)
# 使用绝对坐标将Label放置到(0,0)位置上
# x,y指定组件放置的绝对位置







# window = tk.Tk()
# window.title('my window')
# window.geometry('640x480')


# def hit_me():
#     aa=1


# b = tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
# b.place(relx = 0.5,rely = 0.5,anchor = CENTER,x = -300,y = -300)

# window.mainloop()