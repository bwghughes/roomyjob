#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def send_heartbeat(device_id, timeout):
    url = "https://roomy.firebaseio.com/{}/heartbeat/".format(device_id)
    response = requests.patch(url, data={'device': device_id}, timeout=timeout)
    return response


def send_event(device_id, image, timeout):
    url = "https://roomy.firebaseio.com/events/"
    response = requests.post(url, data={'device': device_id,
                                        'image': 'https://roomy-pics.s3.com/'
                                        .format(image),
                                        'timestamp': 123456}, timeout=timeout)
    return response
