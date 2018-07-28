---
layout: single
title:  "Monitoring the Status of an Aerotech A3200 with Python"
date:   2018-07-28 12:30:00"
tags:   a3200 python automation 
comments: true
---

My company runs serval machines with [Aerotech A3200](https://www.aerotech.com/product-catalog/motion-controller/a3200.aspx) controllers and we wanted to remotly monitor the status of each machine in an effort to start building some metrics. 

The A3200 has a built in ASCII Command Interface that is accessable over a TCP connection on port 8000. By default this is not enabled. To enable it you have to change the command setup parameter in the A3200 Configuration Manager. 

It can be found here: Computer --> (System Version) --> System --> Communication --> ASCII

![ASCII Command Interface Setup](/assets/images/a3200_ascii_setup.png){:class="img-responsive"}

In order to enable the ASCII Command Interface the "CommandSetup" parameter needs to be set to `0x00010004`

After enabling it, the conroller needs to be reset inorder for it to take affect.

Now that it is enabled we can talk to the Aerotech controller with Python. Below is a script that will read the digial output of what is defined as the "X" axis. Since certain outputs are on only when running we can OR them together and deduce when the machine is runnning. 

To run this program for a machine with a different setup all that needs to change is the following:

`MACHINE_IP`, `MACHINE_PORT`, and `MASK`.


{% highlight python %}
#!/usr/bin/env python

# Credit goes to dwhitney67 for posting the TCPSocket classes on
# https://ubuntuforums.org/showthread.php?t=1306456

from datetime import datetime

import socket
import select


class TCPSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.sock.settimeout(3)

    def nonBlocking(self):
        self.sock.setblocking(0)

    def send(self, msg):
        totalSent = 0
        while totalSent < len(msg):
            sent = self.sock.send(msg[totalSent:])
            if sent == 0:
                raise RuntimeError("Socket Connection Broken.")
            totalSent += sent

    def recv(self, msgLen):
        msg = ""
        bytesRcvd = 0
        while bytesRcvd < msgLen:
            chunk = self.sock.recv(msgLen - bytesRcvd)

            if chunk == "": break

            bytesRcvd += len(chunk)
            msg       += chunk.decode('utf-8')

            if "\n" in msg: break
        return msg

    def activityDetected(self, timeout = 0):
        ready_to_read, ready_to_write, in_error = select.select([self.sock], [], [], timeout)
        return len(ready_to_read) > 0


class TCPClientSocket(TCPSocket):
    def __init__(self, sock=None):
        TCPSocket.__init__(self, sock)

    def connect(self, host, port):
        self.sock.connect((host, port))


class TCPServerSocket(TCPSocket):
    def __init__(self, sock=None):
        TCPSocket.__init__(self, sock)


def check_if_running(data, mask=0x1C):
    result = bool(mask & int(data.rstrip().replace('%', '')))
    return result


def check_if_machine_up(machine_ip, machine_port, mask):
    tcpClient = TCPClientSocket()
    try:
        tcpClient.connect(machine_ip, machine_port)
        tcpClient.nonBlocking()
        tcpClient.send(b'AXISSTATUS (X, DATAITEM_DigitalOutput)\n')
        if tcpClient.activityDetected(5):
            response = tcpClient.recv(1024)
            if response[0] != '%': return None
            return check_if_running(response, mask)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    MACHINE_IP = '192.168.168.111'
    MACHINE_PORT = 8000
    MASK = 0x1C

    # 0x1C = 28 in decimal = 0001 1100 in binary
    # outputs 2, 3, and 4 are on when the machine is running

    machine_status = check_if_machine_up(MACHINE_IP, MACHINE_PORT, MASK)

{% endhighlight %} 



