#!/usr/bin/python3
# -*- coding: utf-8 -*-
from os import *
from time import *
from colorama import *
import sys
init(autoreset=True)
if sys.platform != "linux":
       print("This only works on Linux systems for now")
       sys.exit(1)

banner="""
 _____               _             "To those who physically harm
| ____|_  _____  ___| |_ ___  _ __  no pity in cyberspace!"
|  _| \ \/ / _ \/ __| __/ _ \| '__|
| |___ >  <  __/ (__| || (_) | |
|_____/_/\_\___|\___|\__\___/|_|
Author: Mah63 | Tool: Exector"""

banner1="""
..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...           Author: Mah63
  ....                ,ONkc;,;cokOdc',.         Tool: Exector
 .                   OMo           ':ddo.       "To those who physically harm
                    dMc               :OO;      no pity in cyberspace!"
                    0M.                 .:o.    Exector: Control Tools
                    ;Wd                         panel. By testing it in the field, 
                     ;XO,                       software i use added as a module.
                       ,d0Odlc;,..              It is also available as a module in 
                           ..',;:cdOOd::,.      the software I personally wrote.
                                    .:d;.':;.
                                       'd,  .'
                                         ;l   ..
                                          .o
                                            c
                                            .'
                                             .
"""
#print(Fore.GREEN+banner)
#print(Fore.BLUE+banner1)
#print(Fore.CYAN+"Coding By Mah63")
komut=["exit","clear","whoami","help","modules","use","use toriptables3","use toriptables","use Toriptables3","use installer","use Installer","use cupp"]
bos=[""," ","  ","   ","    "]
tam=komut + bos
#fonksiyon için boş yer
def echo_exec(name):
    a=Fore.RED+"["
    b=Fore.RED+"]:"
    c=Fore.BLUE+"*"
    print(a+c+b+Fore.GREEN+" komut çalıştırıldı: "+Fore.CYAN+name)
if getuid()!=0:
    slah=Fore.YELLOW+"$"
    e=Fore.WHITE+"hacker"
    print(Fore.GREEN+banner)
    print(Fore.CYAN+"Coding By Mah63"+Fore.WHITE+" | "+Fore.RED+"Standard Permissions")


if getuid() ==0:
    slah=Fore.YELLOW+"#"
    e=Fore.WHITE+"root"
    print(Fore.BLUE+banner1)
    print(Fore.CYAN+"Coding By Mah63 "+Fore.WHITE+"| "+Fore.RED+"System God(root) Permissions")
##new func
current_time = localtime()
ctime = strftime('%H:%M:%S', current_time)
print('[' + ctime + ']') 
#print(t("Happy hunting"))

#print(slah)
while True:
    q=Fore.RED+"["
    w=Fore.RED+"]"
    #e=Fore.GREEN+"Mahmut"
    r=Fore.YELLOW+"@"
    t=Fore.BLUE+"Exector"
    s=Fore.BLUE+"("
    d=Fore.BLUE+")"
    f=Fore.RED+"Exector/"
    g=Fore.WHITE+":"
    y=Fore.RED+":"
    u=Fore.YELLOW+"="
    o=Fore.BLUE+">"
    p=Fore.CYAN+">"
    A=Fore.WHITE+" "
    h=Fore.GREEN+"uid="
    j=Fore.WHITE+"["
    k=Fore.WHITE+"]"
    current_time = localtime()
    ctime = strftime('%H:%M:%S', current_time)
    atime=j+ctime+k
    sh=input(q+e+r+t+w+g+s+f+d+g+h+slah+g+j+Fore.BLUE+ctime+k+"\n"+y+u+o+p+A)
    if sh=="exit":
        print(j+ctime+k+" Exiting to system")
        exit(Fore.RED+"Goodbye!!!\n")
    if not sh in tam:
        print(Fore.RED+"Hatalı komut: "+Fore.CYAN+sh)
    if sh=="clear":
        system("clear")
    if sh=="whoami":
        print(atime+" Command exected: 'whoami'")
        system("whoami")
    if sh=="help":
        print("help: lists commands.")
        print("exit: quit.")
        print("clear: clears terminal.")
        print("whoami: which user are you?")
        print("modules: lists modules.\nThere are two categories: Mah 63 modules, Exector modules.")
        print("use: enable module use. Example: use my_module")
    if sh=="modules":
        print(Fore.RED+"Modules:")
        print(Fore.BLUE+"Exector modules:")
        print(Fore.WHITE+"Toriptables3: Anonomity tool.")
        print(Fore.WHITE+"cupp: wordlist generetor.")
        print(Fore.YELLOW+"Mah63 modules:")
        print(Fore.WHITE+"Installer: it is intaller tool.")
    if sh=="use":
        print("modül kullanımını sağlar. Örnek: use toriptables3")
    if sh=="use toriptables" or sh=="use Toriptables3" or sh=="use toriptables3":
        #print("modülü yazz!!")
        while True:
            f1=Fore.RED+"Exector/modules/toriptables3/"
            sh1=input(q+e+r+t+w+g+s+f1+d+g+h+slah+y+j+Fore.BLUE+ctime+k+"\n"+y+u+o+p+A)
            if sh1=="exit":
                exit("exiting...")
            #/modules/toriptables3  dizini
            cmd_ti3=["info","exit","back","help","load","ip","refresh","flush",""," ","  ","   "]
            help_ti3="""
            help: komutları listeler
            back: geri gitme (yazılım içi)
            load: yazılımı aktif eder
            flush: yazılımı sonlandırır(aktifliği biter)
            ip: ip bilgisi verir
            refresh: program aktifken yeni ip verir
            exit: yazılımdan direkt çıkış
            info: yazılımla ilgili bilgi verir.
            """
            if sh1 not in cmd_ti3:
                print(Fore.RED+"hatalı komut: "+Fore.BLUE+sh1)
            if sh1=="help":
                print(help_ti3)
            if sh1=="load":
                #system("sudo service tor start")
                system("sudo python3 modules/toriptables3/toriptables3.py -l")
            if sh1=="flush":
                system("sudo python3 modules/toriptables3/toriptables3.py -f")
            if sh1=="info":
                print("yazz bilgi falan")
            if sh1=="refresh":
            	system("sudo python3 modules/toriptables3/toriptables3.py -r")
            if sh1=="ip":
            	system("sudo python3 modules/toriptables3/toriptables3.py -i")
    if sh=="use cupp":
        while True:
            f1=Fore.RED+"Exector/modules/cupp/"
            sh2=input(q+e+r+t+w+g+s+f1+d+g+h+slah+y+j+Fore.BLUE+ctime+k+"\n"+y+u+o+p+A)
            if sh2=="help":
                print("help: it is help")
                print("run: runing software")
                print("install: wordlist install mod.")
            if sh2=="run": 
                system("python3 modules/cupp/cupp.py -i")
            if sh2=="install":
                system("python3 modules/cupp/cupp.py -l")
            if sh2=="exit":
                exit()
    if sh=="use installer" or sh=="use Installer":
        echo_exec("python3 modules/Mah63/installer/installer.py")
        system("python3 modules/Mah63/installer/installer.py")
 

else:
    exit("hata hata hata")
