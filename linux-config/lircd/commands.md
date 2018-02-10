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
