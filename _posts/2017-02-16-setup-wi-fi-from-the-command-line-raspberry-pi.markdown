---
author: nickzanobini
comments: true
date: 2017-02-16 04:45:23+00:00
layout: post
link: https://nickzanobini.wordpress.com/2017/02/16/setup-wi-fi-from-the-command-line-raspberry-pi/
slug: setup-wi-fi-from-the-command-line-raspberry-pi
title: Setup Wi-Fi from the Command Line on a Raspberry Pi
wordpress_id: 641
---

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
