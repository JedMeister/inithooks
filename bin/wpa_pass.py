#!/usr/bin/python3
# Copyright (c) 2022 TurnKey GNU/Linux <admin@turnkeylinux.org>
"""Set wifi ssid & password

Options (if not provided, will ask interactively):
    -s --ssid=  ssid to connect to
    -p --pass=  password
"""

import sys
import getopt
import subprocess
from subprocess import PIPE
import signal

from libinithooks.dialog_wrapper import Dialog


def fatal(s):
    print("Error:", s, file=sys.stderr)
    sys.exit(1)


def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print(f"Syntax: {sys.argv[0]} [options]", file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)


def main():
    #signal.signal(signal.SIGINT, signal.SIG_IGN)
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "hsp:",
                                       ['help', 'pass=', '-ssid='])
    except getopt.GetoptError as e:
        usage(e)

    ssid = ""
    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-s', '--ssid'):
            ssid = val
        elif opt in ('-p', '--pass'):
            password = val

    if not ssid:
        d = Dialog('TurnKey GNU/Linux - First boot configuration')
        select = d.menu(
                "SSID",
                ["Scan", "Enter Manually", "Enter Manually (hidden)"])
        print(select)

    if not password:
        d = Dialog('TurnKey GNU/Linux - First boot configuration')
        password = d.get_password(
            "Wifi Password",
            f"Please enter wifi password for {ssid}.")
        print(password)


if __name__ == "__main__":
    main()
