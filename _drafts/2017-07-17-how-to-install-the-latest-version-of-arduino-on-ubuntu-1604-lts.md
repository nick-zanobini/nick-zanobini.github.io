#### Note: This example is done with the 64-bit version Arduino 1.8.3. The latest version may be different and the below instructions may need to be altered ever so slightly.

1. Download the latest packages, Linux 32-bit or Linux 64-bit, from the official link: [www.arduino.cc/en/Main/Software](www.arduino.cc/en/Main/Software)  

Don’t know your OS type? Go and check out System Settings -> Details -> Overview.

2. Open terminal from Unity Dash, App Launcher, or via Ctrl+Alt+T keys. When it opens, run below commands one by one:

```
# Navigate to your downloads folder:
cd ~/Downloads
# Decompress the downloaded archive with tar command:
tar -xvf arduino-1.8.3-linux64.tar.xz
# Move the result folder to /opt/ directory for global use:
sudo mv arduino-1.8.3 /opt
```

3. Now the IDE is ready for use with bundled Java. But it would be good to create desktop icon/launcher for the application:

```
# Navigate to install folder
cd /opt/arduino-1.8.3
# Give executable permission to install.sh script in that folder
sudo chmod +x install.sh
# Finally run the script to install both desktop shortcut and launcher icon
./install.sh
```

Finally, launch Arduino IDE from Unity Dash, Application Launcher, or via Desktop shorcut.