## Table of Contents
- [Show all modules](#shows-all-modules-currently-loaded)
- [Manually load kernel file](#used-to-manually-load-a-kernel-file,-including-its-dependencies)
- [Manually unload kernel file](#used-to-manually-unload-a-kernel-file)
- [Kernel module information](#provides-information-about-kernel-modules)
- [Generate modules.dep dependencies file](#generates-the-modules.dep-kernel-module-dependencies-file)
- [View all processes](#view-every-process-on-the-system)

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
