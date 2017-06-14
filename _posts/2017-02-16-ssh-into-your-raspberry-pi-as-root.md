---
author: nickzanobini
comments: true
date: 2017-02-16 04:47:31
layout: post
title: SSH into your Raspberry Pi as root
---

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
