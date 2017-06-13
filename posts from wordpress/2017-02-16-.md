---
layout: post
title: Setup and Install Zeroconf on a Raspberry Pi
date: 2017-02-16 04:48
author: nickzanobini
comments: true
categories: [Uncategorized]
---
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
