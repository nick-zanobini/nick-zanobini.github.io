Installing OctoPrint on a Raspberry Pi with a 5" Touch Screen

First download the latest Raspbian Image which can always be found [here](https://www.raspberrypi.org/downloads/raspbian/).

Flash this to your SD card using your favorite program (mine is [Etcher](https://etcher.io/))

Now insert the SD card to your Pi, power it up and connect via SSH.

Once connected run the following commands:

```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install gawk util-linux realpath qemu-user-static git

git clone https://github.com/guysoft/CustomPiOS.git
git clone https://github.com/guysoft/OctoPi.git

cd OctoPi/src/image
wget -c --trust-server-names 'https://downloads.raspberrypi.org/raspbian_lite_latest'

cd ..
../../CustomPiOS/src/update-custompios-paths

sudo modprobe loop
sudo bash -x ./build_dist
```

