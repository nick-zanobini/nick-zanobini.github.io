---
layout: post
title: SSH into your Raspberry Pi as root
date: 2017-02-16 04:47
author: nickzanobini
comments: true
categories: [Uncategorized]
---
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
