---
layout: single
title:  "Vision Controlled 4DOF Robotic Arm"
date:   2016-11-05 19:26:11
tags:   arm ax12a raspberrypi robotarm Robotics rpi trossen python opencv vision
header:
  image: /assets/images/foo-bar-identity.jpg
  teaser: /assets/images/foo-bar-identity-th.jpg
---

I have always been fascinated by the industrial robotic arms and the fully automated robotic assembly lines of automakers. Knowing I didn't have the money or the space for a full sized industrial robotic arm I settled for a smaller hobby arm that I can operate on my coffee table. I purchased a [Trossen Robotics PhantomX Pincher Arm](http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx) and set off to build this arm. 

You can see my other [post](link to post) on how to setup the arm and connect it directly to the RPi. Here is everything I needed for this project:

## Bill of Materials 

| Item | Where to Buy It | Cost |
|:--------:|:-------:|:--------:|
| Robotic Arm with ArbotiX-M Microcontroller | [link](http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx) | cell3 |
| Webcam          | [link](https://smile.amazon.com/dp/B006JH8T3S/ref=cm_sw_r_cp_dp_T2_WD3qzbDARFMRY)   | cell6   |
| 1in x 1in x 2ft length of wood   | [link]()  | cell3   |
| Scrap plywood   | [link]()  | cell6   |
| 2 Right Angle Brackets | [link]()  | cell6   |
| 1 Longer Right Angle Bracket | [link]()  | cell6   |
| 74LS241         | [link](http://www.uni-kl.de/elektronik-lager/417791)  | cell6   |
| Raspberry Pi 2 or 3 | [link](https://smile.amazon.com/dp/B01CD5VC92/ref=cm_sw_r_cp_dp_T2_xi3qzbQ0A26T0)  | cell6   |
| computer        | [link]()  | cell6   |
| 12V 5A SMPS DC power supply | [link](https://smile.amazon.com/dp/B00TVWEGQ2/ref=cm_sw_r_cp_dp_T2_Ph3qzbY66B81R)  | cell6   |
| Jumper wires    | [link](https://smile.amazon.com/dp/B005TZJ0AM/ref=cm_sw_r_cp_dp_T2_Xg3qzbAX4DHWT)  | cell6   |
| Breadboard      | [link](https://smile.amazon.com/dp/B01DDI54II/ref=cm_sw_r_cp_dp_T2_Zg3qzbZA7N3SE)  | cell6   |
| USB to FTDI cable   | [link](http://www.trossenrobotics.com/store/p/6406-FTDI-Cable-5V.aspx)  | cell6   |
| 2 10-32 Phillips head counter sunk screws | [link](https://smile.amazon.com/dp/B01M0YDNX0/ref=cm_sw_r_cp_dp_T2_gf3qzbTFSJ855)  | cell6   |
| 5 10-32 Phillips Flat head screws | [link](https://smile.amazon.com/dp/B01I28XAUI/ref=cm_sw_r_cp_dp_T2_zf3qzbRGQZ5KA)  | cell6   |
| 1 roll double sided tape | [link](https://smile.amazon.com/dp/B0007P5G8Y/ref=cm_sw_r_cp_dp_T2_He3qzbXCTHJA0)  | cell6   |
| Buck Converter USB out   | [link](https://smile.amazon.com/dp/B00XPZ7I4I/ref=cm_sw_r_cp_dp_T2_cb3qzbW1ZZ673)  | cell6   |
| Sain Smart Relay Module   | [link](https://smile.amazon.com/dp/B00VRUAHLE/ref=cm_sw_r_cp_dp_T2_ee3qzbQCYKBYX)  | cell6   |
|=====
| Foot1   | Foot2   | Foot3
{: rules="groups"}

I bought a [Trossen Robotics PhantomX Pincher Arm](http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx) recently and wanted to build a vision based pick and place system to get better with OpenCV and Python.

The first step was to get it setup and talking with my RPi.

Here's a list of what I used to get it up and running.
    
  * My Macbook Pro
  * Arduino IDE
  * [DynaManager](https://github.com/Interbotix/dynaManager/releases)
  * [USB to FTDI cable](http://www.trossenrobotics.com/store/p/6406-FTDI-Cable-5V.aspx) (There's other cheaper ones)
  * Raspberry Pi 2 or 3
  * [Robotic Arm with ArbotiX-M Microcontroller](http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx)
  * Breadboard
  * Jumper wires
  * [74LS241](http://www.uni-kl.de/elektronik-lager/417791) Non inverting buffer gate
  * 12V 5A SMPS DC power supply or 11-12 VDC LiPo Battery

Here's what I did to get the arm connected and talking to my RPi. I assume you already have Raspian Jessie flashed onto your RPi and you know how to either SSH in or open up a terminal window on your RPi.

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
    
  * Now if you have a RPi 2 you can skip this step. If you have a RPi 3 you need to disable the Bluetooth which uses `ttyAMA0` as well and point the serial port you connected earlier to ttyAMA0.
  * Congrats you are now ready to use your arm with your RPi.
  * I tested mine with the following python script which sends a fixed location to servo 1 pauses and then sends another location to servo 1. If it moves then you set up everything correctly.

### Troubleshooting:

  * `src.ax12.timeoutError`: Timeout on servo 1 (Or any other servo number)
    * This error usually means the servo is unreachable.
      * Double check your wiring.
      * Try unplugging the 12V power supply.
      * Swap the 1st and 3rd Pin Dynamixel Cable
    
    * The [74LS241 Circuit and wiring diagram](http://www.instructables.com/id/How-to-drive-Dynamixel-AX-12A-servos-with-a-Raspbe/) says to connect a 10kΩ from pin  2 or 3 of the 74LS241 to pin 20 of the 74LS241. This is wrong. When I had this resistor connected I could not communicate with the AX12a servos.


I used the following sources to help me do this:
[74LS241 Circuit and wiring diagram](http://www.instructables.com/id/How-to-drive-Dynamixel-AX-12A-servos-with-a-Raspbe/)
[RPi serial communication](http://www.oppedijk.com/robotics/control-dynamixel-with-raspberrypi)
[Configuring RPi3 for serial communication](http://raspberrypi.stackexchange.com/questions/45570/how-do-i-make-serial-work-on-the-raspberry-pi3)
[Building, setting up and general information of the arm](http://www.trossenrobotics.com/p/PhantomX-Pincher-Robot-Arm.aspx)
