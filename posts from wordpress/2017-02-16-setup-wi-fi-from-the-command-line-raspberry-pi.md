---
layout: post
title: Setup Wi-Fi from the Command Line on a Raspberry Pi
date: 2017-02-16 04:45
author: nickzanobini
comments: true
categories: [Uncategorized]
---
<p dir="ltr">Open the <code>wpa-supplicant</code> configuration file in nano:</p>

[code language="bash" light="true"]sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
[/code]

<p dir="ltr">Go to the bottom of the file and add the following:</p>

[code language="plain" light="true"]
network={
    ssid=&quot;Your_wifi_name&quot;
    psk=&quot;Your_wifi_password&quot;
}
[/code]
Now save the file by pressing Ctrl+X then Y, then finally press Enter.

<p dir="ltr">To ensure it takes effect reboot your Raspberry Pi or restart the Wi-Fi interface</p>

[code language="bash" light="true"]sudo reboot
sudo ifdown wlan0
sudo ifup wlan0[/code]

<p dir="ltr">You can verify if it has successfully connected using <code>ifconfig wlan0</code>. If the <code>inet addr</code> field has an address beside it, the Pi has connected to the network. If not, check your password and ESSID are correct.</p>

<p dir="ltr"><a href="https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md" target="_blank">Source</a></p>
