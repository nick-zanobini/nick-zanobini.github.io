---
layout: post
title: Run a Python Scripts as a Service
date: 2016-12-01 05:30
author: nickzanobini
comments: true
categories: [linux, python, raspberrypi, rpi]
---
<p dir="auto">It is very common to run a python program as a service so it can start on boot, stop and restart using systemd. In this post I'm going to explain how to set a little script as a service using Raspbian Jessie on a <a href="https://www.raspberrypi.org/">Raspberry Pi</a> .</p>
<p dir="auto">To do this, we need a python program. We will use a simple Hello World script.</p>
[code language="python" light="true"]#!/usr/bin/python
from time import sleep
try:
	while True:
		print &quot;Hello World&quot;
		sleep(60)
except KeyboardInterrupt, e:
	break[/code]

 

Save this file to your home folder (<code>/home/pi/</code>) as <code>hello_world.py</code>.
<p dir="ltr">Next we are going to build our service. We need to create our service in the <code>/lib/systemd/system/</code> directory. To create the script using terminal run:</p>
[code language="bash" light="true"]sudo nano /lib/systemd/system/hello.service
[/code]

 

We will call our service <code>hello.service</code>

[code language="“bash”" light="“true”"]
[Unit]
Description=Hello World		#Name of your service
After=multi-user.target 

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/hello_world.py		#Path to your python script
Restart=on-abort		#restart options see below
[Install]
WantedBy=multi-user.target
[/code]

<code>[Unit]
Description=Hello World      #Name of your service
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/hello_world.py     #Path to your python script
Restart=on-abort #restart options see below

[Install]
WantedBy=multi-user.target </code>

Now save the file by pressing Ctrl+X then Y, then finally press Enter.
<p dir="ltr">The <code>Restart=</code> configures whether the service shall be restarted when the service process exits, is killed, or a timeout is reached. It can be set to one of the following: <code>no</code>, <code>on-success</code>, <code>on-failure</code>, <code>on-abnormal</code>, <code>on-watchdog</code>, <code>on-abort</code>, or <code>always</code>. For the details on each option see the Service Restart Options below.</p>
Now that we have our service we need to activate it:

[code language="bash" light="true"]sudo chmod 644 /lib/systemd/system/hello.service
chmod +x /home/pi/hello_world.py
sudo systemctl daemon-reload
sudo systemctl enable hello.service
sudo systemctl start hello.service
[/code]

 

Every time you change a file in the <em><code>/lib/systemd/system</code></em> folder we have to run <code>/lib/systemd/system</code>.
<p dir="ltr">To check the status of of the service you can run:</p>
[code language="bash" light="true"]sudo systemctl status hello.service
[/code]

 
<p dir="ltr">To restart the service you can run:</p>
[code language="bash" light="true"]sudo systemctl restart  hello.service
[/code]

 
<p dir="ltr">To stop the service you can run:</p>
[code language="bash" light="true"]sudo systemctl stop  hello.service[/code]

To start the service you can run:

[code language="bash" light="true"]sudo systemctl start  hello.service[/code]

 
<h3>Service Restart Options</h3>
<p dir="ltr">If set to <code>no</code> (the default), the service will not be restarted. If set to <code>on-success</code>, it will be restarted only when the service process exits cleanly. In this context, a clean exit means an exit code of 0, or one of the signals <code>SIGHUP</code>, <code>SIGINT</code>, <code>SIGTERM</code> or <code>SIGPIPE</code>, and additionally, exit statuses and signals specified in <code>SuccessExitStatus=</code>.If set to <code>on-failure</code>, the service will be restarted when the process exits with a non-zero exit code, is terminated by a signal (including on core dump, but excluding the aforementioned four signals), when an operation (such as service reload) times out, and when the configured watchdog timeout is triggered.If set to <code>on-abnormal</code>, the service will be restarted when the process is terminated by a signal (including on core dump, excluding the aforementioned four signals), when an operation times out, or when the watchdog timeout is triggered.If set to <code>on-abort</code>, the service will be restarted only if the service process exits due to an uncaught signal not specified as a clean exit status.If set to <code>on-watchdog</code>, the service will be restarted only if the watchdog timeout for the service expires.If set to <code>always</code>, the service will be restarted regardless of whether it exited cleanly or not, got terminated abnormally by a signal, or hit a timeout.</p>
