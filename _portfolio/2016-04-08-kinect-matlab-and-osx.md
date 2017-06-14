---
layout: simple
title: Kinect MATLAB and OSX
date: 2016-04-08 18:43
author: nickzanobini
comments: true
categories: [kinect, mac, matlab, osx, Programming, Robotics]
---
I recently wanted to use my old Xbox 360 Kinect on my MacBook in MATLAB for a project. Well I did a little research and there wasn't a ton of up to date info out there. Here is a little step by step guide to install all the necessary components to get it working on a Mac running OSX 10.11.x El Capitan.

    *Install Xcode from the App Store. Open it and accept the terms and conditions.
    *Open Terminal and run the command

{% highlight bash %}
xcode-select —install
{% endhighlight %}

    *Download MATLAB. Open it and accept the terms and conditions
    *Install and update MacPorts by running the following command in Terminal

{% highlight bash %}
curl -O https://distfiles.macports.org/MacPorts/MacPorts-2.3.3.tar.bz2
tar xf MacPorts-2.3.3.tar.bz2
cd MacPorts-2.3.3/
./configure
make
sudo make install
export PATH=/opt/local/bin:/opt/local/sbin:$PATH
sudo port selfupdate
sudo port upgrade outdated
{% endhighlight %}

    *
<p class="p1">Check to see if you Systems Integrity Protection is enabled by running the following in Terminal</p>


{% highlight bash %}
csrutil status
{% endhighlight %}

    *If it says "enabled" then you will have to do the following, if it says disabled, then you can skip the next step
    *Assuming it says "enabled" you need to reboot your computer into recovery mode by holding down the "command" and "r" key while it restarts
    *Once in recovery mode, at the top of the screen in the menu bar select Utilities and then Terminal and run the following commands

{% highlight bash %}
csrutil disable sudo reboot
{% endhighlight %}

    *Just to be sure it worked lets check the status again by by running the following in Terminal. It should return "disabled"

{% highlight bash %}
csrutil status
{% endhighlight %}

    *Install some perquisites by running the following in Terminal

{% highlight bash %}
sudo port install git
sudo port install libtool
sudo port install libusb-devel
sudo port install cmake
sudo port install wget
{% endhighlight %}

    *Download the files needed to link MATLAB and the Xcode compiler by running the following in Terminal

{% highlight bash %}
cd ~
cd Downloads
wget http://www.mathworks.com/matlabcentral/answers/uploaded_files/37858/xcode7_mexopts.zip
open xcode7_mexopts.zip
{% endhighlight %}

    *Now in MATLAB run the following commands to link the Xcode compiler to MATLAB

{% highlight matlab %}
cd( prefdir );
cd( fullfile( matlabroot, 'bin', 'maci64', 'mexopts' ) );
mkdir mexoptsContentsOLD
movefile *.xml mexoptsContentsOLD/
movefile( '~/Downloads/xcode7_mexopts/*.xml', '.' );
mex -setup
{% endhighlight %}

    *Download OpenNI, NiTE, and SensorKinect and put them all in a folder titled "kinect" together by running the following commands in Terminal.

{% highlight bash %}
cd ~
mkdir kinect &amp;&amp; cd kinect
wget http://openni.ru/wp-content/uploads/2013/11/OpenNI-Bin-Dev-MacOSX-v1.5.7.10.tar.zip
wget http://openni.ru/wp-content/uploads/2012/12/NITE-Bin-MacOSX-v1.5.2.21.tar.zip
wget https://github.com/avin2/SensorKinect/archive/unstable.zip
{% endhighlight %}

    *Install OpenNI by running the following commands in Terminal.

{% highlight bash %}
open OpenNI-Bin-Dev-MacOSX-v1.5.7.10.tar.zip
mv OpenNI-Bin-Dev-MacOSX-v1.5.7.10 OpenNI
cd OpenNI
sudo ./install.sh
{% endhighlight %}

    *Install NiTE by running the following commands in Terminal.

{% highlight bash %}
cd ..
open NITE-Bin-MacOSX-v1.5.2.21.tar.zip
mv NITE-Bin-Dev-MacOSX-v1.5.2.21 NiTE
cd NiTE
sudo ./install.sh
{% endhighlight %}

    *Install SensorKinect by running the following commands in Terminal.

{% highlight bash %}
cd ..
open unstable.zip &amp;&amp; mv SensorKinect-unstable/ SensorKinect
cd SensorKinect/Bin
open SensorKinect093-Bin-MacOSX-v5.1.2.1.tar.bz2
cd Sensor-Bin-MacOSX-v5.1.2.1
sudo ./install.sh
{% endhighlight %}

    *Now reenable your Systems Integrity Protection by rebooting your computer into recovery mode by holding down the "command" and "r" key while it restarts
    *Once in recovery mode, at the top of the screen in the menu bar select Utilities and then Terminal and run the following commands

{% highlight bash %}
csrutil enable
sudo reboot 
{% endhighlight %}

    *Just to be sure it worked lets check the status again by by running the following in Terminal. It should return "enabled"

{% highlight bash %}
csrutil status
{% endhighlight %}

    *Download the MATLAB files to test the Kinect by going (http://au.mathworks.com/matlabcentral/fileexchange/30242-kinect-matlab">here and downloading the files.
    *Move the folder "Kinect_Matlab_version2" to your MATLAB folder
    *In the "OpenNI1" folder open the file compile_cpp_files.m
    *Lines 24, 26, 28, 49 and 51 respectively need to be changed from

{% highlight matlab %}
OpenNiPathInclude=getenv('OPEN_NI_INCLUDE');
OpenNiPathLib=getenv('OPEN_NI_LIB64');
OpenNiPathLib=getenv('OPEN_NI_LIB');
mex('-v',['-L' OpenNiPathLib],'-lopenNI64',['-I' OpenNiPathInclude '\'],Filename);
mex('-v',['-L' OpenNiPathLib],'-lopenNI',['-I' OpenNiPathInclude '\'],Filename);
{% endhighlight %}
to

{% highlight matlab %}
OpenNiPathInclude='/usr/include/ni/';
OpenNiPathLib='/usr/lib';
OpenNiPathLib='/usr/lib';
mex('-v',['-DMX_COMPAT_32_OFF -L' OpenNiPathLib],'/usr/lib/libOpenNI.dylib',['-I' OpenNiPathInclude],Filename);
mex('-v',['-DMX_COMPAT_32_OFF -L' OpenNiPathLib],'/usr/lib/libOpenNI.dylib',['-I' OpenNiPathInclude],Filename);
{% endhighlight %}

    *Thats it. Plug in your Kinect and you are set. Open up one of the examples and test it out!

To write this post I pooled info from the following places:

[Linking Xcode and MATLAB](http://www.mathworks.com/matlabcentral/answers/246507-why-can-t-mex-find-a-supported-compiler-in-matlab-r2015b-after-i-upgraded-to-xcode-7-0)

[Disabling Systems Integrity Protection](http://apple.stackexchange.com/questions/208478/how-do-i-disable-system-integrity-protection-sip-aka-rootless-on-os-x-10-11)

[Installing the Kinect drivers via OpenNI](http://sjtrny.com/posts/2013/2/12/kinect-and-matlab-os-x-via-openni.html)

[The MATLAB files for the Kinect](http://au.mathworks.com/matlabcentral/fileexchange/30242-kinect-matlab)
