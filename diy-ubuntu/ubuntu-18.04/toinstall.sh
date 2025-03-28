#!/bin/bash

cd /tmp/deb
mount none -t proc /proc
mount none -t sysfs /sys   
mount none -t devpts /dev/pts   
export HOME=/root   
export LC_ALL=C

apt remove -y --purge ubiquity*
apt remove -y --purge libreoff*
apt remove -y --purge firefox*
apt remove -y --purge thunderbird*
apt remove -y --purge rhythmbox*
apt remove -y --purge chees*
apt remove -y --purge gnome-mahjongg*
apt remove -y --purge gnome-mines*
apt remove -y --purge gnome-sudoku*
apt remove -y --purge aisleriot*

dpkg -i *.deb

#umount /proc
#umount /sys
#umount /dev/pts
exit



