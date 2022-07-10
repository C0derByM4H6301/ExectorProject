#!/usr/bin/python3
# -*- coding: utf-8 -*-
from os import *
from time import *
from colorama import *
init(autoreset=True)
banner="""
 _____               _
| ____|_  _____  ___| |_ ___  _ __
|  _| \ \/ / _ \/ __| __/ _ \| '__|
| |___ >  <  __/ (__| || (_) | |
|_____/_/\_\___|\___|\__\___/|_|"""

banner1="""
..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...           Author: Mah63
  ....                ,ONkc;,;cokOdc',.         Tool: Exector
 .                   OMo           ':ddo.       "Fizikselde zarar verene
                    dMc               :OO;      siber alemde acımak yok!"
                    0M.                 .:o.    Exector: Araçlar(Tools) kontrol
                    ;Wd                         paneli. Alanında test edip, 
                     ;XO,                       kullandığım yazılımlar 
                       ,d0Odlc;,..              modül olarak eklenmiştir.
                           ..',;:cdOOd::,.
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
komut=["exit","clear","whoami","help","modules","use","use toriptables3","use toriptables","use Toriptables3","use installer","use Installer"]
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
    e=Fore.GREEN+"Mahmut"
    print(Fore.GREEN+banner)
    print(Fore.CYAN+"Coding By Mah63"+Fore.WHITE+" | "+Fore.RED+"Standard Permissions")


if getuid() ==0:
    slah=Fore.YELLOW+"#"
    e=Fore.GREEN+"root"
    print(Fore.BLUE+banner1)
    print(Fore.CYAN+"Coding By Mah63 "+Fore.WHITE+"| "+Fore.RED+"System God(root) Permissions")

#print(slah)
while True:
    q=Fore.RED+"["
    w=Fore.RED+"]"
    #e=Fore.GREEN+"Mahmut"
    r=Fore.YELLOW+"@"
    t=Fore.BLUE+"devaloper"
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
    sh=input(q+e+r+t+w+g+s+f+d+g+h+slah+"\n"+y+u+o+p+A)
    if sh=="exit":
        exit(Fore.RED+"Goodbye!!!\n")
    if not sh in tam:
        print(Fore.RED+"Hatalı komut: "+Fore.CYAN+sh)
    if sh=="clear":
        system("clear")
    if sh=="whoami":
        system("whoami")
    if sh=="help":
        print("help: komutları listeler.")
        print("exit: çıkmak.")
        print("clear: terminali temizler.")
        print("whoami: hangi kullanıcısın?")
        print("modules: modülleri listeler.\nİki katagori var: Mah63 modules, Exector modules.")
        print("use: modül kullanımını sağlar. Örnek: use Modülimi")
    if sh=="modules":
        print(Fore.RED+"Modules:")
        print(Fore.BLUE+"Exector modules:")
        print(Fore.WHITE+"Toriptables3: Anonomity tool.")
        print(Fore.YELLOW+"Mah63 modules:")
        print(Fore.WHITE+"Installer: it is intaller tool.")
    if sh=="use":
        print("modül kullanımını sağlar. Örnek: use toriptables3")
    if sh=="use toriptables" or sh=="use Toriptables3" or sh=="use toriptables3":
        print("modülü yazz!!")
        while True:
            f1=Fore.RED+"Exector/modules/toriptables3/"
            sh1=input(q+e+r+t+w+g+s+f1+d+g+h+slah+"\n"+y+u+o+p+A)
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
    if sh=="use installer" or sh=="Installer":
        echo_exec("python3 modules/Mah63/installer/installer.py")
        system("python3 modules/Mah63/installer/installer.py")
 

else:
    exit("hata hata hata")
