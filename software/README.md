# Vision & Voice Localization Camera

Since there are two parts of our device, the software is also divided into two parts. 

The first part is human detection (YOLOv5) with central control logic running on PC, by folder /laptop

The second part is SSL running on Raspberry Pi Zero, containing relative SSL algorithms and basic drivers for the Respeaker module, by folder /raspberry pi

## How to Setup Software for this project

Firstly, set up the YOLOv5 on your laptop.
````
$ cd ./laptop
$ pip install -r requirements.txt  # install
````

Secondly, copy the ./raspberry_pi to your Raspberry Pi Desktop.

You should also set up basic drivers so as to run the Respeaker module.

Follow the setup steps [here](https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/).

Note that the laptop and Raspberry Pi are using serial communication, so a USB cable is needed.

You should also go to ./laptop/detect_mian.py and ./raspberry_pi/vad_doa_serial.py to change the serial port names.

## How to Run Software for this project

### Yolo5 (PC) part
````
$ conda activate yolo   # enter your python environment
$ (yolo) python3 detect_main.py --source 0 --classes 0
````

### Raspberry pi zero part
````
$ ssh pi@raspberrypi.local    # ssh + hostname of your pi
password:
$ cd ~/Desktop/mic_array      # cd to your working directory
$ sudo chmod 666 /dev/ttyGS0  # gain authority of the serial port
$ python3 vad_doa_serial.py
````

Note: the python program on PC (yolo5 part) will wait for the python program on the pi zero to start so that the serial communication will establish and the system can operate correctly.

### Raspberry pi zero VNC (optional)
You may wish to use VNC to get the remote control of your pi zero. To do that, first ssh to your pi zero:
````
$ ssh pi@raspberrypi.local   
password:
````
Then get the ip address of the pi zero:
````
$ ifconfig
````
Once you have the ip of the pi zero, you can start remote controlling with the help of VNC software like VNC connect.
