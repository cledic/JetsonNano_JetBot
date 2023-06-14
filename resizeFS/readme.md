
# Installazione Jetpack e comando resize del FileSystem


https://forums.developer.nvidia.com/t/jetbot-software-setup-jetpack-4-5-1-version/178724/4

```
cd ~/jetcard
git pull
git checkout jetpack_4.5.1
./script/jetson_install_nvresizefs_service.sh
cd
rm -rf jetcard
sudo reboot
```
