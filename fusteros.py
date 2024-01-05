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
                        subprocess.getoutput(f"git clone https://github.com/{link}")
                    except Exception as e:
                        print(e)
                        pass
                else:
                    print("Please Set Method:\n    dl")
                    pass

if name == "" or name == " " or name == None:
    namex = uuid.uuid4().hex
    print(f"username> {namex}")
    print(f"Welcome to Fuster OS {namex} !")
    MainActivity.FusterRunner(namex)

else:
    print(f"username> {name}")
    print(f"Welcome to Fuster OS {name} !")
    MainActivity.FusterRunner(name)
