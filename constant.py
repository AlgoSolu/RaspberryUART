import os
import sys
import signal
import time
#############
# Constants #
DEBUG = False
DEBUG_DB = False
fps = 30
refreshPeriod = int(round(1000/fps))
width = 1184
height = 624
rationX = 0.63
rationY = 0.63
############

def resource_path(relative_path):
    if dev_or_prod() == "prod" :
        base_path = sys._MEIPASS
        print(base_path)
        return os.path.join(base_path, relative_path)
    else:
        return relative_path

def dev_or_prod():
    env = ""
    try:
        base_path = sys._MEIPASS
        env = "prod"
    except Exception as e:
        env = "dev"
    print("Environnement:"+env)
    return env


class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass
 
    def __init__(self, sec):
        self.sec = sec
 
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)
 
    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm
 
    def raise_timeout(self, *args):
        raise Timeout.Timeout()