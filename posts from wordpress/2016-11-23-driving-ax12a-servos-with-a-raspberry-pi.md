---
layout: jetpack-portfolio
title: Driving Ax-12a Servos with a Raspberry Pi 3
date: 2016-11-23 06:24
author: nickzanobini
comments: true
categories: []
---
I bought a <a href="http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx" target="_blank">Trossen Robotics PhantomX Pincher Arm</a> recently and wanted to build a vision based pick and place system to get better with OpenCV and Python.

The first step was to get it setup and talking with my RPi.<img class="alignright  wp-image-443" src="https://nickzanobini.files.wordpress.com/2016/11/imageedit_4_5605969898.png?w=300" alt="imageedit_4_5605969898" width="356" height="356" />

Here's a list of what I used to get it up and running.

<ul>
    <li>My Macbook Pro</li>
    <li>Arduino IDE</li>
    <li><a href="https://github.com/Interbotix/dynaManager/releases">DynaManager</a></li>
    <li><a href="http://www.trossenrobotics.com/store/p/6406-FTDI-Cable-5V.aspx" target="_blank">USB to FTDI cable</a> (There's other cheaper ones)</li>
    <li>Raspberry Pi 2 or 3</li>
    <li><a href="http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx" target="_blank">Robotic Arm with ArbotiX-M Microcontroller</a></li>
    <li>Breadboard</li>
    <li>Jumper wires</li>
    <li><a href="http://www.uni-kl.de/elektronik-lager/417791">74LS241</a> Non inverting buffer gate</li>
    <li>12V 5A SMPS DC power supply or 11-12 VDC LiPo Battery</li>
</ul>

Here's what I did to get the arm connected and talking to my RPi. I assume you already have Raspian Jessie flashed onto your RPi and you know how to either SSH in or open up a terminal window on your RPi.

<ul>
    <li>Assemble the arm based on the <a href="http://learn.trossenrobotics.com/16-interbotix/robot-arms/pincher-robot-arm/163-phantomx-pincher-robot-arm-assembly-guide.html">instructions</a>.</li>
    <li>Assign each servo an ID with the DynaManager following <a href="http://learn.trossenrobotics.com/index.php/getting-started-with-the-arbotix/1-using-the-tr-dynamixel-servo-tool#&amp;panel1-1" target="_blank">these instructions</a>
<ul>
    <li>Using my computer, the FTDI cable, the arm and ArbotiX-M Micro-controller I connected my FTDI cable to the ArbotiX-M and connected only ONE servo as shown below. It is important to number the servos one at a time.</li>
    <li>I assigned the following ID's to each servo:
<ul>
    <li>ID 1: Shoulder Rotate, ID 2: Shoulder Flex, ID 3: Elbow Flex, ID 4: Wrist Flex, ID 5: Gripper</li>
</ul>
</li>
    <li>I know assigning ID’s to the servos can be done without the FTDI cable and ArbotiX-M Microcontroller, however I had them and it was quick and easy.</li>
</ul>
</li>
</ul>

<img class=" alignleft" src="http://learn.trossenrobotics.com/cache/multithumb_thumbs/b_400_400_16777215_00__images_tutorials_arbotixM_arbotixm_single_servo.png" alt="b_400_400_16777215_00__images_tutorials_arbotixM_arbotixm_single_servo.png" width="364" height="378" align="middle" />

<ul>
    <li>After assigning each servo their respective ID's I connected all of them together and tested the arm using the <a href="http://learn.trossenrobotics.com/interbotix/robot-arms/16-phantomx-pincher-robot-arm/25-phantomx-pincher-robot-arm-build-check" target="_blank">provided build check program</a>.</li>
    <li>Next, I set up the circuit to send commands to the AX12a Servos.
<ul>
    <li>They are controlled by a TTL level serial link so in order to have reliable communication we need to convert the RPi's 3.3V level serial link to the TTL level of the servo.</li>
    <li>We also need to convert the communication from full-duplex into half-duplex so we can communicate over the RPi's UART port, using only one wire for both sending and receiving.</li>
</ul>
</li>
</ul>

<ul>
    <li>Here’s a more detailed description of the pin connections and a description of all the RPi pins so there’s no confusion.</li>
</ul>

Connect pins 2 and 3 of the 74LS241 together
Connect pins 1 and 19 of the 74LS241 together

[caption id="attachment_341" align="alignright" width="312"]<img class="  wp-image-341 alignright" src="https://nickzanobini.files.wordpress.com/2016/11/circuit.png?w=300" alt="circuit" width="312" height="286" /> Full Duplex to Half Duplex Circuit[/caption]

Connect pin 2 or 3 of the 74LS241 to the data pin of the 3-Pin Dynamixel Cable
Connect pin 18 of the 74LS241 to the RXD0 pin on the RPi. (Pin# 10 or GPIO 15)
Connect pin 17 of the 74LS241 to the TXD0 pin on the RPi. (Pin# 8 or GPIO 14)
Connect pin 10 of the 74LS241 to ground on the RPi. (Pin #06 or Pin #14)
Connect pin 20 of the 74LS241 to 5V on the RPi. (Pin #02 or Pin #04)
Connect the +12V from the 12V DC supply to the 12V pin of 3-Pin Dynamixel Cable
Connect the ground from the 12V DC supply to the ground pin of 3-Pin Dynamixel Cable

<ul>
    <li>If you want to get fancy <a href="https://circuits.io/circuits/267189-ax-12-driver-for-raspberry-pi/" target="_blank">here is a simple PCB design for the circuit</a></li>
</ul>

<img class="  wp-image-461 aligncenter" src="https://nickzanobini.files.wordpress.com/2015/06/ascasc.png" alt="ascasc" width="737" height="259" />

<ul>
    <li>Next we need to configure the RPi for serial communication to the AX12a servos. (I use nano but you can use any editor you want)
<ul>
    <li>Set the configuration parameters in <code>/boot/config.txt</code> by running:[code language="bash" light="true"]
sudo nano /boot/config.txt
[/code]</li>
    <li>Change or add the following lines:
[code language="bash" light="true"]
init_uart_clock = 160000000
sudo stty -F /dev/ttyAMA0 10000000
[/code]</li>
    <li>Save these changes and exit nano by pressing
<ul>
    <li>Control + o</li>
    <li>Enter</li>
    <li>Control + x</li>
</ul>
</li>
    <li>Prevent any other processes from using the serial port ttyAMA0 by commenting out all options mentioning ttyAMA0 in both <code>/boot/cmdline.txt</code> and <code>/etc/inittab</code>
[code language="bash" light="true"]
sudo nano /boot/cmdline.txt
sudo nano /etc/inittab
[/code]
<ul>
    <li>Save these changes and exit nano by pressing
<ul>
    <li>Control + o</li>
    <li>Enter</li>
    <li>Control + x</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>

<ul>
    <li><img class=" size-full wp-image-521 alignleft" src="https://nickzanobini.files.wordpress.com/2016/11/imageedit_6_7513314533.png?w=364" alt="imageedit_6_7513314533.png" width="364" height="207" />Now if you have a RPi 2 you can skip this step. If you have a RPi 3 you need to disable the Bluetooth which uses ttyAMA0 as well and point the serial port you connected earlier to ttyAMA0.</li>
    <li>Congrats you are now ready to use your arm with your RPi.</li>
    <li>I tested mine with the following python script which sends a fixed location to servo 1 pauses and then sends another location to servo 1. If it moves then you set up everything correctly.</li>
</ul>

<h3>Troubleshooting:</h3>

<ul>
    <li class="p1"><span class="s1"><code>src.ax12.timeoutError</code>: Timeout on servo 1 (Or any other servo number)</span>
<ul>
    <li class="p1">This error usually means the servo is unreachable.
<ul>
    <li class="p1">Double check your wiring.</li>
    <li class="p1">Try unplugging the 12V power supply.</li>
    <li class="p1">Swap the 1st and 3rd Pin Dynamixel Cable</li>
</ul>
</li>
    <li class="p1">The <a href="http://www.instructables.com/id/How-to-drive-Dynamixel-AX-12A-servos-with-a-Raspbe/" target="_blank">74LS241 Circuit and wiring diagram</a> says to connect a 10kΩ from pin  2 or 3 of the 74LS241 to pin 20 of the 74LS241. This is wrong. When I had this resistor connected I could not communicate with the AX12a servos.</li>
</ul>
</li>
</ul>

<p dir="ltr">I used the following sources to help me do this:
<a href="http://www.instructables.com/id/How-to-drive-Dynamixel-AX-12A-servos-with-a-Raspbe/" target="_blank">74LS241 Circuit and wiring diagram</a>
<a href="http://www.oppedijk.com/robotics/control-dynamixel-with-raspberrypi" target="_blank">RPi serial communication</a>
<a href="http://raspberrypi.stackexchange.com/questions/45570/how-do-i-make-serial-work-on-the-raspberry-pi3" target="_blank">Configuring RPi3 for serial communication</a>
<a href="http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx" target="_blank">Building, setting up and general information of the arm</a></p>
