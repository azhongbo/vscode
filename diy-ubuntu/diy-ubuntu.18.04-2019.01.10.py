#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,time,datetime,time,re
from tkinter import *

root_fold = 'ubuntu-mate-18.04'
iso_name  = 'ubuntu-18.04.1-desktop-amd64.iso'
vdi_file  = 'ubuntu-18.04-amd64.vdi'
iso_file  = '/sda3/VirtualBoxVMs/' + iso_name


# 使用 時間日期格式當作版本 ver 
ver = time.strftime('%Y%m%d.%H%M',time.localtime(time.time() - 0*60*60) )
out_iso   = '/isodevice/_ISO/LINUX/ubuntu.1804-' + ver + '.iso'


window = Tk()
window.title( "Diy ubuntu-18.04")
window.geometry('1000x780')

sButton = [None] *  500
cButton = [None] *  500
sLabel  = [None] *  500



def get_flag_id(id):
    return "tmp/chk_flag_id_" + str(id)


def clean_me(id):
    global sLabel
    sLabel[id].config(fg="black")
    os.popen("rm -f " + get_flag_id(id) )



os.popen("mkdir -p tmp")
os.popen("mkdir -p ubuntu_chroot/bin")
os.popen("mkdir -p ubuntu_chroot/etc/apt")
os.popen("mkdir -p ubuntu_chroot/etc/xdg/autostart")
os.popen("mkdir -p ubuntu_chroot/root")
os.popen("mkdir -p ubuntu_chroot/usr/bin")
os.popen("mkdir -p ubuntu_chroot/user/local/bin")
os.popen("mkdir -p ubuntu_chroot/usr/local/lib/python3.5")
os.popen("mkdir -p ubuntu_chroot/usr/share/backgrounds/mate/nature")
os.popen("mkdir -p ubuntu_deb")

os.popen("sudo chmod a+rw -R ubuntu_chroot")
os.popen("sudo chmod a+rw -R ubuntu_deb")




sourceslist = """
deb http://archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse
deb http://security.ubuntu.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ bionic-updates main restricted universe multiverse
"""
fp = open("ubuntu_chroot/etc/apt/sources.list",'w')
fp.write(sourceslist)
fp.close


chewingDesktop = """[Desktop Entry]
Type=Application
Name=Autostart Script
Exec=chewing
Icon=system-run
X-GNOME-Autostart-enabled=true
Name[en_US]=chewing.desktop
"""
fp = open("ubuntu_chroot/etc/xdg/autostart/chewing.desktop",'w')
fp.write(chewingDesktop)
fp.close



chewing  = """#!/bin/bash
sudo locale-gen zh_TW.UTF-8
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('ibus', 'chewing'), ('ibus', 'table:cangjie3')]"
gsettings set org.gnome.shell favorite-apps "['firefox.desktop', 'org.gnome.Nautilus.desktop']"
gsettings set org.gnome.nautilus.preferences executable-text-activation "ask"
gsettings set org.gnome.desktop.screensaver idle-activation-enabled false
gsettings set org.gnome.desktop.session idle-delay 0
gsettings set org.gnome.settings-daemon.plugins.media-keys terminal '<Primary><Alt>t'


touch ~/Templates/New_Document

sudo mkdir -p /var/www/html/test
sudo chmod a+rwx -R /var/www/html/test
xrandr --output HDMI-1 --primary
xrandr -s 1280x960

mount_device () 
{
    if [ -e /dev/$1 ]
    then

        sudo umount /dev/$1
        sudo mkdir /$2
        sudo mount /dev/$1 /$2
        #sudo chown -R ubuntu:ubuntu /$2
        echo "file:///"$2 $2  >>   /home/ubuntu/.config/gtk-3.0/bookmarks
    fi
}

mount_device sda3 sda3
mount_device sdb1 ssd

"""
fp = open("ubuntu_chroot/bin/chewing",'w')
fp.write(chewing)
fp.close


dns = """nameserver 168.95.1.1"""
fp = open("ubuntu_chroot/etc/resolv.conf",'w')
fp.write(dns)
fp.close

dns = """nameserver 168.95.1.1"""
fp = open("ubuntu_chroot/etc/resolv.conf",'w')
fp.write(dns)
fp.close



os.popen("sudo chmod a+rw -R ubuntu_chroot")
os.popen("sudo chmod a+rw -R ubuntu_deb")




### @@@ 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####



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





xx = 20
yy = 20 - 35
id = 0


#########################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 建立 VDI 檔案"
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

sleep 3
exit
""".replace("VDI_FILE",vdi_file) 
layButton(id,xx,yy,actionText,runCommand)


#########################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 掛載 VDI 檔案 至 livecd 目錄"
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

sleep 5

""" %(vdi_file)
layButton(id,xx,yy,actionText,runCommand)



#########################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 解開 ISO 檔案至 /livecd  "
runCommand = """#!/bin/bash
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
yy = yy + 35
id = id + 1
actionText = str(id) + ") 複製 客製化 檔案至 /livecd"
runCommand = """#!/bin/bash
cp -R  ubuntu_chroot/* /livecd/isonew/custom/
sync;sync;sync;

echo 執行 複製客製化檔案至 /livecd 完成
sleep 3
"""
layButton(id,xx,yy,actionText,runCommand)


#########################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 複製 DEBs 檔案至 /livecd"
runCommand = """#!/bin/bash
cp -R ubuntu_deb/* /livecd/isonew/custom/root/
sync;sync;sync;

echo 執行 複製 DEBs 檔案至 /livecd 完成
sleep 3
"""
layButton(id,xx,yy,actionText,runCommand)


#########################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 複製 DEBs 檔案至 ubuntu 暫存目錄"
runCommand = """#!/bin/bash
cp -R /livecd/isonew/custom/var/cache/apt/archives/*.deb ubuntu_deb/
sync;sync;sync;

echo 複製 完成
sleep 3
"""
layButton(id,xx,yy,actionText,runCommand)










yy = 300
#########################################################
### 工具區 nmon
#########################################################

yy = yy + 35
id = id + 1
actionText = str(id) + ") nmon"
runCommand = """#!/bin/bash
nmon
"""
layButton(id,xx,yy,actionText,runCommand)



#########################################################
### 工具區 df -m
#########################################################

yy = yy + 35
id = id + 1
actionText = str(id) + ") df -m"
runCommand = """#!/bin/bash
watch -n 2 df -m
"""
layButton(id,xx,yy,actionText,runCommand)


#########################################################
### 工具區 Reboot
#########################################################

yy = yy + 35
id = id + 1
actionText = str(id) + ") reboot"
runCommand = """#!/bin/bash
sync;sync;sync;reboot
"""
layButton(id,xx,yy,actionText,runCommand)




#########################################################
### 基本區 封裝 ISO 檔案
#########################################################


yy = yy + 35 + 35
id = id + 1
actionText = str(id) + ") 封裝 ISO 檔案"
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







### @@@ END END END 呼叫外部命令區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####



























### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####
### @@@ Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####


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





### 開始 chroot 安裝
def hit_chroot(id,runCommand):
    global sLabel,root_fold
    sLabel[id].config(fg="red")
    os.popen("touch " + get_flag_id(id) )

    install_code = """#!/bin/bash
        mount -t proc none /proc
        mount -t sysfs none /sys
        export HOME=/root
        cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime

        # chmod 755 /usr/bin/phantomjs
        # chmod 755 /usr/local/bin/geckodriver

        apt-get update

        %s

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
    sleep 5
    """

    file_name = "CommandLine_" + str(id) + ".sh"

    f = open( "tmp/" + file_name , 'w', encoding = 'UTF-8')
    f.write(execCommand)
    f.close()

    os.popen("chmod 755 tmp/" + file_name)
    os.popen("sudo mate-terminal -x bash -c 'sh tmp/" + file_name + "' ")







xx = 500
yy = 20 - 35

#########################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 設定 /bin/基本檔案 755 權限"
runCommand = """
clear
cd /bin
pwd
chmod 755 chewing
ls chewing -l
sleep 3
"""
chrootButton(id,xx,yy,actionText,runCommand)


#########################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 root/*.deb"
runCommand = """
cd /root
dpkg -i *.deb
"""
chrootButton(id,xx,yy,actionText,runCommand)


#########################################################
yy = yy + 35 + 35
id = id + 1
actionText = str(id) + ") 安裝 VirtualBox 所有工具"
runCommand = """
apt-get -y install virtualbox virtualbox-guest-utils virtualbox-guest-additions-iso virtualbox-qt squashfs-tools qemu
"""
chrootButton(id,xx,yy,actionText,runCommand)




### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 網路工具"
runCommand = """
apt-get -y install firefox uget curl remmina remmina-plugin-rdp remmina-plugin-vnc etherape lynx nbtscan net-tools nmap putty
"""
chrootButton(id,xx,yy,actionText,runCommand)


### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 一般工具"
runCommand = """
apt-get -y install ubuntu-restricted-extras winff grsync clonezilla kazam mdadm shutter gnome-raw-thumbnailer ufraw-batch encfs k4dirstat nmon language-pack-zh-hant expect gimp git ibus ibus-chewing ibus-table-cangjie libreoffice-l10n-zh-tw libreoffice-pdfimport p7zip p7zip-full p7zip-rar libjpeg62 smplayer mate-terminal dconf-editor 
apt-get -y install qml-module-qtquick-layouts qml-module-qtquick2 qml-module-qtquick-controls qml-module-qtquick-dialogs qml-module-qtquick-window2
"""
chrootButton(id,xx,yy,actionText,runCommand)

### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 更新 python"
runCommand = """
# apt-get -y install scrot python-pip  python-tk       
apt-get -y install python3-pip python3-tk python3-dev scrot

# python3 -m pip install --upgrade pip
python3 -m pip install selenium
python3 -m pip install python3-xlib
python3 -m pip install pymongo
python3 -m pip install beautifulsoup4

# python -m pip install --upgrade pip
# python -m pip install selenium
# python -m pip install python-xlib
# python -m pip install pymongo
"""
chrootButton(id,xx,yy,actionText,runCommand)


### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 ssh-server samba lamp"
runCommand = """
apt-get -y install tasksel openssh-server samba system-config-samba apache2 php7.2 php7.2-sqlite3  apache2-dev php7.2-ldap php7.2-curl sqlite3 

# apt-get -y install tasksel openssh-server samba system-config-samba 
# tasksel install lamp-server
# apt-get -y install php7.0-sqlite3 sqlite3 php7.0-mysql apache2-dev 
# apt-get -y install php-mongodb mongodb php-mongodb mongodb
"""
chrootButton(id,xx,yy,actionText,runCommand)



### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 mysql"
runCommand = """
cd /tmp
wget https://repo.mysql.com//mysql-apt-config_0.8.12-1_all.deb
dpkg -i mysql-apt-config_0.8.12-1_all.deb
apt-get -y install mysql-client mysql-server mysql-workbench
"""
chrootButton(id,xx,yy,actionText,runCommand)




### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 模擬器"
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



### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 Sublime/MS sqlcmd/Chrome/H264"
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
# wget http://h264.code-shop.com/download/apache_mod_h264_streaming-2.2.7.tar.gz
# tar -zxvf apache_mod_h264_streaming-2.2.7.tar.gz

# cd mod_h264_streaming-2.2.7
# ./configure --with-apxs=`which apxs2`
# make
# make install
# echo 'LoadModule h264_streaming_module /usr/lib/apache2/modules/mod_h264_streaming.so' >> /etc/apache2/apache2.conf
# echo 'AddHandler h264-streaming.extensions .mp4' >> /etc/apache2/apache2.conf

cd /tmp
wget http://h264.code-shop.com/download/apache_mod_h264_streaming-2.2.7.tar.gz
tar -zxvf apache_mod_h264_streaming-2.2.7.tar.gz
cd mod_h264_streaming-2.2.7

./configure
make
make install

echo 'LoadModule h264_streaming_module /usr/lib/apache2/modules/mod_h264_streaming.so' >> /etc/apache2/mods-available/php7.2.load
echo 'AddHandler h264-streaming.extensions .mp4'                                       >> /etc/apache2/mods-available/php7.2.load
"""
chrootButton(id,xx,yy,actionText,runCommand)



### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 joystick keyboard 對應"
runCommand = """
apt-get -y install gdebi
wget 'https://launchpad.net/~mdeguzis/+archive/ubuntu/libregeek/+files/antimicro_2.23~artful-1_amd64.deb'
echo y | gdebi antimicro*.deb

# add-apt-repository ppa:mdeguzis/libregeek
# apt-get update
# apt-get install antimicro
"""
chrootButton(id,xx,yy,actionText,runCommand)




### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 VMWare"
runCommand = """
cd /root
chmod 755 VMware-Workstation-Full-14.1.1-7528167.x86_64.bundle
./VMware-Workstation-Full-14.1.1-7528167.x86_64.bundle --custom
"""
chrootButton(id,xx,yy,actionText,runCommand)



### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 安裝 Horizon-Client"
runCommand = """
cd /root
chmod 755 VMware-Horizon-Client-4.8.0-8518891.x64.bundle
./VMware-Horizon-Client-4.8.0-8518891.x64.bundle --console
"""
chrootButton(id,xx,yy,actionText,runCommand)



### ubuntu-mate 16.04 ######################################################
yy = yy + 35
id = id + 1
actionText = str(id) + ") 清除暫存區域 & chmod 755"
runCommand = """
apt --fix-broken -y install
apt-get clean
chmod 755 /bin/chewing
rm -rf /root/*
rm -rf /tmp/*
"""
chrootButton(id,xx,yy,actionText,runCommand)













### @@@ END END END  Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####

window.mainloop()


