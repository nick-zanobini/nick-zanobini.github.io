---
layout: post
title: Raspberry Pi Cheat Sheet
date: 2016-12-01 05:58
author: nickzanobini
comments: true
categories: [Uncategorized]
---
<h3>List all devices connected to the network</h3>

[code language="bash" light="true"]arp -a
[/code]

<h3>Setup Wi-Fi from the command line</h3>

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

<h3>SSH into your Raspberry Pi as root</h3>

Login, and edit this file:
[code language="bash" light="true"]sudo nano /etc/ssh/sshd_config
[/code]

<p dir="ltr">Find <code>PermitRootLogin without-password</code>: and change it to <code>PermitRootLogin yes</code></p>

<p dir="ltr">Now close and save the file by pressing Ctrl+X then Y, then finally press Enter.
To ensure it takes effect either reboot your Raspberry Pi or the SSHD service</p>

[code language="bash" light="true"]sudo reboot
sudo /etc/init.d/ssh restart [/code]
Now you can login as root, but I recommend you using strong password or ssh-keys

<p dir="ltr"><a href="http://raspberrypi.stackexchange.com/questions/48056/login-as-root-not-possible" target="_blank">Source</a></p>

<h3>Setup and Install Zeroconf</h3>

<p dir="ltr">Zeroconfig allows you to access your Raspberry Pi using the hostname instead of the IP address.
<code>RPi0.local</code> instead of <code>192.168.0.XX</code></p>

<p dir="ltr">Zeroconf is provided through an optional package called <em>Avahi.</em></p>

<p dir="ltr">It’s super easy to install from the command line:</p>

[code language="bash" light="true"]sudo apt-get install avahi-daemon
[/code]

<p dir="ltr">This takes about five minutes. Once installed, the system can be contacted from other computers at <em>hostname.</em>local, where hostname is either the default (raspberrypi) or an alternate name assigned by:</p>

[code language="bash" light="true"]sudo raspi-config
[/code]
If the system will be sharing a network with any Mac computers, I like to install <em>Netatalk:</em>
[code language="plain" light="true"]sudo apt-get install netatalk
[/code]

<p dir="ltr">This adds support for <em>Apple Filing Protocol,</em> making it easy to move files back and forth in the Finder.
<a href="https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview" target="_blank">Source</a></p>
