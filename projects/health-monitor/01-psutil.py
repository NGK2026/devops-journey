# practice and explore file
# for cpu, memory and disk

import psutil as ps

## CPU
cpuCount = ps.cpu_count()
cpuNonLogical = ps.cpu_count(logical=False)
cpuPercent = ps.cpu_percent(interval=1)

print(
    f"\n===== ***** CPU ***** =====\n"
    f"CPU actual physical cores: {cpuNonLogical} cores\n"
    f"CPU logical cores: {cpuCount} threads\n"
    f"CPU currently at: {cpuPercent} now"
)

# get cpu usage percent
# for x in range(5):
    # print(f"Currently {ps.cpu_percent(interval=1)}% used")


## MEMORY
memCurr = ps.virtual_memory().percent
memUsed = ps.virtual_memory().used
memFree = ps.virtual_memory().free
memTotal = ps.virtual_memory().total
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

## DISK
diskTotal = ps.disk_usage('/').total
diskUsed = ps.disk_usage('/').used
diskFree = ps.disk_usage('/').free
diskCurr = 