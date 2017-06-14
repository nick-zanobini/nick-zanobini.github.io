---
author: nickzanobini
comments: true
date: 2017-02-15 04:33:30+00:00
layout: post
link: https://nickzanobini.wordpress.com/2017/02/15/connecting-a-readyshare-media-server-to-osmc-on-a-raspberry-pi/
slug: connecting-a-readyshare-media-server-to-osmc-on-a-raspberry-pi
title: Connecting a ReadyShare Media Server to OSMC on a Raspberry Pi
wordpress_id: 625
---

I have OSMC installed on a Raspberry Pi 2, and a Netgear router with a 3TB HDD attached. I store all my movies and TV shows on the hard drive and wanted to add them to OSMC.

Connect to your Media Center via SSH.

First I made a folder for both TV Shows and Movies on my Raspberry Pi.

[code lang=bash]
sudo mkdir /media/Movies
sudo mkdir /media/TVShows
[/code]

Next, to mount my ReadyShare media server as a media source to the Raspberry Pi. My hard drive is connected as the T_Drive so I will mount that. Change this to match your configuration.

[code lang=bash]
sudo mount -t cifs //192.168.0.1/T_Drive/Movies /media/Movies -o username=admin,password=password
[/code]

**_OR_**

[code lang=bash]
sudo mount -t cifs //readyshare/T_Drive/Movies /media/Movies -o username=admin,password=password
[/code]

My router IP address is 192.168.0.1. Change this to match your router or just use //readyshare instead.

Now you will be able to add **both** TVShows and Movies as a media source on your Raspberry Pi.
