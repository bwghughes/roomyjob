#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import requests
import logging
logging.basicConfig()


class InvalidImageException(Exception):
    pass


def send_heartbeat(root_url, device_id, timeout):
    url = "{}/{}/heartbeat/".format(root_url, device_id)
    logging.info("Sending heartbeat to {}".format(url))
    try:
        response = requests.patch(url, data={'device': device_id},
                                  timeout=timeout)
        return response
    except requests.exceptions.Timeout, e:
        logging.fatal("Cannot connect to {}".format(url))
        raise e


def send_event(root_url, device_id, image_url, timeout):
    url = "{}/{}/events/".format(root_url, device_id)
    logging.info("Sending event to {}".format(url))
    try:
        if not image_url.endswith('.jpg'):
            raise InvalidImageException
        response = requests.post(url, data={'device': device_id,
                                 'image_url': image_url,
                                 'timestamp': time.time()},
                                 timeout=timeout)
        return response
    except (InvalidImageException, requests.exceptions.Timeout), e:
        if isinstance(e, requests.exceptions.Timeout):
            logging.fatal("Cannot connect to {}".format(url))
            raise e
        else:
            logging.fatal("Invalid image")
            raise e
