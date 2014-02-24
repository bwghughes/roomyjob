#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_roomyjob
----------------------------------

Tests for `roomyjob` module.
"""

from mock import patch
import roomyjob
from roomyjob import dispatch


def test_module_headers():
    assert roomyjob.__author__
    assert roomyjob.__email__
    assert roomyjob.__version__


def test_dispatch_calls_heartbeat():
    with patch.object(roomyjob, 'send_heartbeat') as mock_send_heartbeat:
        arguments = {'--device': 'roomy-test', 'heartbeat': True,
                     '--timeout': 1}
        dispatch(arguments)
        mock_send_heartbeat.assert_called_once


def test_defaults():
    with patch.object(roomyjob, 'send_heartbeat') as mock_send_heartbeat:
        arguments = {'--device': 'roomy-test', 'heartbeat': True}
        dispatch(arguments)
        assert arguments.get('--timeout') == 3
        mock_send_heartbeat.assert_called_once


def test_dispatch_calls_send_event():
    with patch.object(roomyjob, 'send_event') as mock_send_event:
        arguments = {'--device': 'roomy-test', 'event': True,
                     '--timeout': 1}
        dispatch(arguments)
        mock_send_event.assert_called_once
