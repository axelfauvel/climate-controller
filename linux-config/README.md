# Setup
```
sudo apt-get update
sudo apt-get install -y lirc
```

Append the following config in /etc/modules
```
lirc_dev
lirc_rpi gpio_in_pin=18 gpio_out_pin=17
```


set following config in /etc/lirc/hardware.conf
```
# /etc/lirc/hardware.conf
#
# Arguments which will be used when launching lircd
LIRCD_ARGS="--uinput"
#Don't start lircmd even if there seems to be a good config file
#START_LIRCMD=false
#Don't start irexec, even if a good config file seems to exist.
#START_IREXEC=false
#Try to load appropriate kernel modules
LOAD_MODULES=true
# Run "lircd --driver=help" for a list of supported drivers.
#DRIVER="UNCONFIGURED"
DRIVER="default"
# usually /dev/lirc0 is the correct setting for systems using udev
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
```

Append following config /etc/lirc/lirc_options.conf
```
driver = default
device = /dev/lirc0
```

Append following config /boot/config.txt
```
dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=17
```

restart device

Start remote recording
---
stop lircd  
`systemctl lircd stop`

Trick, force raw mode recording  
`irrecord -f -n -d /dev/lirc0 ~/lirc.conf`

Copy config file  
`sudo cp clim.lircd.conf /etc/lirc/lircd.conf`

start lircd  
`systemctl lircd start`

update config file  
`irrecord -f -n -u clim.lircd.conf`
