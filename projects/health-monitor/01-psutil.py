# practice and explore file
# for cpu, memory and disk

import psutil as ps

cpuCount = ps.cpu_count()
nonLogicalCpu = ps.cpu_count(logical=False)

print(
    f"CPU logical cores: {cpuCount} threads.\n"
    f"CPU actual physical cores: {nonLogicalCpu} cores.\n"
)

# get cpu usage percent
for x in range(5):
    print(f"Currently {ps.cpu_percent(interval=1)}% used")

