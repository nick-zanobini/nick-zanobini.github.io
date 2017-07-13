---
layout: single
title: 	Configuring a Naitive Install of Ubuntu 16.04 LTS for Udacity's Robotics Nanodegree
date: 	2017-07-11 03:52:00
tags:	linux udacity ubuntu
comments: true
---

I am currently taking the Robotics Nanodegree from Udacity and I wanted to document all the packages I had to install for the program. I will continue to update this as I go along and install more things.

* [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu)
{% highlight bash %}
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
sudo rosdep init
rosdep update
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install python-rosinstall
{% endhighlight %} 

* [pip](https://pip.pypa.io/en/stable/installing/)
{% highlight bash %}
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
{% endhighlight %} 

* [MoveIt](http://moveit.ros.org/install/) and [MoveIt Visual Tools](https://github.com/ros-planning/moveit_visual_tools)
{% highlight bash %}
sudo apt-get install ros-kinetic-moveit
sudo apt-get install ros-kinetic-moveit-visual-tools
source /opt/ros/kinetic/setup.bash
{% endhighlight %} 

* [python-pcl](https://github.com/strawlab/python-pcl)
{% highlight bash %}
sudo pip install cython
git clone https://github.com/strawlab/python-pcl.git
cd python-pcl
python setup.py build
sudo python setup.py install
sudo apt-get install pcl-tools
{% endhighlight %} 