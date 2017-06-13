---
layout: post
title: Link Raspberry Pi Hardware Clock to the Local Time
date: 2017-02-16 04:54
author: nickzanobini
comments: true
categories: [Uncategorized]
---
Often times Cron uses the hwclock to execute its schedule. To make sure this happens at the right time you need to sync the two times. First check if they are the same.
<code>date ; date -u</code>
The system clock gets set to either UTC or Local based on the last option used when the hwclock function was run. If you run:
<code>hwclock -w --localtime</code>
This should write your system clock to local time instead of UTC and should subsequently set it and read it at boot using local time. If you manually set your system clock and the hwclock was last specified with UTC then it will automatically set it back to UTC.
<a href="http://askubuntu.com/questions/175452/hwclock-not-in-sync-with-system-clock">Source</a>
