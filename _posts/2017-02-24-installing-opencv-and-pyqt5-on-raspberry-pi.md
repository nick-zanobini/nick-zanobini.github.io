---
layout: single
comments: true
date: 	2017-02-24 05:59:58
title: 	Installing OpenCV and PyQT5 on Raspberry Pi
tags:	python raspberrypi linux qt pyqt opencv 
---

PyQt5 is available as a collection of packages for Debian 8 (Jessie). To install a basic set of PyQt5 modules, you need to [install PyQt5](https://gist.github.com/garyjohnson/f041d2274dccd6641c51).

{% highlight bash %}
# Link GPU eglfs binaries so Qt can get to them in system path
sudo ln -s /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so.1.0.0
sudo ln -s /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so.2.0.0

# Install the leandog apt server in your sources
echo "deb http://apt.leandog.com/ jessie main" | sudo tee --append /etc/apt/sources.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BDCBFB15

# Install packages
sudo apt-get update
sudo apt-get install -y qt5 sip pyqt5
sudo apt-get install pyqt5-dev-tools

# Depends on your use case, but I generally recommend increasing vram memory split in raspi-config to 256
{% endhighlight %} 

A pre-compiled binary of OpenCV for the Raspberry Pi on [GitHub](https://github.com/jabelone/OpenCV-for-Pi).
It was compiled on a Raspberry Pi 3 Model B+ running Raspian Jessie. This version was built with TBB which enables automatic multithreading in many OpenCV algorithms.

Once connected to your Raspberry Pi you need to start installing the necessary libraries.

0) Always good practice to update everything before you install stuff:

{% highlight bash %}
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
{% endhighlight %} 
1) We need to install some packages that allow OpenCV to process images:

{% highlight bash %}
sudo apt-get install libtiff5-dev libjasper-dev libpng12-dev
{% endhighlight %} 
If you get an error about libjpeg-dev try installing this first:

{% highlight bash %}
sudo apt-get install libjpeg-dev
{% endhighlight %} 
2) We need to install some packages that allow OpenCV to process videos:

{% highlight bash %}
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
{% endhighlight %} 
3) We need to install the GTK library for some GUI stuff like viewing images.

{% highlight bash %}
sudo apt-get install libgtk2.0-dev
{% endhighlight %} 
4) We need to install some other packages for various operations in OpenCV:

{% highlight bash %}
sudo apt-get install libatlas-base-dev gfortran
{% endhighlight %} 
5) We need to install pip if you haven't done so in the past:

{% highlight bash %}
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
{% endhighlight %} 
6) Now we can install NumPy - a python library for maths stuff - needed for maths stuff.

{% highlight bash %}
sudo pip install numpy
{% endhighlight %} 
7) Download and install the file from this repo called "latest-OpenCV.deb".

{% highlight bash %}
wget "https://github.com/jabelone/OpenCV-for-Pi/raw/master/latest-OpenCV.deb"
sudo dpkg -i latest-OpenCV.deb
{% endhighlight %} 
8) Test it installed correctly by doing the following:
Open a python shell

{% highlight bash %}
python
{% endhighlight %} 
Run the following commands, it should return the same version you installed.

{% highlight python %}
import cv2
cv2.__version__
{% endhighlight %} 
