climate-controller
===

Control a TOSHIBA AC with a anavi infrared PHAT plugged on a raspberry pi.

How it works ?
==============
I've copied my Toshiba A/C remote using lircd in RAW mode.
I've made an API with Python Flask that sends command to lirc.

What can I do with that ?
=========================
* You can manage your AC temperature and mode (cool or heat)
* You can start and stop your AC. It will restart using last preset
* You can set a timer to stop your AC

What can't I do with that ?
===========================
* You can't change fan speed, I've only recorded temperatures in AUTO mode (this should be available sometimes) :)

How can I install this ?
========================
Please refer to [this doc](setup.md)


How can I use it ?
==================
If you're a tough bearded men, CURL will be sufficient !
If you have an Android phone, I recommend using HTTP shortcuts to ease using :)





