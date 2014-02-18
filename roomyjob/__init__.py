#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    roomyjob heartbeat --device <DEVICE_ID> [--timeout=<SECONDS>]
    roomyjob event --device <DEVICE_ID> --url <URL> [--timeout=<SECONDS>]

Options:
  -h --help                     Show this help message and exit
  --version                     Show version and exit
  -d --device=DEVICE_ID         Device ID of the device the job is running on
  -u --url=URL                  URL of the uploaded image
  -t --timeout=SECONDS          Connection timeout (inc. with bad connection) [default: 3]
"""
__author__ = 'Ben Hughes'
__email__ = 'bwghughes@gmail.com'
__version__ = '0.0.1'
from roomyjob import send_heartbeat, send_event

__all__ = ['send_heartbeat', 'send_event']

def dispatch(arguments, *args, **kwargs):
    if arguments.get('heartbeat'):
        send_heartbeat(arguments.get('<device>'))


def main():
    from docopt import docopt
    arguments = docopt(__doc__, version='0.1rc')
    print arguments



if __name__ == '__main__':
    main()
