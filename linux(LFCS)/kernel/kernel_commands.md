## Table of Contents
- [Show all modules](#shows_all_modules_currently_loaded)
- [Manually load kernel file](#used_to_manually_load_a_kernel_file,_including_its_dependencies)
- [Manually unload kernel file](#used_to_manually_unload_a_kernel_file)
- [Kernel module information](#provides_information_about_kernel_modules)
- [Generate modules.dep dependencies file](#generates_the_modules.dep_kernel_module_dependencies_file)
- [View all processes](#view_every_process_on_the_system)

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
