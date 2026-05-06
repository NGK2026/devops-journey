# practice and explore file
# for cpu, memory and disk

import psutil as ps

## CPU
cpuCount = ps.cpu_count()
nonLogicalCpu = ps.cpu_count(logical=False)
cpuPercent = ps.cpu_percent(interval=1)

print(
    f"\n===== ***** CPU ***** =====\n"
    f"CPU actual physical cores: {nonLogicalCpu} cores\n"
    f"CPU logical cores: {cpuCount} threads\n"
    f"CPU currently at: {cpuPercent} now"
)

# get cpu usage percent
# for x in range(5):
    # print(f"Currently {ps.cpu_percent(interval=1)}% used")


## MEMORY
currentMem = ps.virtual_memory().percent
usedMem = ps.virtual_memory().used
freeMem = ps.virtual_memory().free
totalMem = ps.virtual_memory().total
totalGB = totalMem / (1024**3)
usedGB = usedMem / (1024**3)
freeGB = freeMem / (1024**3)
print(
    f"\n===== ***** MEMORY ***** =====\n"
    f"RAM total: {totalGB:.2f} GB\n"
    f"RAM used: {usedGB:.2f} GB\n"
    f"RAM free: {freeGB:.2f} GB\n"
    f"RAM usage currently at: {currentMem}%\n"
    f"RAM: {usedGB:.2f} GB / {totalGB:.2f} GB ({currentMem}%)\n"
)

## DISK