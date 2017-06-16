---
layout: single
title: 	SSH into your Raspberry Pi as root
date: 	2017-02-16 04:47:31
tags:	linux raspberrypi
comments: true
---

Login, and edit this file:
{% highlight bash %}
sudo nano /etc/ssh/sshd_config
{% endhighlight %} 

Find `PermitRootLogin without-password`: and change it to `PermitRootLogin yes`

Now close and save the file (by pressing Ctrl+X then Y, then finally press Enter).
To ensure it takes effect either reboot your Raspberry Pi or the SSHD service

{% highlight bash %}
sudo reboot
sudo /etc/init.d/ssh restart 
{% endhighlight %} 

Now you can login as root, but I recommend you using strong password or ssh-keys


[Source](http://raspberrypi.stackexchange.com/questions/48056/login-as-root-not-possible)
