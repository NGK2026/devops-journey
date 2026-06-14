## Table of Contents
- [Show all modules](#shows-all-modules-currently-loaded)
- [Manually load kernel file](#used-to-manually-load-a-kernel-file,-including-its-dependencies)
- [Manually unload kernel file](#used-to-manually-unload-a-kernel-file)
- [Kernel module information](#provides-information-about-kernel-modules)
- [Generate modules.dep dependencies file](#generates-the-modules.dep-kernel-module-dependencies-file)
- [View all processes](#view-every-process-on-the-system)
- [View Memory info](#memory-info)
- [View CPU info](#cpu-info)
- [Find MAN](#man-pages-find-swappiness)

##### Shows all modules currently loaded
```sh
lsmod
```
##### Used to manually load a kernel file, including its dependencies
```sh
modprobe 
```
##### Used to manually unload a kernel file
```sh
modprobe -r 
```
##### Provides information about kernel modules
```sh
modinfo 
```
##### Generates the modules.dep kernel module dependencies file
```sh
depmod 
```
##### View every process on the system
```sh
ps aux 
```
##### Memory info
```sh
meminfo
```
##### CPU info
```sh
cpuinfo
```
##### MAN pages find swappiness
```sh
man -K swappiness

--Man-- next: docker-container-run(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-create(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-run(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-service-create(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-service-update(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]

--Man-- next: tmpfiles.d(5) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: proc_sys_vm(5) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
```