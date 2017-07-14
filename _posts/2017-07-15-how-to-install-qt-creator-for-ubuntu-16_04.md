---
layout: single
comments: true
date: 	2017-07-15 11:59:00
title: 	How install Qt Creator for Ubuntu 16.04
tags:	ubuntu qt linux
---


This tutorial was done with the following software versions:

* Ubuntu 16.04 LTS
* Qt Creator 3.5.1
* Qt 5.5.1

### Install Qt
{% highlight bash %}
sudo apt-get install build-essential
sudo apt-get install qtcreator
sudo apt-get install qt5-default
{% endhighlight %} 


### Install documentation and examples

If Qt Creator is installed thanks to the Ubuntu Sofware Center or thanks to the synaptic package manager, documentation for Qt Creator is not installed. Hitting the F1 key will show you the following message : "No documentation available". This can easily be solved by installing the Qt documentation:
{% highlight bash %}
sudo apt-get install qt5-doc
sudo apt-get install qt5-doc-html qtbase5-doc-html
sudo apt-get install qtbase5-examples
{% endhighlight %}

Restart Qt Creator to make the documentation available.