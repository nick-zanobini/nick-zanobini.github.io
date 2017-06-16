---
layout: single
comments: true
date: 	2017-02-15 04:33:30
title: 	Connecting a ReadyShare Media Server to OSMC on a Raspberry Pi
tags: raspberrypi router ReadyShare hdd external linux OSMC
---

I have OSMC installed on a Raspberry Pi 2, and a Netgear router with a 3TB HDD attached. I store all my movies and TV shows on the hard drive and wanted to add them to OSMC.

Connect to your Media Center via SSH.

First I made a folder for both TV Shows and Movies on my Raspberry Pi.

{% highlight bash %}
sudo mkdir /media/Movies
sudo mkdir /media/TVShows
{% endhighlight %} 

Next, to mount my ReadyShare media server as a media source to the Raspberry Pi. My hard drive is connected as the T_Drive so I will mount that. Change this to match your configuration.

{% highlight bash %}
sudo mount -t cifs //192.168.0.1/T_Drive/Movies /media/Movies -o username=admin,password=password
{% endhighlight %} 

**_OR_**

{% highlight bash %}
sudo mount -t cifs //readyshare/T_Drive/Movies /media/Movies -o username=admin,password=password
{% endhighlight %} 

My router IP address is 192.168.0.1. Change this to match your router or just use //readyshare instead.

Now you will be able to add **both** TVShows and Movies as a media source on your Raspberry Pi.
