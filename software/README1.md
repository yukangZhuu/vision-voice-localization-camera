# Visual and Sound Tracking Fusion Camera


## Hardware modules


## Software and control logic

## Commands to setup and run the program


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

Note: the python program on PC (yolo5 part) will wait for the python program on the pi zero to start so that the serail communication will establish and the system can operate correctly.

### Raspberry pi zero VNC (optinal)
You may wish to use VNC to get the remote control of your pi zero. To do that, first ssh to your pi zero:
````
$ ssh pi@raspberrypi.local   
password:
````
Then get the ip adress of the pi zero:
````
$ ifconfig
````
Once you have the ip of the pi zero, you can start remote controlling with the help of VNC software like VNC connect.