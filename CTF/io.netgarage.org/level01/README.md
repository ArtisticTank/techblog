
### Level01

Hey everyone today we'd try to solve the io.netgarage CTF level01 puzzle.

You can connect to their SSH Server using the following command in terminal

```sh
root@kali:~# ssh level1@io.netgarage.org
```
###### Password : level1

```sh
level1@io:/levels$ ls -l level01*
-r-sr-x--- 1 level2 level1 1184 Jan 13  2014 level01
```




You may find the challenge in /levels directory navigate there by command
```sh
level1@io:~$ cd /levels
```
Our first challenge is a file called as level01
```sh
level1@io:/levels$ ls -l level01
-r-sr-x--- 1 level2 level1 1184 Jan 13  2014 level01
```
```sh
level1@io:/levels$ file level01
level01: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, not stripped
```

```sh
level1@io:/levels$ ./level01
Enter the 3 digit passcode to enter:
```

```sh
level1@io:/levels$ cat level01
ELF�4�4 (%%(((||h(��=�B�d������̀��1�1��< t�,0<	w
k�
�1�����؁�ø��M�P̀1���PS�ᙰ
                      ø�̀�L$���%̀�Enter the 3 digit passcode to enter: Congrats you found it, now read the password for level2 from /home/level2/.pass
��#-49>�C(KMS�Y�`���l���s���level01.asmfscanfskipwhitedoitexitscanfYouWinexitputsmainprompt1prompt2shell_start__bss_start_edata_end
```

```sh
level1@io:/levels$ strings level01
,0<	w
Enter the 3 digit passcode to enter: Congrats you found it, now read the password for level2 from /home/level2/.pass
/bin/sh
.symtab
.strtab
.shstrtab
.text
.lib
.data
level01.asm
fscanf
skipwhite
doit
exitscanf
YouWin
exit
puts
main
prompt1
prompt2
shell
_start
__bss_start
_edata
_end
```

```sh
level1@io:/levels$ gdb level01
GNU gdb (Debian 7.12-6) 7.12.0.20161007-git
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from level01...(no debugging symbols found)...done.
(gdb) 

(gdb) disassemble main
Dump of assembler code for function main:
   0x08048080 <+0>:	push   $0x8049128
   0x08048085 <+5>:	call   0x804810f
   0x0804808a <+10>:	call   0x804809f
   0x0804808f <+15>:	cmp    $0x10f,%eax
   0x08048094 <+20>:	je     0x80480dc
   0x0804809a <+26>:	call   0x8048103
End of assembler dump.
```
```python
import sys
def hextodecimal(digit):
    return int(digit, 16)

if __name__ == "__main__":
    hexstring = sys.argv[1]
    print(hextodecimal(hexstring))
```
```sh
root@kali:~/pythonworkspace# python hextodec.py 0x10f
271
```
```sh
level1@io:/levels$ ./level01 
Enter the 3 digit passcode to enter: 271
Congrats you found it, now read the password for level2 from /home/level2/.pass
sh-4.3$ 
```
```sh
sh-4.3$ cat /home/level2/.pass
XNWFtWKWHhaaXoKI
```




