---
layout: single
title:  "Bootstrapping Python Programs on Windows"
date:   2018-9-29 10:30:00"
tags:   python windows 
comments: true
---

How do you ensure a python program will run on a Windows system and continue to run even if it gets stopped/halted/hung up somewhere. 

While you could do this with another python program its also as easy to do it with a batch file. It isn't the cleanest way to run applications but if your program is relatively simple then it is a perfect way to make sure it works. It also prevents memory leaks, a common problem with programs that use: 

{% highlight python %}
while True:
	do something
{% endhighlight %} 

To do this I make a batch file that activates my virtual enviorment and then calls my python program. Then I make another batch file that checks if the first batch file is running, kills it if it is and starts it again. 

Then I create a Windows Scheduled Task that calls the second batch file every hour of every day. 

(Note: I use this method to generate raw html pages based on data pulled from our database. These pages are used to track jobs throughout our shop.) 

`program.py`
{% highlight python %}
#!/usr/bin/env python
from time import sleep
count = 0
while True:
	count += 1
	print(count)
	sleep(1)
{% endhighlight %} 

`run_program.bat`
{% highlight bat %}
CD %CD% && CD env/Scripts && CALL activate.bat && cd ../..
CALL python program.py
{% endhighlight %} 

`bootstrap_program.bat`
{% highlight bat %}

{% endhighlight %} 

![Windows Scheduled Task](/assets/images/windows_scheduled_task.png){:class="img-responsive"}



















