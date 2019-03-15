#!/usr/bin/env python3

import subprocess

command = '/home/pi/test/printer_server.py /home/pi/test/{0}'.format('data.json')

process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
