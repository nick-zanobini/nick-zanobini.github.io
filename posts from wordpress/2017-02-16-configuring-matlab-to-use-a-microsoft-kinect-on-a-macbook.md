---
layout: jetpack-portfolio
title: Configuring MATLAB to use a Microsoft Kinect on a Macbook
date: 2017-02-16 05:25
author: nickzanobini
comments: true
categories: []
---
I recently wanted to use my old Xbox 360 Kinect on my MacBook in MATLAB for a project. Well I did a little research and there wasn't a ton of up to date info out there. Here is a little step by step guide to install all the necessary components to get it working on a Mac running OSX 10.11.x El Capitan.

<img class=" size-full wp-image-672 aligncenter" src="https://nickzanobini.files.wordpress.com/2017/02/arm1.png" alt="arm" width="577" height="251" />

<ul>
    <li>Install Xcode from the App Store. Open it and accept the terms and conditions.</li>
    <li>Open Terminal and run the command</li>
</ul>

[code language="bash" light="true"]
xcode-select —install
[/code]

<ul>
    <li>Download MATLAB. Open it and accept the terms and conditions</li>
    <li>Install and update MacPorts by running the following command in Terminal</li>
</ul>

[code language="bash" light="true"]
curl -O https://distfiles.macports.org/MacPorts/MacPorts-2.3.3.tar.bz2
tar xf MacPorts-2.3.3.tar.bz2
cd MacPorts-2.3.3/
./configure
make
sudo make install
export PATH=/opt/local/bin:/opt/local/sbin:$PATH
sudo port selfupdate
sudo port upgrade outdated
[/code]

<ul>
    <li>
<p class="p1">Check to see if you Systems Integrity Protection is enabled by running the following in Terminal</p>
</li>
</ul>

[code language="bash" light="true"]
csrutil status
[/code]

<ul>
    <li>If it says "enabled" then you will have to do the following, if it says disabled, then you can skip the next step</li>
    <li>Assuming it says "enabled" you need to reboot your computer into recovery mode by holding down the "command" and "r" key while it restarts</li>
    <li>Once in recovery mode, at the top of the screen in the menu bar select Utilities and then Terminal and run the following commands</li>
</ul>

[code language="bash" light="true"]
csrutil disable sudo reboot
[/code]

<ul>
    <li>Just to be sure it worked lets check the status again by by running the following in Terminal. It should return "disabled"</li>
</ul>

[code language="bash" light="true"]

csrutil status

[/code]

<ul>
    <li>Install some perquisites by running the following in Terminal</li>
</ul>

[code language="bash" light="true"]
sudo port install git
sudo port install libtool
sudo port install libusb-devel
sudo port install cmake
sudo port install wget
[/code]

<ul>
    <li>
<p class="p1">Download the files needed to link MATLAB and the Xcode compiler by running the following in Terminal</p>
</li>
</ul>

[code language="bash" light="true"]
cd ~
cd Downloads
wget http://www.mathworks.com/matlabcentral/answers/uploaded_files/37858/xcode7_mexopts.zip
open xcode7_mexopts.zip
[/code]

<ul>
    <li>Now in MATLAB run the following commands to link the Xcode compiler to MATLAB</li>
</ul>

[code language="matlab" light="true"]
cd( prefdir );
cd( fullfile( matlabroot, 'bin', 'maci64', 'mexopts' ) );
mkdir mexoptsContentsOLD
movefile *.xml mexoptsContentsOLD/
movefile( '~/Downloads/xcode7_mexopts/*.xml', '.' );
mex -setup
[/code]

<ul>
    <li>Download OpenNI, NiTE, and SensorKinect and put them all in a folder titled "kinect" together by running the following commands in Terminal.</li>
</ul>

[code language="bash" light="true"]
cd ~
mkdir kinect &amp;amp;&amp;amp; cd kinect
wget http://openni.ru/wp-content/uploads/2013/11/OpenNI-Bin-Dev-MacOSX-v1.5.7.10.tar.zip
wget http://openni.ru/wp-content/uploads/2012/12/NITE-Bin-MacOSX-v1.5.2.21.tar.zip
wget https://github.com/avin2/SensorKinect/archive/unstable.zip
[/code]

<ul>
    <li>Install OpenNI by running the following commands in Terminal.</li>
</ul>

[code language="bash" light="true"]
open OpenNI-Bin-Dev-MacOSX-v1.5.7.10.tar.zip
mv OpenNI-Bin-Dev-MacOSX-v1.5.7.10 OpenNI
cd OpenNI
sudo ./install.sh
[/code]

<ul>
    <li>Install NiTE by running the following commands in Terminal.</li>
</ul>

[code language="bash" light="true"]
cd ..
open NITE-Bin-MacOSX-v1.5.2.21.tar.zip
mv NITE-Bin-Dev-MacOSX-v1.5.2.21 NiTE
cd NiTE
sudo ./install.sh
[/code]

<ul>
    <li>Install SensorKinect by running the following commands in Terminal.</li>
</ul>

[code language="bash" light="true"]
cd ..
open unstable.zip &amp;amp;&amp;amp; mv SensorKinect-unstable/ SensorKinect
cd SensorKinect/Bin
open SensorKinect093-Bin-MacOSX-v5.1.2.1.tar.bz2
cd Sensor-Bin-MacOSX-v5.1.2.1
sudo ./install.sh
[/code]

<ul>
    <li>Now reenable your Systems Integrity Protection by rebooting your computer into recovery mode by holding down the "command" and "r" key while it restarts</li>
    <li>Once in recovery mode, at the top of the screen in the menu bar select Utilities and then Terminal and run the following commands</li>
</ul>

[code language="bash" light="true"] csrutil enable
sudo reboot [/code]

<ul>
    <li>Just to be sure it worked lets check the status again by by running the following in Terminal. It should return "enabled"[code language="bash" light="true"]

csrutil status

[/code]</li>
    <li>Download the MATLAB files to test the Kinect by going <a href="http://au.mathworks.com/matlabcentral/fileexchange/30242-kinect-matlab">here</a> and downloading the files.</li>
    <li>Move the folder "Kinect_Matlab_version2" to your MATLAB folder</li>
    <li>In the "OpenNI1" folder open the file compile_cpp_files.m</li>
    <li>Lines 24, 26, 28, 49 and 51 respectively need to be changed from</li>
</ul>

[code language="matlab" light="true"]
OpenNiPathInclude=getenv('OPEN_NI_INCLUDE');
OpenNiPathLib=getenv('OPEN_NI_LIB64');
OpenNiPathLib=getenv('OPEN_NI_LIB');
mex('-v',['-L' OpenNiPathLib],'-lopenNI64',['-I' OpenNiPathInclude '\'],Filename);
mex('-v',['-L' OpenNiPathLib],'-lopenNI',['-I' OpenNiPathInclude '\'],Filename);
[/code]
to

[code language="matlab" light="true"]
OpenNiPathInclude='/usr/include/ni/';
OpenNiPathLib='/usr/lib';
OpenNiPathLib='/usr/lib';
mex('-v',['-DMX_COMPAT_32_OFF -L' OpenNiPathLib],'/usr/lib/libOpenNI.dylib',['-I' OpenNiPathInclude],Filename);
mex('-v',['-DMX_COMPAT_32_OFF -L' OpenNiPathLib],'/usr/lib/libOpenNI.dylib',['-I' OpenNiPathInclude],Filename);
[/code]

<ul>
    <li>Thats it. Plug in your Kinect and you are set. Open up one of the examples and test it out!</li>
</ul>

To write this post I pooled info from the following places:

Linking Xcode and MATLAB: <a href="http://www.mathworks.com/matlabcentral/answers/246507-why-can-t-mex-find-a-supported-compiler-in-matlab-r2015b-after-i-upgraded-to-xcode-7-0">http://www.mathworks.com/matlabcentral/answers/246507-why-can-t-mex-find-a-supported-compiler-in-matlab-r2015b-after-i-upgraded-to-xcode-7-0</a>

Disabling Systems Integrity Protection: <a href="http://apple.stackexchange.com/questions/208478/how-do-i-disable-system-integrity-protection-sip-aka-rootless-on-os-x-10-11">http://apple.stackexchange.com/questions/208478/how-do-i-disable-system-integrity-protection-sip-aka-rootless-on-os-x-10-11</a>

Installing the Kinect drivers via OpenNI: <a href="http://sjtrny.com/posts/2013/2/12/kinect-and-matlab-os-x-via-openni.html">http://sjtrny.com/posts/2013/2/12/kinect-and-matlab-os-x-via-openni.html</a>

The MATLAB files for the Kinect: <a href="http://au.mathworks.com/matlabcentral/fileexchange/30242-kinect-matlab">http://au.mathworks.com/matlabcentral/fileexchange/30242-kinect-matlab</a>
