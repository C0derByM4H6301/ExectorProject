#!/usr/bin/python3
from colorama import *
from os import *
from time import *
banneri1="""
 _           _        _ _           
(_)_ __  ___| |_ __ _| | | ___ _ __ 
| | '_ \/ __| __/ _` | | |/ _ \ '__|
| | | | \__ \ || (_| | | |  __/ |   
|_|_| |_|___/\__\__,_|_|_|\___|_|
	"""
#print(Fore.YELLOW+banneri1)
if getuid()!=0:
    slah=Fore.YELLOW+"$"
    e=Fore.GREEN+"Exector"
    print(Fore.YELLOW+banneri1)
    print(Fore.CYAN+"Coding By Mah63"+Fore.WHITE+" | "+Fore.RED+"Standard Permissions")


if getuid() ==0:
    slah=Fore.YELLOW+"#"
    e=Fore.GREEN+"root"
    print(Fore.YELLOW+banneri1)
    print(Fore.CYAN+"Coding By Mah63 "+Fore.WHITE+"| "+Fore.RED+"System God(root) Permissions")
q=Fore.RED+"["
w=Fore.RED+"]"
#e=Fore.GREEN+"Mahmut"
r=Fore.YELLOW+"@"
t=Fore.BLUE+"installer"
s=Fore.BLUE+"("
d=Fore.BLUE+")"
#f=Fore.RED+"Exector/modules/installer/"
g=Fore.WHITE+":"
y=Fore.RED+":"
u=Fore.YELLOW+"="
o=Fore.BLUE+">"
p=Fore.CYAN+">"
A=Fore.WHITE+" "
h=Fore.GREEN+"uid="

while True:
	cmd_ins=[""," ","  ","   ","exit"]
	f2=Fore.RED+"Exector/modules/installer"
	sh2=input(q+e+r+t+w+g+s+f2+d+g+h+slah+"\n"+y+u+o+p+A)
	if sh2=="exit":
		exit()
	if not sh2 in cmd_ins:
		print(Fore.RED+"hatalı komut: "+Fore.CYAN+sh2)
	#https://github.com/SecureAuthCorp/impacket.git

