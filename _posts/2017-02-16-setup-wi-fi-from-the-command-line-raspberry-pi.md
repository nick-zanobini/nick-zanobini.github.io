---
layout: single
comments: true
date: 	2017-02-16 04:45:23
title: 	Setup Wi-Fi from the Command Line on a Raspberry Pi
tags:	raspberrypi tips linux
---

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
