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
- [sysctl](#sysctl)

##### Shows all modules currently loaded
```sh
$ lsmod
```
##### Used to manually load a kernel file, including its dependencies
```sh
$ modprobe 
```
##### Used to manually unload a kernel file
```sh
$ modprobe -r 
```
##### Provides information about kernel modules
```sh
$ modinfo 
```
##### Generates the modules.dep kernel module dependencies file
```sh
$ depmod 
```
##### View every process on the system
```sh
$ ps aux 
```
##### Memory info
```sh
$ meminfo
```
##### CPU info
```sh
$ cpuinfo
```
##### MAN pages find swappiness
```sh
$ man -K swappiness

--Man-- next: docker-container-run(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-create(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-run(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-service-create(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: docker-service-update(1) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: tmpfiles.d(5) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
--Man-- next: proc_sys_vm(5) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]
```
##### sysctl 
- Interface to manage /proc
- Persistent setting management, using /etc/sysctl.conf and includes files in /etc/sysctl.d/
- configuring 'swappiness' results in parameters (from > to):
```txt
/proc/sys/vm/swappiness becomes vm.swappiness
```
-Commands:
```sh
$ sysclt -a # all sysctl parameters
fs.binfmt_misc.DOSWin = offset 0
fs.binfmt_misc.DOSWin = magic 4d5a
fs.binfmt_misc.status = enabled
fs.dentry-negative = 0
fs.dentry-state = 281277        225273  45      0       45704   0
fs.dir-notify-enable = 1
fs.epoll.max_user_watches = 7072300
:sysctl: permission denied on key 'kernel.usermodehelper.bset'
--snip--

$ sysclt -a | wc -l # count lines
1449


$ echo vm.swappiness=60 > /etc/sysctl.d/swappiness.conf

$ sysctl -a | grep swapp

$ sysctl -p /etc/sysctl.d/swappiness.conf

$ sysctl -a | grep swapp
```