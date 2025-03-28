#!/bin/bash

#sudo apt update && sudo apt upgrade
#sudo apt install squashfs-tools genisoimage isolinux xorriso dumpet gddrescue

iso_file="ubuntu-18.04.4-desktop-amd64.iso"

mkdir /custom/iso
mkdir /custom/livecd
sudo mount -o loop /custom/$iso_file /custom/iso
cp -rT /custom/iso /custom/livecd
unsquashfs -d /custom/squashfs /custom/livecd/casper/filesystem.squashfs
mkdir /custom/squashfs/tmp/deb

cp /custom/packages/deb/* /custom/squashfs/tmp/deb/
cp -R /custom/packages/python3.6/dist-packages/ /custom/squashfs/usr/local/lib/python3.6/
cp /custom/toinstall.sh /custom/squashfs/tmp/

sudo chroot /custom/squashfs /tmp/toinstall.sh
umount -f /custom/squashfs/proc /custom/squashfs/sys  /custom/squashfs/dev/pts

rm /custom/livecd/casper/filesystem.squashfs
mksquashfs /custom/squashfs /custom/livecd/casper/filesystem.squashfs
echo $(du -sx --block-size=1 /custom/livecd/casper/filesystem.squashfs) > /custom/livecd/casper/filesystem.size
rm /custom/livecd/md5sum.txt
sh -c "cd /custom/livecd && find . -type f -print0 | xargs -0 md5sum > md5sum.txt"
xorriso -as mkisofs -D -r -V CustomUbuntu -cache-inodes -J -l -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -J -joliet-long -eltorito-alt-boot -e boot/grub/efi.img -no-emul-boot -isohybrid-gpt-basdat -isohybrid-apm-hfsplus -o custom-$iso_file /custom/livecd
chmod a+rw custom-$iso_file

# mkdir /custom/iso
# mkdir /custom/livecd
# sudo mount -o loop /custom/ubuntu-18.04.4-desktop-amd64.iso /custom/iso
# cp -rT /custom/iso /custom/livecd
# sudo unsquashfs -d /custom/squashfs /custom/livecd/casper/filesystem.squashfs
# mkdir /custom/squashfs/tmp/deb

# cp /custom/packages/deb/* /custom/squashfs/tmp/deb/
# cp -R /custom/packages/python3.6/dist-packages/ /custom/squashfs/usr/local/lib/python3.6/
# cp /custom/toinstall.sh /custom/squashfs/tmp/

# sudo chroot /custom/squashfs /tmp/toinstall.sh

# rm -rf /custom/livecd
# cp -rT /custom/iso /custom/livecd
# umount -f /custom/squashfs/proc /custom/squashfs/sys  /custom/squashfs/dev/pts
# rm /custom/livecd/casper/filesystem.squashfs

# mksquashfs /custom/squashfs /custom/livecd/casper/filesystem.squashfs
# echo $(du -sx --block-size=1 /custom/livecd/casper/filesystem.squashfs) > /custom/livecd/casper/filesystem.size
# rm /custom/livecd/md5sum.txt
# sh -c "cd /custom/livecd && find . -type f -print0 | xargs -0 md5sum > md5sum.txt"
# xorriso -as mkisofs -D -r -V CustomUbuntu -cache-inodes -J -l -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -J -joliet-long -eltorito-alt-boot -e boot/grub/efi.img -no-emul-boot -isohybrid-gpt-basdat -isohybrid-apm-hfsplus -o old6-ubuntu-18.04.4-desktop2-amd64.iso /custom/livecd
