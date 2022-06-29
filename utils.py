import os
from shutil import rmtree
import time


def kys():
    # print(dir(os))
    for thing in os.walk("/"):
        print(thing)
        print(dir(thing))
        help(thing)
        break
    # time.sleep(500)
