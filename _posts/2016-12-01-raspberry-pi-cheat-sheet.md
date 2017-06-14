---
layout: single
author: nickzanobini
comments: true
date: 2016-12-01 05:58:35
layout: post
title: Raspberry Pi Cheat Sheet
---

### List all devices connected to the network



[code language="bash" light="true"]arp -a
[/code]



### Setup Wi-Fi from the command line





Open the `wpa-supplicant` configuration file in nano:



[code language="bash" light="true"]sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
[/code]



Go to the bottom of the file and add the following:



[code language="plain" light="true"]
network={
    ssid="Your_wifi_name"
    psk="Your_wifi_password"
}
[/code]
Now save the file by pressing Ctrl+X then Y, then finally press Enter.



To ensure it takes effect reboot your Raspberry Pi or restart the Wi-Fi interface



[code language="bash" light="true"]sudo reboot
sudo ifdown wlan0
sudo ifup wlan0[/code]



You can verify if it has successfully connected using `ifconfig wlan0`. If the `inet addr` field has an address beside it, the Pi has connected to the network. If not, check your password and ESSID are correct.





[Source](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)





### SSH into your Raspberry Pi as root



Login, and edit this file:
[code language="bash" light="true"]sudo nano /etc/ssh/sshd_config
[/code]



Find `PermitRootLogin without-password`: and change it to `PermitRootLogin yes`





Now close and save the file by pressing Ctrl+X then Y, then finally press Enter.
To ensure it takes effect either reboot your Raspberry Pi or the SSHD service



[code language="bash" light="true"]sudo reboot
sudo /etc/init.d/ssh restart [/code]
Now you can login as root, but I recommend you using strong password or ssh-keys



[Source](http://raspberrypi.stackexchange.com/questions/48056/login-as-root-not-possible)





### Setup and Install Zeroconf





Zeroconfig allows you to access your Raspberry Pi using the hostname instead of the IP address.
`RPi0.local` instead of `192.168.0.XX`





Zeroconf is provided through an optional package called _Avahi._





It’s super easy to install from the command line:



[code language="bash" light="true"]sudo apt-get install avahi-daemon
[/code]



This takes about five minutes. Once installed, the system can be contacted from other computers at _hostname._local, where hostname is either the default (raspberrypi) or an alternate name assigned by:



[code language="bash" light="true"]sudo raspi-config
[/code]
If the system will be sharing a network with any Mac computers, I like to install _Netatalk:_
[code language="plain" light="true"]sudo apt-get install netatalk
[/code]



This adds support for _Apple Filing Protocol,_ making it easy to move files back and forth in the Finder.
[Source](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)
