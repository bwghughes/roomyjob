#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_roomyjob
----------------------------------

Tests for `roomyjob` module.
"""

import json
import httpretty
from pytest import raises
import requests

from roomyjob import send_heartbeat, send_event, InvalidImageException

ROOT_DEVICE_URL = "https://roomy.firebaseio.com/device"
TEST_DEVICE = "test-device"


@httpretty.activate
def test_heartbeat_returns_ok_on_valid_body():
    httpretty.register_uri(httpretty.PATCH,
                           "{}/{}/last-seen.json".format(ROOT_DEVICE_URL,
                                                     TEST_DEVICE),
                           body=json.dumps({"last_seen": 12345678}),
                           content_type="application/json")

    response = send_heartbeat(ROOT_DEVICE_URL, "test-device", 3)
    assert response.status_code == 200
    assert response.json() == {"last_seen": 12345678}


@httpretty.activate
def test_we_can_post_a_valid_event():
    image_url = "https://roomy-pics-blah.com/1.jpg"
    httpretty.register_uri(httpretty.POST,
                           "{}/{}/events.json".format(ROOT_DEVICE_URL,
                                                      TEST_DEVICE),
                           body=json.dumps({"image": image_url,
                                            "timestamp": 123456567}),
                           content_type="application/json")
    response = send_event(ROOT_DEVICE_URL, TEST_DEVICE, image_url, 3)
    assert response.status_code == 200


@httpretty.activate
def test_we_can_post_an_invalid_image_event():
    image_url = "https://roomy-pics-blah.com/1"
    httpretty.register_uri(httpretty.POST,
                           "{}/{}/events/".format(ROOT_DEVICE_URL, TEST_DEVICE),
                           body=json.dumps({"image": image_url,
                                            "timestamp": 123456567}),
                           content_type="application/json")
    with raises(InvalidImageException):
        send_event(ROOT_DEVICE_URL, TEST_DEVICE, image_url, 3)


@httpretty.activate
def test_we_error_on_event_post_connection_timeout():
    image_url = "https://roomy-pics-blah.com/1.jpg"
    httpretty.register_uri(httpretty.POST,
                           "{}/{}/events/".format(ROOT_DEVICE_URL, TEST_DEVICE),
                           body=json.dumps({"image": image_url,
                                            "timestamp": 123456567}),
                           content_type="application/json")
    with raises(requests.exceptions.Timeout):
        send_event(ROOT_DEVICE_URL, TEST_DEVICE, image_url, 0)


@httpretty.activate
def test_we_error_on_heartbeat_patch_connection_timeout():
    httpretty.register_uri(httpretty.PATCH,
                           "{}/{}/heartbeat/".format(ROOT_DEVICE_URL,
                                                     TEST_DEVICE),
                           body=json.dumps({"last_seen": 12345678}),
                           content_type="application/json")

    with raises(requests.exceptions.Timeout):
        send_heartbeat(ROOT_DEVICE_URL, "test-device", 0)
