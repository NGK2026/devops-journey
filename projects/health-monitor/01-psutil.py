# practice and explore file
# for cpu, memory and disk

# add prometheus client library

import psutil as ps
import prometheus_client as pc


## CPU
cpuCount = ps.cpu_count()
cpuNonLogical = ps.cpu_count(logical=False)
cpuPercent = ps.cpu_percent(interval=1)

print(
    f"\n===== ***** CPU ***** =====\n"
    f"CPU actual physical cores: {cpuNonLogical} cores\n"
    f"CPU logical cores: {cpuCount} threads\n"
    f"CPU currently at: {cpuPercent}% now"
)

# get cpu usage percent
# for x in range(5):
    # print(f"Currently {ps.cpu_percent(interval=1)}% used")


## MEMORY
memCurr = ps.virtual_memory().percent
memUsed = ps.virtual_memory().used
memFree = ps.virtual_memory().free
memTotal = ps.virtual_memory().total
# in GB
memGbTot = memTotal / (1024**3)
memGbUsed = memUsed / (1024**3)
memGbFree = memFree / (1024**3)
print(
    f"\n===== ***** MEMORY ***** =====\n"
    f"RAM total: {memGbTot:.2f} GB\n"
    f"RAM used: {memGbUsed:.2f} GB\n"
    f"RAM free: {memGbFree:.2f} GB\n"
    f"RAM usage currently at: {memCurr}%\n"
    f"RAM: {memGbUsed:.2f} GB / {memGbTot:.2f} GB ({memCurr}%)\n"
)

## DISK ROOT
diskTotal = ps.disk_usage('/').total
diskUsed = ps.disk_usage('/').used
diskFree = ps.disk_usage('/').free
diskCurr = ps.disk_usage('/').percent
# in GB
diskGbTotal = diskTotal / (1024**3)
diskGbUsed = diskUsed / (1024**3)
diskGbFree = diskFree / (1024**3)

print(
    f"\n===== ***** DISK ***** =====\n"
    f"** Root /:\n"
    f"Disk total: {diskGbTotal:.2f} GB\n"
    f"Disk used: {diskGbUsed:.2f} GB\n"
    f"Disk free: {diskGbFree:.2f} GB\n"
    f"Disk usage currently at: {diskCurr}%\n"
    f"Disk: {diskGbUsed:.2f} GB / {diskGbTotal:.2f} GB ({diskCurr}%)\n"
)

# DISK HOME
diskTotal = ps.disk_usage('/home').total
diskUsed = ps.disk_usage('/home').used
diskFree = ps.disk_usage('/home').free
diskCurr = ps.disk_usage('/home').percent
# in GB
diskGbTotal = diskTotal / (1024**3)
diskGbUsed = diskUsed / (1024**3)
diskGbFree = diskFree / (1024**3)

print(
    f"\n"
    f"** HOME /home:\n"
    f"Disk total: {diskGbTotal:.2f} GB\n"
    f"Disk used: {diskGbUsed:.2f} GB\n"
    f"Disk free: {diskGbFree:.2f} GB\n"
    f"Disk usage currently at: {diskCurr}%\n"
    f"Disk: {diskGbUsed:.2f} GB / {diskGbTotal:.2f} GB ({diskCurr}%)\n"
)

# Prometheus

cpu_gauge = pc.Gauge('cpu_usage_percent', 'Current CPU usage in percent')
cpu_gauge.set(ps.cpu_percent(interval=1))
