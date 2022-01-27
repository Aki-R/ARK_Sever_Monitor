# ARK_Sever_Monitor
Python script which monitor ARK server status and restart ARK if it's not active.

Use crontab to periodically activate this script.

ex.) Activate the script every 15 minutes as below 

      */15 * * * * python3 /home/user/python/ARK_Server_Monitor/ARK_ServerMonitor.py
