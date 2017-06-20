---
layout: single
title:  "Vision Controlled 4DOF Robotic Arm"
date:   2016-11-05 19:26:11
tags:   arm ax12a raspberrypi robotarm Robotics rpi trossen python opencv vision
header:
  image: /assets/images/foo-bar-identity.jpg
  teaser: /assets/images/foo-bar-identity-th.jpg
---


{% include toc title="Unique Title" icon="file-text" %}

Testing Kramdown auto-generated table of contents with unique title and icon assigned in the include like so:

```liquid
{% raw %}{% include toc title="Unique Title" icon="file-text" %}{% endraw %}
```

## Overview

I have always been fascinated by the industrial robotic arms and the fully automated robotic assembly lines of automakers. Knowing I didn't have the money or the space for a full sized industrial robotic arm I settled for a smaller hobby arm that I can operate on my coffee table. I purchased a [Trossen Robotics PhantomX Pincher Arm](http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx) and set off to build a vision controlled arm in Python using OpenCV. 

I build this project in serveral stages. It is depicted in the final stages throughout this post.

<!-- Here is everything I needed for this project: -->

## Bill of Materials 

| Item | Where to Buy It | Cost |
|:--------|:-------:|:--------:|
| Robotic Arm with ArbotiX-M Microcontroller | [link](http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx) | cell3 |
| Webcam          | [link](https://smile.amazon.com/dp/B006JH8T3S/ref=cm_sw_r_cp_dp_T2_WD3qzbDARFMRY)   | cell6   |
| 1in x 1in x 2ft length of wood   | [link](https://smile.amazon.com/)  | cell3   |
| Scrap plywood   | Home Depot  | cell6   |
| 2 Right Angle Brackets | [link](https://smile.amazon.com/)  | cell6   |
| 1 Longer Right Angle Bracket | [link](https://smile.amazon.com/)  | cell6   |
| 74LS241         | [link](http://www.uni-kl.de/elektronik-lager/417791)  | cell6   |
| Raspberry Pi 2 or 3 | [link](https://smile.amazon.com/dp/B01CD5VC92/ref=cm_sw_r_cp_dp_T2_xi3qzbQ0A26T0)  | cell6   |
| computer        | I hope you have one  | N/A   |
| 12V 5A SMPS DC power supply | [link](https://smile.amazon.com/dp/B00TVWEGQ2/ref=cm_sw_r_cp_dp_T2_Ph3qzbY66B81R)  | cell6   
| Jumper wires    | [link](https://smile.amazon.com/dp/B005TZJ0AM/ref=cm_sw_r_cp_dp_T2_Xg3qzbAX4DHWT)  | cell6   |
| Breadboard      | [link](https://smile.amazon.com/dp/B01DDI54II/ref=cm_sw_r_cp_dp_T2_Zg3qzbZA7N3SE)  | cell6   |
| USB to FTDI cable   | [link](http://www.trossenrobotics.com/store/p/6406-FTDI-Cable-5V.aspx)  | cell6   |
| 2 10-32 Phillips head counter sunk screws | [link](https://smile.amazon.com/dp/B01M0YDNX0/ref=cm_sw_r_cp_dp_T2_gf3qzbTFSJ855)  | cell6   |
| 5 10-32 Phillips Flat head screws | [link](https://smile.amazon.com/dp/B01I28XAUI/ref=cm_sw_r_cp_dp_T2_zf3qzbRGQZ5KA)  | cell6   |
| 1 roll double sided tape | [link](https://smile.amazon.com/dp/B0007P5G8Y/ref=cm_sw_r_cp_dp_T2_He3qzbXCTHJA0)  | cell6   |
| Buck Converter USB out   | [link](https://smile.amazon.com/dp/B00XPZ7I4I/ref=cm_sw_r_cp_dp_T2_cb3qzbW1ZZ673)  | cell6   |
| Sain Smart Relay Module   | [link](https://smile.amazon.com/dp/B00VRUAHLE/ref=cm_sw_r_cp_dp_T2_ee3qzbQCYKBYX)  | cell6   |
| 5VDC USB Charger | [link]()  | cell6   |
| Micro USB Cable  | [link]()  | cell6   |
|=====
| Foot1   | Foot2   | Foot3
{: rules="groups"}

## Setup and Configuration - Part 1

First we need to update your Raspberry Pi install Python 3.X and OpenCV. Once connected to your Raspberry Pi you need to start installing the necessary libraries.

0) Always good practice to update everything before you install stuff:
{% highlight bash %}
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
{% endhighlight %} 

1) We need to install some packages that allow OpenCV to process images:
{% highlight bash %}
sudo apt-get install libjpeg-dev
sudo apt-get install libtiff5-dev libjasper-dev libpng12-dev
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

5) We need to install python and pip if you haven't done so in the past:
{% highlight bash %}
sudo apt-get install python3
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


## Setup and Configuration - Part 2
<!-- You can see my other [post]({{ site.url }}/_posts/2016-11-05-connecting-trossen-robotics-phantomx-pincher-arm-to-a-raspberry-pi.md) on how to setup the arm and connect it directly to the RPi. -->

* Assemble the arm based on the [instructions](http://learn.trossenrobotics.com/16-interbotix/robot-arms/pincher-robot-arm/163-phantomx-pincher-robot-arm-assembly-guide.html).
  * Assign each servo an ID with the DynaManager following [these instructions](http://learn.trossenrobotics.com/index.php/getting-started-with-the-arbotix/1-using-the-tr-dynamixel-servo-tool#&panel1-1)
    * Using my computer, the FTDI cable, the arm and ArbotiX-M Micro-controller I connected my FTDI cable to the ArbotiX-M and connected only ONE servo as shown below. It is important to number the servos one at a time.
    * I assigned the following ID's to each servo:
      * ID 1: Shoulder Rotate, ID 2: Shoulder Flex, ID 3: Elbow Flex, ID 4: Wrist Flex, ID 5: Gripper
    * I know assigning ID’s to the servos can be done without the FTDI cable and ArbotiX-M Microcontroller, however I had them and it was quick and easy.

![b_400_400_16777215_00__images_tutorials_arbotixM_arbotixm_single_servo.png](http://learn.trossenrobotics.com/cache/multithumb_thumbs/b_400_400_16777215_00__images_tutorials_arbotixM_arbotixm_single_servo.png)

  * After assigning each servo their respective ID's I connected all of them together and tested the arm using the [provided build check program](http://learn.trossenrobotics.com/interbotix/robot-arms/16-phantomx-pincher-robot-arm/25-phantomx-pincher-robot-arm-build-check).
  * Next, I set up the circuit to send commands to the AX12a Servos.
    * They are controlled by a TTL level serial link so in order to have reliable communication we need to convert the RPi's 3.3V level serial link to the TTL level of the servo.
    * We also need to convert the communication from full-duplex into half-duplex so we can communicate over the RPi's UART port, using only one wire for both sending and receiving.
  * The circuit looks as follows![circuit](https://nickzanobini.files.wordpress.com/2016/11/circuit.png)
  * Here’s a more detailed description of the pin connections and a description of all the RPi pins so there’s no confusion.
    * Connect pins 2 and 3 of the 74LS241 together
    * Connect pins 1 and 19 of the 74LS241 together
    * Connect pin 2 or 3 of the 74LS241 to the data pin of the 3-Pin Dynamixel Cable
    * Connect pin 18 of the 74LS241 to the RXD0 pin on the RPi. (Pin# 10 or GPIO 15)
    * Connect pin 17 of the 74LS241 to the TXD0 pin on the RPi. (Pin# 8 or GPIO 14)
    * Connect pin 10 of the 74LS241 to ground on the RPi. (Pin #06 or Pin #14)
    * Connect pin 20 of the 74LS241 to 5V on the RPi. (Pin #02 or Pin #04)
    * Connect the +12V from the 12V DC supply to the 12V pin of 3-Pin Dynamixel Cable
    * Connect the ground from the 12V DC supply to the ground pin of 3-Pin Dynamixel Cable
  * If you want to get fancy [here is a simple PCB design for the circuit](https://circuits.io/circuits/267189-ax-12-driver-for-raspberry-pi/)

![](http://nickzanobini.files.wordpress.com/2016/11/img_0525.png)![](http://nickzanobini.files.wordpress.com/2016/11/2.png)
    
  * Next we need to configure the RPi for serial communication to the AX12a servos. (I use nano but you can use any editor you want. For anyone not familiar with nano the way to save and exit is by pressing Ctrl+X then Y, then finally press Enter)
    * Set the configuration parameters in `/boot/config.txt` by running:  
      {% highlight bash %}
      sudo nano /boot/config.txt
      {% endhighlight %}  

    * Change or add the following lines:  
      {% highlight bash %}
      init_uart_clock = 160000000
      sudo stty -F /dev/ttyAMA0 10000000
      {% endhighlight %}  

    * Save these changes and exit nano (or your other favorite text editor)  
    * Prevent any other processes from using the serial port ttyAMA0 by commenting out all options mentioning ttyAMA0 in both `/boot/cmdline.txt` and `/etc/inittab`  
      {% highlight bash %}
      sudo nano /boot/cmdline.txt
      sudo nano /etc/inittab
      {% endhighlight %}  

      * Save these changes and exit nano (or your other favorite text editor)

## Setup and Configuration - Part 3
Once I got it connected and talking with my Raspberry Pi I did a couple of things.

1.  I installed the relay in series with the 12V going to the motors. This allowed me to kill power to the servos whenever I needed to.
2.  I installed the 12VDC to 5VDC Buck converter so I only needed one thing plugged in at all times.

## Initial Tests
After I did those two things I ran a couple of tests. 
1.  I powered up the RPi and made it still turned on and that I could move the arm by hand (There was no power going to the arm)  
2.  I SSHed into the RPi and toggled the relay to make sure that worked. You should hear the relay click on and then five seconds later click off.  
  {% highlight bash %}
  python
  {% endhighlight %}
  {% highlight python %}
  import RPI.GPIO as GPIO
  from time import sleep
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(23, GPIO.OUT)
  GPIO.output(23, GPIO.HIGH)
  sleep(5)
  GPIO.output(23, GPIO.LOW)
  {% endhighlight %}

3.  Move the arm straight up and then into a resting position - [basic_move_test.py]({{ site.url }}/assets/PhantomX-Pincher-Arm/ArmTest/basic_move_test.py)



