#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def send_heartbeat(device_id):
    url = "https://roomy.firebaseio.com/{}/heartbeat/".format(device_id)
    response = requests.patch(url, data={'device': device_id}, timeout=3)
    return response


def send_event(device_id, image):
    url = "https://roomy.firebaseio.com/events/"
    response = requests.post(url, data={'device': device_id,
                                        'image': 'https://roomy-pics.s3.com/'
                                        .format(image),
                                        'timestamp': 123456}, timeout=3)
    return response
