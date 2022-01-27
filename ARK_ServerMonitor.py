# -*- coding: utf-8 -*-

import subprocess

# Configuration
# Define command to start ARK server program
ARK_START_COMMAND = '/home/user/python/ARK_Server_Monitor/LostIsland_Start.sh'

if __name__ == "__main__":
    # Check all process at the time
    result = subprocess.getoutput('top -n 1')
    # Check if ARK is in working or not
    arkinwork = result.find('Shoot')

    if arkinwork == -1:
        # initialize ARK server program
        subprocess.run(['nohup'ARK_START_COMMAND])
        print('ARK is restarting')
    else:
        print('ARK server is in working now.')