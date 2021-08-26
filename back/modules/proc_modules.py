def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds

def get_hostname():
    with open('/proc/sys/kernel/hostname', 'r') as f:
        hostname = str(f.readline())

    return hostname

def get_loadavg():
    load = []
    count = 0
    with open('/proc/loadavg', 'r') as f:
        load1  = str(f.readline())
    load.append(float(load1.split()[0]))
    load.append(float(load1.split()[1]))
    load.append(float(load1.split()[2]))
    return load

print(get_uptime())
print(get_hostname())
print(get_loadavg())
