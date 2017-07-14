---
layout: single
title:  Error: qt_gui_main() found no plugin matching 
date:   2017-07-14 12:30:00"rqt_mypkg
tags:   ros rqt python linux
comments: true
---


Last night I was trying to update a rqt package and I knew I had setup everything correctly this time but it still was giving me this error: `qt_gui_main() found no plugin matching "rqt_mypkg"`

Unfortunately, my plugin was also not in the list returned by "rqt --list-plugins". rosrun also fails.

Here's what I was doing to get the error:

{% highlight bash %}
catkin_make
rosrun rqt_mypkg rqt_mypkg
qt_gui_main() found no plugin matching "rqt_mypkg"
{% endhighlight %} 

This appears to be a problem with rqt caching the locations of plugins in its config and not updating that info. 

A simple way to fix it is to delete that cache and restart rqt:

{% highlight bash %}
rm ~/.config/ros.org/rqt_gui.ini
rqt
{% endhighlight %} 