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
sudo apt-get install ros-kinetic-joint-trajectory-controller

{% endhighlight %}

* [Setup ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
{% highlight bash %}
source /opt/ros/kinetic/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
{% endhighlight %}

* [MoveIt](http://moveit.ros.org/install/) and [MoveIt Visual Tools](https://github.com/ros-planning/moveit_visual_tools)
{% highlight bash %}
sudo apt-get install ros-kinetic-moveit
sudo apt-get install ros-kinetic-moveit-visual-tools
source /opt/ros/kinetic/setup.bash
{% endhighlight %}

* [Gazebo 7]()
{% highlight bash %}
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install gazebo7
sudo apt-get install libignition-math2-dev
{% endhighlight %}

* [pip](https://pip.pypa.io/en/stable/installing/)
{% highlight bash %}
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
rm get-pip.py
{% endhighlight %} 

* [git](https://help.ubuntu.com/lts/serverguide/git.html)
{% highlight bash %}
sudo apt-get install git
git config --global push.default simple
git config --global user.email "github_username@users.noreply.github.com"
git config --global user.name "Your Name Here"
git config credential.helper store
{% endhighlight %}

* [OpenCV](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)
{% highlight bash %}
# 1. KEEP UBUNTU OR DEBIAN UP TO DATE

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade
sudo apt-get -y autoremove

# 2. INSTALL THE DEPENDENCIES

# Build tools:
sudo apt-get install -y build-essential cmake

# GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):
sudo apt-get install -y qt5-default libvtk6-dev

# Media I/O:
sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev

# Video I/O:
sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev

# Parallelism and linear algebra libraries:
sudo apt-get install -y libtbb-dev libeigen3-dev

# Python:
sudo apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy python-vtk

# Java:
sudo apt-get install -y ant default-jdk

# Documentation:
sudo apt-get install -y doxygen

# 3. INSTALL THE LIBRARY (YOU CAN CHANGE '3.2.0' FOR THE LAST STABLE VERSION)
sudo apt-get install -y unzip wget
wget https://github.com/opencv/opencv/archive/3.2.0.zip
unzip 3.2.0.zip
rm 3.2.0.zip
mv opencv-3.2.0 opencv
cd opencv
wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip
unzip 3.2.0.zip
rm 3.2.0.zip
mv opencv_contrib-3.2.0 opencv_contrib
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
    -D WITH_QT=ON -DWITH_OPENGL=ON \
    -D FORCE_VTK=ON \
    -D WITH_TBB=ON \
    -D WITH_GDAL=ON \
    -D WITH_XINE=ON \
    -D BUILD_EXAMPLES=ON \
    -D ENABLE_PRECOMPILED_HEADERS=OFF ..

make -j $(($(nproc) + 1))

sudo make install
sudo ldconfig
{% endhighlight %}

* Miscellaneous Packages
{% highlight bash %}
sudo apt-get update
sudo pip install mpmath
sudo pip install sympy
sudo apt-get install netatalk avahi-daemon openssh-server
sudo apt install xfce4 xfce4-goodies tightvncserver
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


**Optional Packages**
{% highlight bash %}
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
{% endhighlight %} 