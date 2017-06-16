---
layout: single
comments: true
date: 	2017-02-22 04:06:21
title: 	Auto Generating a requests.txt from a Python File
tags:   python pip
---

If you ever wondered how to get a requirements.txt from a folder containing Python files, there's an easy solution.
{% highlight bash %}
pip install pipreqs
pipreqs path_to_python_project
{% endhighlight %} 
There you go. You will have a requirements.txt that will encompass the files in your folder.
