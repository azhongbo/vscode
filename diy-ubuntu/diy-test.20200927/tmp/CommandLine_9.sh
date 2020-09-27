
cd /livecd/isonew/cd
mkisofs -r -V "UbuntuLiveCD" -b isolinux/isolinux.bin -c isolinux/boot.cat -cache-inodes -J -l -no-emul-boot -boot-load-size 4 -boot-info-table -o /sda2/e2b/_ISO/LINUX/klcppp-1804-20200918.2137.iso .

sync;sync;sync;
sleep 1
