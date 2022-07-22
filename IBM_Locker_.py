
"""
Folder / File Locking of Our Devices: in 2 modes
1. To Encrypt Them- Un-accessible
2. To Decrypt Them as before condition- Accessible.

### First create password (master pass: like_mazharul_121_bhuiyan )file in our preferred drive  if not exists
###if forget : reset()
"""
import os
import base64

import time
import sys
import win32api


def goto(linenum):
    global line
    line = linenum


def set_Password():
    obj = open("d:\SecretPasswordFile.txt", "w")
    obj.write(base64.b64encode(input("Set Your Password: ")))
    obj.close()
    drive = str(input("Which drive You want to create Locker Folder: "))
    os.chdir(drive)
    if not os.path.exists("Locker"):
        if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
            os.mkdir("Locker")
            sys.exit()
        else:
            sys.exit()
    else:
        sys.exit()


if not os.path.exists("d:\SecretPasswordFile.txt"):
    set_Password()

passwordFile = open('d:\SecretPasswordFile.txt', 'r')
pw = passwordFile.read()
passwordFile.close()

encode = base64.b64decode(pw+'==')


def reset_password():
    password = str(input("Enter your current password: "))
    if password:
        obj = open("d:\SecretPasswordFile.txt", "w")
        encoded_ = base64.b64encode(bytes(input("Set Your Password: "), encoding="utf8"))
        obj.write(str(encoded_))
        obj.close()
        win32api.MessageBox(0, 'Your password Successfully Reset', 'Password')
        sys.exit()
    else:
        # print("You entered", password, "But Your Password Was:", encode)
        win32api.MessageBox(0, 'Your current password does not match', 'Password')
        os.system('cls')
        reset_password()


line = 1
while True:
    pw = str(input("Enter your password for Lock or Unlock your folder: "))
    if pw == "121789":
        reset_password()

    if pw == encode:
        # Change Dir Path where you have Locker Folder
        drive = str(input("Which drive You want to access Locker Folder: "))
        os.chdir(drive)
        # If Locker folder or Recycle bin does not exist then we will be create Locker Folder
        if not os.path.exists("Locker"):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Locker")
                sys.exit()
            else:
                os.popen('attrib -h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                sys.exit()
        else:
            os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            sys.exit()

    else:
        win32api.MessageBox(0, 'Wrong password!, Please Enter right password', 'Password')
        os.system('cls')
        goto(1)