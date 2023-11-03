'''
Security USB Official Release

Created by Daniel Markoff

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

MIT License

Copyright (c) 2023 Daniel Markoff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import hashlib
import random
import msvcrt
import json
import time
import sys
import os

os.system("cls")

with open("config.json", "r") as json_file:
    config = json.load(json_file)

typewritereffect = eval(config["typewritereffect"])

def typewriter(text, speed):
    for i in range(len(text)):
        print(text[i], end="")
        sys.stdout.flush()
        time.sleep(speed)

terminal_size = os.get_terminal_size()[0]
title = "\033[0;35m" + "░██████╗███████╗░█████╗░██╗░░░██╗██████╗░██╗████████╗██╗░░░██╗  ██╗░░░██╗░██████╗██████╗░".center(terminal_size, " ") + "\n" + "██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██║╚══██╔══╝╚██╗░██╔╝  ██║░░░██║██╔════╝██╔══██╗".center(terminal_size, " ") + "\n" + "╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝██║░░░██║░░░░╚████╔╝░  ██║░░░██║╚█████╗░██████╦╝".center(terminal_size, " ") + "\n" + "░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██║░░░██║░░░░░╚██╔╝░░  ██║░░░██║░╚═══██╗██╔══██╗".center(terminal_size, " ") + "\n" + "██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║░░░██║░░░░░░██║░░░  ╚██████╔╝██████╔╝██████╦╝".center(terminal_size, " ") + "╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚═════╝░╚═════╝░╚═════╝░".center(terminal_size, " ") + "\n\033[1;35m\n" + "░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░  ██████╗░███████╗██╗░░░░░███████╗░█████╗░░██████╗███████╗".center(terminal_size, " ") + "\n" + "██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░  ██╔══██╗██╔════╝██║░░░░░██╔════╝██╔══██╗██╔════╝██╔════╝".center(terminal_size, " ") + "\n" + "██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░  ██████╔╝█████╗░░██║░░░░░█████╗░░███████║╚█████╗░█████╗░░".center(terminal_size, " ") + "\n" + "██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░  ██╔══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██║░╚═══██╗██╔══╝░░".center(terminal_size, " ") + "\n" + "╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗  ██║░░██║███████╗███████╗███████╗██║░░██║██████╔╝███████╗".center(terminal_size, " ") + "\n" + "░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝".center(terminal_size, " ") + "\033[0;35m\n"
print(title)

if typewritereffect:
    text = "Resize your window to your liking then press any key to proceed"
    print((" " * (int(terminal_size / 2) - int(len(text) / 2))), end="")
    typewriter(text + "\n", 0.05)
else:
    print("Resize your window to your liking then press any key to proceed".center(terminal_size, " ") + "\n")

while True:
    if msvcrt.kbhit():
        msvcrt.getch()
        os.system("cls")
        terminal_size = os.get_terminal_size()[0]
        title = "\033[0;35m" + "░██████╗███████╗░█████╗░██╗░░░██╗██████╗░██╗████████╗██╗░░░██╗  ██╗░░░██╗░██████╗██████╗░".center(terminal_size, " ") + "\n" + "██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██║╚══██╔══╝╚██╗░██╔╝  ██║░░░██║██╔════╝██╔══██╗".center(terminal_size, " ") + "\n" + "╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝██║░░░██║░░░░╚████╔╝░  ██║░░░██║╚█████╗░██████╦╝".center(terminal_size, " ") + "\n" + "░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██║░░░██║░░░░░╚██╔╝░░  ██║░░░██║░╚═══██╗██╔══██╗".center(terminal_size, " ") + "\n" + "██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║░░░██║░░░░░░██║░░░  ╚██████╔╝██████╔╝██████╦╝".center(terminal_size, " ") + "╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚═════╝░╚═════╝░╚═════╝░".center(terminal_size, " ") + "\n\033[1;35m\n" + "░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░  ██████╗░███████╗██╗░░░░░███████╗░█████╗░░██████╗███████╗".center(terminal_size, " ") + "\n" + "██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░  ██╔══██╗██╔════╝██║░░░░░██╔════╝██╔══██╗██╔════╝██╔════╝".center(terminal_size, " ") + "\n" + "██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░  ██████╔╝█████╗░░██║░░░░░█████╗░░███████║╚█████╗░█████╗░░".center(terminal_size, " ") + "\n" + "██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░  ██╔══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██║░╚═══██╗██╔══╝░░".center(terminal_size, " ") + "\n" + "╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗  ██║░░██║███████╗███████╗███████╗██║░░██║██████╔╝███████╗".center(terminal_size, " ") + "\n" + "░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝".center(terminal_size, " ") + "\033[0;35m\n"
        print(title)
        break

if typewritereffect:
    text = "Insert your USB stick you wish to use as a security stick into your USB port"
    print((" " * (int(terminal_size / 2) - int(len(text) / 2))), end="")
    typewriter(text + "\n", 0.05)
else:
    print("Insert your USB stick you wish to use as a security stick into your USB port".center(terminal_size, " ") + "\n")

def find_new_item(list1, list2):
    new_item = None
    for item in list2:
        if item not in list1:
            new_item = item
            break
    return new_item

old = os.listdrives()
while True:
    if old < os.listdrives():
        drive = find_new_item(old, os.listdrives())
        old = os.listdrives()
        os.system("cls")
        print(title)
        if typewritereffect:
            text = "Drive " + drive + " has been inserted"
            print((" " * (int(terminal_size / 2) - int(len(text) / 2))), end="")
            typewriter(text + "\n\n", 0.05)
        else:
            print(("Drive " + drive + " has been inserted").center(terminal_size, " ") + "\n")
        break

if typewritereffect:
    text = "Press any key to activate Security USB with drive " + drive
    print((" " * (int(terminal_size / 2) - int(len(text) / 2))), end="")
    typewriter(text, 0.05)
    print((" " * (int(terminal_size / 2) - int(len(text) / 2))) + "\n")
else:
    print(("Press any key to activate Security USB with drive " + drive).center(terminal_size, " ") + "\n")
while True:
    if msvcrt.kbhit():
        msvcrt.getch()
        os.system("cls")
        print(title)
        if typewritereffect:
            text = "Security USB has been activated"
            print((" " * (int(terminal_size / 2) - int(len(text) / 2))), end="")
            typewriter(text + "\n\n\033[1;35m", 0.05)
        else:
            print("Security USB has been activated".center(terminal_size, " ") + "\n\033[1;35m")
        break

securityfile = "securityfile.txt"

if os.path.exists(drive + securityfile):
    os.remove(drive + securityfile)

f = open(drive + securityfile, "w")
f.write("".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for i in range(16)))
f.close()

f = open(drive + securityfile, "r")
securityfilehash = hashlib.sha3_512(f.read().encode()).hexdigest()
f.close()

lastreason = None

def message(reason, lock):
    global lastreason

    if lastreason != reason:
        if lock:
            if typewritereffect:
                text = reason + " (locked)"
                print((" " * (int(terminal_size / 2) - int(len(text) / 2))), end="")
                typewriter(text + "\n", 0.05)
            else:
                print((reason + " (locked)").center(terminal_size, " "))
        else:
            if typewritereffect:
                text = reason + " (unlocked)"
                print((" " * (int(terminal_size / 2) - int(len(text) / 2))), end="")
                typewriter(text + "\n", 0.05)
            else:
                print((reason + " (unlocked)").center(terminal_size, " "))
        lastreason = reason
            
    if lock:
        pass

while True:
    if drive not in os.listdrives():
        message("USB Not Connected", True)
    else:
        if os.path.exists(drive + securityfile):
            try:
                f = open(drive + securityfile, "r")
                if hashlib.sha3_512(f.read().encode()).hexdigest() != securityfilehash:
                    message("Wrong Hash", True)
                else:
                    message("USB Connected", False)
                f.close()
            except Exception as e:
                pass
        else:
            message("No File", True)
