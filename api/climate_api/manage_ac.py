import subprocess


def power_management(setting):
    command = "irsend SEND_ONCE clim {}".format(setting)
    return send_command(command)


def temperature_management(ac_mode, temperature, fan):
    command = "irsend SEND_ONCE clim {}_{}_{}".format(ac_mode, temperature, fan)
    return send_command(command)


def send_command(command):
    launched = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
    launched.wait()
    if launched.returncode == 0:
        return True
    return False


def timer(timer):
    time_to_wait = int(timer)*60
    command = "sleep {} && irsend SEND_ONCE clim poweroff".format(
        str(time_to_wait))
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True,
                     executable="/bin/bash")
    return True
