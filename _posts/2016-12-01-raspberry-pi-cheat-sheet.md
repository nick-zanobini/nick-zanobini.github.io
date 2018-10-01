---
layout: single
title: 	Raspberry Pi Cheat Sheet
comments: true
date: 	2016-12-01 05:58:35
tags:	raspberrypi tips linux
---

### List all devices connected to the network

{% highlight bash %}
arp -a
{% endhighlight %} 

### Setup Wi-Fi from the command line

Open the `wpa-supplicant` configuration file in nano:

{% highlight bash %}
sudo nano /etc/wpasupplicant/wpasupplicant.conf
{% endhighlight %} 

Go to the bottom of the file and add the following:

{% highlight bash %}
network={
    ssid="Yourwifiname"
    psk="Yourwifipassword"
}
{% endhighlight %} 

Now save the file by pressing Ctrl+X then Y, then finally press Enter.

To ensure it takes effect reboot your Raspberry Pi or restart the Wi-Fi interface

{% highlight bash %}
sudo reboot
{% endhighlight %} 

or 

{% highlight bash %}
sudo ifdown wlan0
sudo ifup wlan0
{% endhighlight %} 

You can verify if it has successfully connected using `ifconfig wlan0`. If the `inet addr` field has an address beside it, the Pi has connected to the network. If not, check your password and ESSID are correct.

[Source](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)

### SSH into your Raspberry Pi as root

Login, and edit this file:
{% highlight bash %}
sudo nano /etc/ssh/sshdconfig
{% endhighlight %} 

Find `PermitRootLogin without-password`: and change it to `PermitRootLogin yes`

Now close and save the file by pressing Ctrl+X then Y, then finally press Enter.
To ensure it takes effect either reboot your Raspberry Pi or the SSHD service

{% highlight bash %}
sudo reboot
sudo /etc/init.d/ssh restart {% endhighlight %} 
Now you can login as root, but I recommend you using strong password or ssh-keys

[Source](http://raspberrypi.stackexchange.com/questions/48056/login-as-root-not-possible)

### Setup and Install Zeroconf

Zeroconfig allows you to access your Raspberry Pi using the hostname instead of the IP address.
`RPi0.local` instead of `192.168.0.XX`

Zeroconf is provided through an optional package called Avahi.

It’s super easy to install from the command line:

{% highlight bash %}
sudo apt-get install avahi-daemon
{% endhighlight %} 

This takes about five minutes. Once installed, the system can be contacted from other computers at hostname.local, where hostname is either the default (raspberrypi) or an alternate name assigned by:

{% highlight bash %}
sudo raspi-config
{% endhighlight %}

If the system will be sharing a network with any Mac computers, I like to install Netatalk:

{% highlight bash %}
sudo apt-get install netatalk
{% endhighlight %} 

This adds support for Apple Filing Protocol, making it easy to move files back and forth in the Finder.
[Source](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)


### Flip Touchscreen 180 Degrees

You need to edit the config file `/boot/config.txt` and add the line `lcd_rotate=2`


### Enable SSH on Headless Pi

After burning Raspian to your SD card go to the boot folder on the SD card and create a blank file `ssh` with no extension. 



