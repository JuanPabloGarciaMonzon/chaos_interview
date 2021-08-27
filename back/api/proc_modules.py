import json
def get_uptime():
    uptime = []
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    uptime.append(uptime_seconds)
    return uptime

def get_hostname():
    host = []
    with open('/proc/sys/kernel/hostname', 'r') as f:
        hostname = str(f.readline())
    host.append(hostname)
    return host

def get_loadavg():
    load = []
    count = 0
    with open('/proc/loadavg', 'r') as f:
        load1  = str(f.readline())
    load.append(float(load1.split()[0]))
    load.append(float(load1.split()[1]))
    load.append(float(load1.split()[2]))
    return load
