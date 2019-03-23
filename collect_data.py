import time
import os
import csv

def check_ping():
    hostname = '"www.google.com"'
    response = os.system("ping -c 1 " + hostname + " > /dev/null")
    # and then check the response...
    if response == 0:
        pingstatus = 1
    else:
        pingstatus = 0

    return pingstatus

with open('haz_ping.csv', mode='w') as haz_ping_file:
    haz_ping = csv.writer(haz_ping_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    haz_ping.writerow(["timestamp", "ping"])
    while (True):
        ping = check_ping()
        print(ping)
        haz_ping.writerow([time.time(), str(ping)])
        time.sleep(1)

        git config --global user.email "zagatta@sonah-parking.com"
  git config --global user.name "zagatta-sonah"
