#!/usr/bin/python3
#Coding By Mah:63
#https://github.com/C0derByM4H6301
from os import *
from colorama import *
init(autoreset=True)
banner="""
 _   _           _       _              _
| | | |_ __   __| | __ _| |_ ___ _ __  | |_ ___
| | | | '_ \ / _` |/ _` | __/ _ \ '__| | __/ _ \ 
| |_| | |_) | (_| | (_| | ||  __/ |    | || (_) |
 \___/| .__/ \__,_|\__,_|\__\___|_|     \__\___/
      |_|
 _____               _
| ____|_  _____  ___| |_ ___  _ __
|  _| \ \/ / _ \/ __| __/ _ \| '__|
| |___ >  <  __/ (__| || (_) | |
|_____/_/\_\___|\___|\__\___/|_| """
print(Style.BRIGHT+Fore.RED+banner)
print(Fore.CYAN+"Coding By Mah:63")
print(Fore.YELLOW+"https://github.com/C0derByM4H6301")
system("chmod 777 updater_file/updater.sh")
system("cd .. && mv ExeectorProject/updater_file/updater.sh . && rm -rf ExectorProject/ && bash updater.sh")

print(Fore.RED+"\n Bug found, please type terminal 'cd ..'")
