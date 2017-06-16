---
layout: post
title: Simple Python Scripts: Daily Reminders
date: 2016-11-23 05:40
author: nickzanobini
comments: true
categories: [python, pythonSMS, quoteOfTheDay, raspberrypi, reminder, rpi, simple]
---
<p dir="auto">Every morning I log into my computer and chrome opens up a blank tab with the Momentum extension loaded. My favorite thing is the daily quote that is displayed. I thought wouldn’t it be nice if I could get a text message every day with a good quote? So I went into researching the easiest way to send text messages from python. I came across two options:</p>

<ol>
	<li>Twilio’s free trial account which doesn’t expire (That I know of)</li>
	<li>Gmail’s SMS Gateway</li>
</ol>
<p dir="ltr">I have tried both and frankly they both do the same thing. Using the free version of Twilio there is a irremovable header attached to every message. I have included one of my daily texts below. If you take the Gmail SMS Gateway route then the message will appear as a text from yourself assuming your email is saved under your contact info. It is important to note, in order to get the Gmail route working I had to enable 2-Factor Authentication on my Gmail account and then get an app specific password to sign in with. With the security setting the way they were on my account this was my only option.</p>

<blockquote>Sent from your Twilio trial account - Patience, persistence and perspiration make an unbeatable combination for success.</blockquote>
<p dir="ltr">After sending the timeless classic “Hello World” to myself from both services I dug into finding an easy way to get a daily quote and options to have it sent everyday. For the daily quote I stumbled upon Goodreads Quote of the Day package that generates a new quote every day for me.</p>
<p dir="ltr">Next I looked into how I was going to get it sent to me everyday. I am going to be running this script on my Raspberry Pi; there are a ton of options for scheduling and running scripts or services out there.</p>

<ol>
	<li>Crontab</li>
	<li>Using python’s <code>threading.Timer()</code> function</li>
	<li>Writing a custom sleep function to pull the current time and calculate the amount of time to sleep</li>
</ol>
<p dir="ltr">I have used crontab for several things in the past and for what I needed it for it worked, but people complain about it so I decided why not, I'll write a function to sleep until its time to post. It was surprisingly simple. Using the datetime package I was able to get the current time and create a datetime object for the following time at the desired time, 6:30 AM in my case. I simply subtracted tomorrow’s datetime object from current time and then converted the difference to seconds. With the amount of seconds until the next day at 6:30 AM, I simply set the script to sleep for x seconds. I am still testing using the <code>threading.Timer()</code> function and will provide an update when I am done.</p>
<p dir="ltr">Here’s the code for sending a text with the quote of the day using Twilio:</p>
[code language="python" light="true"]#!/usr/bin/env python
from twilio.rest import TwilioRestClient
from goodreads_quotes import Goodreads
from time import sleep
import datetime as dt

def wait_to_tomorrow(now, time_to_text_tomorrow):
    '''Wait to tomorrow'''
    tomorrow = dt.datetime.replace(
        now + dt.timedelta(days=1), hour=time_to_text_tomorrow, minute=30, second=0)
    delta = tomorrow - now
    sleep_time = delta.total_seconds()
    return int(sleep_time)

def send_message(msg):
    # Your Account SID from www.twilio.com/console
    account_sid = &quot;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&quot;
    # Your Auth Token from www.twilio.com/console
    auth_token = &quot;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&quot;
    # country code and 10 digit Twilio number
    twillio_num = &quot;+19998675309&quot;
    # country code and 10 digit number text is sent to
    my_phone_num = &quot;+12345678901&quot;
    # twillio client login
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=msg,
                                     to=my_phone_num,    # Replace with your phone number
                                     from_=twillio_num)  # Replace with your Twilio number

def main():
    while True:
        # Get day of week Monday = 0, Sunday = 6
        day_of_week = dt.date.today().weekday()
        # get current time
        now = dt.datetime.now()
        # Random times to text myself
        time = [18, 17, 13, 11, 7, 22, 13]
        # todays text time
        time_to_text = time[day_of_week]
        # tomorrow's text time
        time_to_text_tomorrow = time[day_of_week + 1]
        # message to text
        qotd = (Goodreads.get_daily_quote())
        msg = qotd['quote']
        if now.hour == time_to_text:
            # send sms
            send_message(msg)
        # sleep till tomorrow's most time
        time_to_tomorrow = wait_to_tomorrow(now, time_to_text_tomorrow)
        # sleep until text time tomorrow
        sleep(time_to_tomorrow)

if __name__ == '__main__':
    main()[/code]

Here’s the code for sending a text with the quote of the day using Gmail’s SMS gateway

[code language="python" light="true"]#!/usr/bin/env python
from goodreads_quotes import Goodreads
from time import sleep
import datetime as dt
import smtplib

def wait_to_tomorrow(now, time_to_text_tomorrow):
    '''Wait to tomorrow'''
    tomorrow = dt.datetime.replace(
        now + dt.timedelta(days=1), hour=time_to_text_tomorrow, minute=30, second=0)
    delta = tomorrow - now
    sleep_time = delta.total_seconds()
    return int(sleep_time)

def send_message(msg):
    # connect, open and login to gmail sms server
    server = smtplib.SMTP(&quot;smtp.gmail.com&quot;, 587)
    server.starttls()
    server.login('user_name@gmail.com', 'google_app_specific_password')
    # send message
    server.sendmail(&quot;Python Scripts&quot;, '999867309@mms.att.net', msg)
    # close connection to gmail server
    server.close()

def main():
    while True:
        # Get day of week Monday = 0, Sunday = 6
        day_of_week = dt.date.today().weekday()
        # get current time
        now = dt.datetime.now()
        # Random times to text myself
        time = [18, 17, 13, 11, 7, 22, 13]
        # todays text time
        time_to_text = time[day_of_week]
        # tomorrow's text time
        time_to_text_tomorrow = time[day_of_week + 1]
        # message to text
        qotd = (Goodreads.get_daily_quote())
        msg = qotd['quote']
        if now.hour == time_to_text:
            # send sms
            send_message(msg)
        # sleep till tomorrow's most time
        time_to_tomorrow = wait_to_tomorrow(now, time_to_text_tomorrow)
        # sleep until text time tomorrow
        sleep(time_to_tomorrow)

if __name__ == '__main__':
    main()[/code]
