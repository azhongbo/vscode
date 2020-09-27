#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,time,datetime,time,re
from tkinter import *


# 使用 時間日期格式當作版本 ver 
ver = time.strftime('%Y%m%d.%H%M',time.localtime(time.time() - 0*60*60) )

ubuntu_iso     = f"/sda2/e2b/_ISO/LINUX/ubuntu-18.04.4-desktop-amd64.iso"
ubuntu_new_iso = f"/sda2/e2b/_ISO/LINUX/klcppp-1804-{ver}.iso"



id = 0
xx = 0
yy = 0

window = Tk()
window.title( "Diy ubuntu-18.04")
window.geometry('1000x780')

sButton = [None] *  500
cButton = [None] *  500
sLabel  = [None] *  500

os.popen("mkdir -p tmp")


def get_flag_id(id):
    return "tmp/chk_flag_id_" + str(id)


def layButton(xx,yy,actionText,runCommand):
    global sButton,sLabel,id

    id = id + 1

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

def get_flag_id(id):
    return "tmp/chk_flag_id_" + str(id)

def clean_me(id):
    global sLabel
    sLabel[id].config(fg="black")
    os.popen("rm -f " + get_flag_id(id) )





xx = 20
yy = 20 - 35


#########################################################
yy+=35
layButton(xx,yy,
"建立 mnon",
"""
nmon
""")



#########################################################
yy+=35
layButton(xx,yy,
"建立 nvidia-smi ",
"""
watch -n 2 nvidia-smi
""")

#########################################################
yy+=35
layButton(xx,yy,
"檔案總管-開啟 /livecd ",
"""
#sudo nautilus /livecd
gnome-terminal -e 'nautilus /livecd'
""")










#########################################################
yy+=35*2
layButton(xx,yy,
"format /dev/sdb (SSD硬碟)",
"""
echo "d
n
p
1


w
" | fdisk /dev/sdb
mkfs.ext4 -F /dev/sdb1
""")

#########################################################
yy+=35
layButton(xx,yy,
"掛載 /dev/sdb1 /livecd (SSD)",
"""
mkdir /livecd
mount /dev/sdb1 /livecd
mount /dev/sdb1 /livecd


mkdir -p /livecd/isomount /livecd/isonew/squashfs
mkdir -p /livecd/isomount /livecd/isonew/cd
mkdir -p /livecd/isomount /livecd/isonew/custom
""")

#########################################################
yy+=35
layButton(xx,yy,
"卸載 /dev/sdb1 /livecd (SSD)",
"""
umount /livecd/isonew/squashfs 
umount /livecd/isonew/squashfs 
umount /livecd/isomount
umount /livecd/isomount
umount /livecd
umount /livecd
""")



#########################################################
yy+=35
layButton(xx,yy,
"解壓縮 Ubuntu ISO",
f"""
mount -o loop,ro {ubuntu_iso} /livecd/isomount
rsync --exclude=/livecd/isomount/casper/filesystem.squashfs -avP /livecd/isomount/ /livecd/isonew/cd/
modprobe squashfs
mount -t squashfs -o loop /livecd/isomount/casper/filesystem.squashfs /livecd/isonew/squashfs
rsync -avP /livecd/isonew/squashfs/ /livecd/isonew/custom/
umount /livecd/isonew/squashfs 
umount /livecd/isomount
sync;sync;sync;
""")



#########################################################
yy+=35
layButton(xx,yy,
"封裝 filesystem.squashfs",
f"""
rm /livecd/isonew/cd/casper/filesystem.squashfs

cd /livecd
chmod +w /livecd/isonew/cd/casper/filesystem.manifest
mksquashfs /livecd/isonew/custom /livecd/isonew/cd/casper/filesystem.squashfs

sync;sync;sync;
sleep 1
""")


#########################################################
yy+=35
layButton(xx,yy,
"封裝 新ISO",
f"""
cd /livecd/isonew/cd
mkisofs -r -V "UbuntuLiveCD" -b isolinux/isolinux.bin -c isolinux/boot.cat -cache-inodes -J -l -no-emul-boot -boot-load-size 4 -boot-info-table -o {ubuntu_new_iso} .

sync;sync;sync;
chmod a+rw /sda2/e2b/_ISO/LINUX/*
sleep 1
""")



#########################################################
yy+=35
layButton(xx,yy,
"建立開機 E2B 至 /dev/sda1",
f"""
cd /sda2/e2b/_ISO/docs/linux_utils
./fmt_ntfs.sh

sleep 1
""")








### @@@ END END END  Chroot 區域 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ####

window.mainloop()


