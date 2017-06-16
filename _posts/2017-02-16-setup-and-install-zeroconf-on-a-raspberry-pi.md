---
layout: single
comments: true
date: 	2017-02-16 04:48:24
title: 	Setup and Install Zeroconf on a Raspberry Pi
tags:	raspberrypi tips linux
---

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
