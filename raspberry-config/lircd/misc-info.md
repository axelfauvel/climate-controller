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


Turn off device
---
`irsend SEND_ONCE clim poweroff`

Change temperature
---
`irsend SEND_ONCE clim <heat or clim>_<temp>_<fan_power>` 

fan-power can only be `auto`

example :
`irsend SEND_ONCE clim heat_20_auto`
`irsend SEND_ONCE clim clim_19_auto`


