#!/usr/bin/env python3

import fusutils
import subprocess
import uuid
import platform

print("Boot the os ...")
name = str(input("select a username> "))



class MainActivity(object):
    def FusterRunner(username : str):
        while 1:
            user = str(input(f"\n{fusutils.Symbols.upper()}{username}\n{fusutils.Symbols.base()}{fusutils.PathWorker.DirectoryRunner()}\n{fusutils.Symbols.under()}fuster> "))

            if fusutils.String(user).startsWith("loop-install"):
                if platform.system() == "Windows" or platform.system() == "windows":
                    print("\nThe 'loop-install' command is for termux Users")
                    
                else:
                    textor = fusutils.String(user).replacer("loop-install ", "")
                    subprocess.getoutput(f"pkg install {textor}")
                    
            elif fusutils.String(user).startsWith("git"):
                textor = fusutils.String(user).replacer("git ", "")
                us = fusutils.String(textor).splitter()
                
                if "dl" == us[0]:
                    try:
                        link = us[fusutils.List(us).indexOf("dl")+1]
                        print(subprocess.getoutput(f"git clone https://github.com/{link}"))
                    except Exception as e:
                        print(e)
                        pass
                else:
                    print("Please Set Method:\n    dl")
                    pass
            
            elif fusutils.String(user).startsWith("kop"):
                try:
                    cmd = fusutils.String(user).replacer("kop ", "")
                    
                    if cmd == "kop" or cmd == "":
                        print("\nkop: does not get any data")
                    else:
                        if fusutils.String(cmd).startsWith("cd"):
                            pathx = fusutils.String(cmd).splitter("cd")
                            if pathx[0] == "cd" or pathx[0] == "" or pathx[0] == IndexError:
                                print("kop: cd was not get any directory")
                            else:
                                fusutils.PathWorker.changeWay(pathx)
                        else:
                            print(subprocess.getoutput(cmd))
                except Exception as e:
                    print(e)

            elif user == "exit":
                exit("\nShutting Down OS ...\n")
            
            else:
                print("\nunknown command: {}".format(user))

if name == "" or name == " " or name == None:
    namex = uuid.uuid4().hex
    print(f"username> {namex}")
    print(f"Welcome to Fuster OS {namex} !")
    MainActivity.FusterRunner(namex)

else:
    print(f"username> {name}")
    print(f"Welcome to Fuster OS {name} !")
    MainActivity.FusterRunner(name)
