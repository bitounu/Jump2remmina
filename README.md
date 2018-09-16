# JumpDesktop to Remmina private converter

I just switched back to Linux from OSX and need replacement 
for JumpDesktop. JumpDesktop is very good software that allows
RDP and VNC (and SSH) remote sessions to computers.
Almost ideal alternative in Linux is Remmina but both use
different type of configuration files.
JumpDesktop uses *json* while Remmina files are *ini*.
I have a lot such connections for my work so, I wrote small 
tool to convert them all in one run to Remmina.

One can use it this way (*could change if I spend more time 
on this*):
`./jump2remmina.py -i jumpdesktopfile.jump > remminafile.remmina`
Of course to convert all files in derectory one can use simple script:
```bash
#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for file in *.jump; do
  ./jump2remmina.py -i ${file} >  `basename ${file} .jump`.remmina
done
IFS=$SAVEIFS
```
The `IFS` stuff in the beginning of bash is to take care of files 
with spaces in names (Aghhhhhr!).
