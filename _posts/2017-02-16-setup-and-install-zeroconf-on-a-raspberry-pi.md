---
layout: single
author: nickzanobini
comments: true
date: 2017-02-16 04:48:24
layout: post
title: Setup and Install Zeroconf on a Raspberry Pi
---

Zeroconfig allows you to access your Raspberry Pi using the hostname instead of the IP address.
`RPi0.local` instead of `192.168.0.XX`





Zeroconf is provided through an optional package called _Avahi._





It’s super easy to install from the command line:



[code language="bash" light="true"]sudo apt-get install avahi-daemon
[/code]



This takes about five minutes. Once installed, the system can be contacted from other computers at _hostname._local, where hostname is either the default (raspberrypi) or an alternate name assigned by:



[code language="bash" light="true"]sudo raspi-config
[/code]
If the system will be sharing a network with any Mac computers, I like to install _Netatalk:_
[code language="plain" light="true"]sudo apt-get install netatalk
[/code]



This adds support for _Apple Filing Protocol,_ making it easy to move files back and forth in the Finder.
[Source](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)
