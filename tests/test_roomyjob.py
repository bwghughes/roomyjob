#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_roomyjob
----------------------------------

Tests for `roomyjob` module.
"""

import json
import httpretty

from roomyjob import send_heartbeat, send_event


@httpretty.activate
def test_heartbeat_returns_ok_on_valid_body():
    httpretty.register_uri(httpretty.PATCH,
                           "https://roomy.firebaseio.com/roomyTest/heartbeat/",
                           body=json.dumps({"last_seen": 12345678}),
                           content_type="application/json")

    response = send_heartbeat("roomyTest")
    assert response.status_code == 200
    assert response.json() == {"last_seen": 12345678}


@httpretty.activate
def test_we_can_post_a_valid_event():
    device_id = "roomyTest"
    image_url = "https://roomy-pics-blah.com/1.jpg"
    httpretty.register_uri(httpretty.POST,
                           "https://roomy.firebaseio.com/events/",
                           body=json.dumps({"device": device_id,
                                            "image": image_url,
                                            "timestamp": 123456567}),
                           content_type="application/json")

    response = send_event(device_id, image_url)
    assert response.status_code == 200
