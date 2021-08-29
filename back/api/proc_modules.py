import json
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return str(uptime_seconds)

def get_hostname():
    with open('/proc/sys/kernel/hostname', 'r') as f:
        hostname = str(f.readline())
    return str(hostname)

def get_loadavg():
    with open('/proc/loadavg', 'r') as f:
        load1  = str(f.readline())
    load = {"1m":float(load1.split()[0]),"5m":float(load1.split()[1]),"15m":float(load1.split()[2])}
    print(load)
    return load
